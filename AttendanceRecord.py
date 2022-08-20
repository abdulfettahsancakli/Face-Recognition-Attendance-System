
from tkinter import *
from tkinter import ttk

import label as label
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkcalendar import Calendar, DateEntry
import cv2
import PyQt5

class AttendanceRecord:
   def __init__(self, root):
     self.root = root
     self.root.geometry("1200x675+0+0")
     self.root.title("DataList")

     self.var_dt=StringVar()
     self.var_dt2=StringVar()


     img2 = Image.open(r"Images\Best-attendance-tracking-software.jpg")
     img2 = img2.resize((1200, 180), Image.ANTIALIAS)
     self.photoimg2 = ImageTk.PhotoImage(img2)

     f_lbl = Label(self.root, image=self.photoimg2)
     f_lbl.place(x=0, y=0)

     main_frame = Frame(self.root, bd=2, bg="#888888")
     main_frame.place(x=0, y=180, width=1200, height=675)

     #Searching System in Right Label Frame
     search_frame = LabelFrame(main_frame,bd=2,bg="#888888",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="black")
     search_frame.place(x=0,y=0,width=1200,height=500)

     DataFrom = Label(search_frame, text="Date From :", font=("verdana", 12, "bold"), fg="black",bg="#888888")
     DataFrom.place(x=0,y=8)


     DataTo = Label(search_frame, text="Date To :", font=("verdana", 12, "bold"), fg="black", bg="#888888")
     DataTo.place(x=0, y=245)

     searchbydate_label = Label(search_frame, text="Search By Date", font=("verdana", 12, "bold"), fg="black",bg="#888888" )
     searchbydate_label.place(x=230,y=-10)

     search_label = Label(search_frame, text="Search Student Name:", font=("verdana", 12, "bold"), fg="black",bg="#888888" )
     search_label.place(x=420,y=-10)

     self.var_search = StringVar()
     search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width=16, font=("verdana", 12, "bold"))
     # search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)
     search_entry.place(x=625, y=-8)

     allstudents = Label(search_frame, text="See All Attendance ", font=("verdana", 12, "bold"), fg="black",bg="#888888")
     allstudents.place(x=875, y=-10)

     showallicon = Image.open(r"Images\all.png")
     showallicon = showallicon.resize((64, 64), Image.ANTIALIAS)
     self.photoshowallicon = ImageTk.PhotoImage(showallicon)

     show = Button(search_frame, command=self.fetch_data, bg="white", image=self.photoshowallicon, cursor="hand2")
     show.place(x=925, y=15, width=70, height=70)



     def selectDate():
       myDate=myCal.get_date()
       SelectedDate=Label(search_frame,text=myDate,bg="yellow",font=("times new roman", 15, "bold"))
       self.var_dt=SelectedDate['text']
       #print(self.var_dt)
       SelectedDate.place(x=110,y=8)

     def selectDate2():
       myDate2=myCal2.get_date()
       SelectedDate2=Label(search_frame,text=myDate2,bg="yellow",font=("times new roman", 12, "bold"))
       self.var_dt2 = SelectedDate2['text']
       SelectedDate2.place(x=90,y=245)



     myCal=Calendar(search_frame,setmde="day",date_pattern="dd/mm/yyyy")
     myCal.place(x=0,y=50)

     pickdateicon = Image.open(r"Images\PickDate.png")
     pickdateicon = pickdateicon.resize((30,30), Image.ANTIALIAS)
     self.photopickdateicon = ImageTk.PhotoImage(pickdateicon)

     openCal=Button(search_frame,text="Pick Date",command=selectDate,image=self.photopickdateicon)
     openCal.place(x=125,y=37)

     myCal2 = Calendar(search_frame, setmde="day", date_pattern="dd/mm/yyyy")
     myCal2.place(x=0, y=280)

     openCal2 = Button(search_frame, text="Select Date",command=selectDate2,image=self.photopickdateicon)
     openCal2.place(x=125,y=267)


     searchicon2 = Image.open(r"Images\magnifier.png")
     searchicon2 = searchicon2.resize((64, 64), Image.ANTIALIAS)
     self.photosearchicon2 = ImageTk.PhotoImage(searchicon2)

     search2 = Button(search_frame, command=self.search_data, bg="white", image=self.photosearchicon2, cursor="hand2")
     search2.place(x=500, y=15, width=70, height=70)

     searchicon = Image.open(r"Images\searchdateicon2.jpg")
     searchicon = searchicon.resize((64, 64), Image.ANTIALIAS)
     self.photosearchicon = ImageTk.PhotoImage(searchicon)

     search = Button(search_frame, command=self.searchdate,bg="white", image=self.photosearchicon, cursor="hand2")
     search.place(x=260, y=15, width=70, height=70)



     # Table Frame
     # Searching System in Right Label Frame
     table_frame = Frame(search_frame, bd=2, bg="white", relief=RIDGE)
     table_frame.place(x=270, y=100, width=900, height=360)

     scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
     scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

     self.student_table = ttk.Treeview(table_frame, column=(
         "StudentName", "Department", "Time","Status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

     scroll_x.pack(side=BOTTOM, fill=X)
     scroll_y.pack(side=RIGHT, fill=Y)
     scroll_x.config(command=self.student_table.xview)
     scroll_y.config(command=self.student_table.yview)

     self.student_table.heading("StudentName", text="StudentName")
     self.student_table.heading("Department", text="Department")
     self.student_table.heading("Time", text="Time")
     self.student_table.heading("Status", text="Status")
     self.student_table["show"] = "headings"

     self.student_table.column("StudentName", width=90)
     self.student_table.column("Department", width=90)
     self.student_table.column("Time", width=90)
     self.student_table.column("Status", width=90)

     self.student_table.pack(fill=BOTH, expand=1)
     self.student_table.bind("<ButtonRelease>")
     self.fetch_data()

   def searchdate(self):
     try:
       print(self.var_dt)
       print(self.var_dt2)
       conn = mysql.connector.connect(username='root', password='g9vscqk5', host='localhost',
                                      database='face_recognizer')
       my_cursor = conn.cursor()
       #my_cursor.execute(("SELECT * from attendance where time  "'+self.var_dt+'""))
       my_cursor.execute(("SELECT * from attendance where time between '" + self.var_dt + "%' AND '" + self.var_dt2 + "'"))
       #my_cursor.execute(("SELECT * from attendance where TIME between "'+ self.var_dt +'"  AND "'+self.var_dt2 +'""))
       rows = my_cursor.fetchall()


       if len(rows) != 0:
         self.student_table.delete(*self.student_table.get_children())
         for i in rows:
           self.student_table.insert("", END, values=i)
       else:
         messagebox.showerror("Error", "Data Not Found", parent=self.root)
         conn.commit()
       conn.close()
     except Exception as es:
       messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

   def search_data(self):
     if self.var_search.get() == "" :
       messagebox.showerror("Error", "Please write a student id", parent=self.root)
     else:
       try:
         conn = mysql.connector.connect(username='root', password='g9vscqk5', host='localhost',database='face_recognizer')
         my_cursor = conn.cursor()
         my_cursor.execute(("SELECT * from attendance where StudentName LIKE '%"+self.var_search.get()+"%'"))
         rows = my_cursor.fetchall()

         if len(rows) != 0:
           self.student_table.delete(*self.student_table.get_children())
           for i in rows:
             self.student_table.insert("", END, values=i)
         else:
             messagebox.showerror("Error", "Data Not Found", parent=self.root)
             conn.commit()
         conn.close()
       except Exception as es:
         messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)


   def fetch_data(self):
         conn = mysql.connector.connect(host="localhost", username="root", password="g9vscqk5",database="face_recognizer")
         my_cursor = conn.cursor()
         my_cursor.execute("select * from attendance")
         data = my_cursor.fetchall()

         if len(data) != 0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("", END, values=i)
                 conn.commit()
             conn.close()



if __name__ == "__main__":
    root = Tk()
    obj = AttendanceRecord(root)
    root.mainloop()
