from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import PyQt5

class DataList:
   def __init__(self, root):
     self.root = root
     self.root.geometry("1200x675+0+0")
     self.root.title("DataList")

     img2 = Image.open(r"Images_GUI\Search.jpg")
     img2 = img2.resize((1200, 180), Image.ANTIALIAS)
     self.photoimg2 = ImageTk.PhotoImage(img2)

     f_lbl = Label(self.root, image=self.photoimg2)
     f_lbl.place(x=0, y=0)

     main_frame = Frame(self.root, bd=2, bg="#888888")
     main_frame.place(x=0, y=180, width=1200, height=675)

     #Searching System in Right Label Frame
     search_frame = LabelFrame(main_frame,bd=2,bg="#888888",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="black")
     search_frame.place(x=0,y=0,width=1200,height=500)

     # Search Label
     search_label = Label(search_frame, text="Search Student ID:", font=("verdana", 12, "bold"), fg="black",bg="#888888" )
     search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
     search_label.place(x=330,y=25)

     self.var_search = StringVar()
     search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width=16, font=("verdana", 12, "bold"))
     # search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)
     search_entry.place(x=515,y=25)


     searchicon = Image.open(r"Images_GUI\magnifier.png")
     searchicon = searchicon.resize((64, 64), Image.ANTIALIAS)
     self.photosearchicon = ImageTk.PhotoImage(searchicon)

     search = Button(search_frame, command=self.search_data,bg="white", image=self.photosearchicon, cursor="hand2")
     search.place(x=720, y=0, width=70, height=70)

     showallicon = Image.open(r"Images_GUI\all.png")
     showallicon = showallicon.resize((64, 64), Image.ANTIALIAS)
     self.photoshowallicon = ImageTk.PhotoImage(showallicon)

     show = Button(search_frame, command=self.fetch_data, bg="white", image=self.photoshowallicon, cursor="hand2")
     show.place(x=820, y=0, width=70, height=70)

     # Table Frame
     # Searching System in Right Label Frame
     table_frame = Frame(search_frame, bd=2, bg="white", relief=RIDGE)
     table_frame.place(x=50, y=90, width=1100, height=360)

     scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
     scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

     self.student_table = ttk.Treeview(table_frame, column=(
         "Faculty", "Department", "Year", "Semester", "Class", "Student ID", "Student Name", "Date of Birth",
         "Mobile Number", "Gender"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

     scroll_x.pack(side=BOTTOM, fill=X)
     scroll_y.pack(side=RIGHT, fill=Y)
     scroll_x.config(command=self.student_table.xview)
     scroll_y.config(command=self.student_table.yview)

     self.student_table.heading("Faculty", text="Faculty")
     self.student_table.heading("Department", text="Department")
     self.student_table.heading("Year", text="Year")
     self.student_table.heading("Semester", text="Semester")
     self.student_table.heading("Class", text="Class")
     self.student_table.heading("Student ID", text="ID")
     self.student_table.heading("Student Name", text="Name")
     self.student_table.heading("Date of Birth", text="Birthday")
     self.student_table.heading("Mobile Number", text="Phone")
     self.student_table.heading("Gender", text="Gender")
     self.student_table["show"] = "headings"

     self.student_table.column("Faculty", width=90)
     self.student_table.column("Department", width=90)
     self.student_table.column("Year", width=90)
     self.student_table.column("Semester", width=90)
     self.student_table.column("Class", width=90, )
     self.student_table.column("Student ID", width=90)
     self.student_table.column("Student Name", width=90)
     self.student_table.column("Date of Birth", width=90)
     self.student_table.column("Mobile Number", width=90)
     self.student_table.column("Gender", width=90)

     self.student_table.pack(fill=BOTH, expand=1)
     self.student_table.bind("<ButtonRelease>")
     self.fetch_data()


   def search_data(self):
     if self.var_search.get() == "" :
       messagebox.showerror("Error", "Please write a student id", parent=self.root)
     else:
       try:
         conn = mysql.connector.connect(username='root', password='g9vscqk5', host='localhost',database='face_recognizer')
         my_cursor = conn.cursor()
         my_cursor.execute(("SELECT * from unistudents where Studentid LIKE '%"+self.var_search.get()+"%'"))
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
         my_cursor.execute("select * from unistudents")
         data = my_cursor.fetchall()

         if len(data) != 0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("", END, values=i)
                 conn.commit()
             conn.close()



if __name__ == "__main__":
    root = Tk()
    obj = DataList(root)
    root.mainloop()
