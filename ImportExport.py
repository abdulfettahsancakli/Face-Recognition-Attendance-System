import contextlib
import csv
import os
from tkinter import *
from tkinter import ttk, filedialog

import pymysql
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import PyQt5
Mydata = []
class ImportExport:
   def __init__(self, root):
     self.root = root
     self.root.geometry("1200x675+0+0")
     self.root.title("Import & Export")

     self.var_faculty = StringVar()
     self.var_department = StringVar()
     self.var_time2=StringVar()
     self.var_year = StringVar()
     self.var_semester = StringVar()
     self.var_class = StringVar()
     self.var_std_id = StringVar()
     self.var_std_name = StringVar()
     self.var_dob = StringVar()
     self.var_mob = StringVar()
     self.var_gender = StringVar()
     self.var_time =StringVar()

     img2 = Image.open(r"Images_GUI\impexp.jpg")
     img2 = img2.resize((1200, 180), Image.ANTIALIAS)
     self.photoimg2 = ImageTk.PhotoImage(img2)

     f_lbl = Label(self.root, image=self.photoimg2)
     f_lbl.place(x=0, y=0)

     main_frame = Frame(self.root, bd=2, bg="#888888")
     main_frame.place(x=0, y=180, width=350, height=675)

     main_frame2 = Frame(self.root, bd=2, bg="#888888")
     main_frame2.place(x=350, y=180, width=350, height=675)

     faculty = Image.open(r"Images_GUI\AttendanceReport.jpg")
     faculty = faculty.resize((400, 495), Image.ANTIALIAS)
     self.photofaculty = ImageTk.PhotoImage(faculty)

     f_lbl = Label(main_frame, image=self.photofaculty)
     f_lbl.place(x=0, y=-5, width=400)

     main_frame3 = Frame(self.root, bd=2, bg="#888888")
     main_frame3.place(x=700, y=180, width=500, height=675)

     # =========================Student ID Entry================================
     studentID_label = Label(main_frame2, text="Student Name : ", font=("times new roman", 15, "bold"), bg="#888888")
     studentID_label.place(x=5, y=45)

     studentID_entry = ttk.Entry(main_frame2, textvariable=self.var_std_name, width=20,
                                 font=("times new roman", 12, "bold"))
     studentID_entry.place(x=140, y=50)
     # ========================================================================

     # =========================Student Name Entry================================
     studentName_label = Label(main_frame2, text="Department : ", font=("times new roman", 15, "bold"), bg="#888888")
     studentName_label.place(x=20, y=115)

     studentName_entry = ttk.Entry(main_frame2, textvariable=self.var_department, width=20,
                                   font=("times new roman", 12, "bold"))
     studentName_entry.place(x=140, y=118)
     # ========================================================================

     # =========================Date Of Birth================================
     studentdob_label = Label(main_frame2, text="Date :  ", font=("times new roman", 15, "bold"), bg="#888888")
     studentdob_label.place(x=75, y=180)

     studentdob_entry = ttk.Entry(main_frame2, textvariable=self.var_time, width=20,
                                  font=("times new roman", 12, "bold"))
     studentdob_entry.place(x=140, y=180)
     # ========================================================================

     # =========================Time =================================
     studentMobileNo_label = Label(main_frame2, text="Time :  ", font=("times new roman", 15, "bold"),
                                   bg="#888888")
     studentMobileNo_label.place(x=70, y=245)

     studentMobileNo_entry = ttk.Entry(main_frame2, width=20,textvariable=self.var_time2,
                                       font=("times new roman", 12, "bold"))
     studentMobileNo_entry.place(x=140, y=245)
     # ========================================================================

     # =========================Gender Combobox============================================
     gender_label = Label(main_frame2, text="Status : ", font=("times new roman", 15, "bold"), bg="#888888")
     gender_label.place(x=60, y=310)
     # ========================================================================
     gender_combo = ttk.Combobox(main_frame2, textvariable=self.var_gender, font=("times new roman", 12, "bold"),
                                 state="readonly", width=20)
     gender_combo["values"] = ("Status", "Present", "Absent")
     gender_combo.current(0)
     gender_combo.place(x=140, y=315)
     # ========================================================================

     # =================TABLE FRAME =============#
     table_frame = Frame(main_frame3, bd=2, bg="white", relief=RIDGE)
     table_frame.place(x=0, y=0, width=495, height=260)

     scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
     scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

     self.student_table = ttk.Treeview(table_frame,
                                       column=("StudentName", "Department", "Date", "Time", "Status"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

     scroll_x.pack(side=BOTTOM, fill=X)
     scroll_y.pack(side=RIGHT, fill=Y)
     scroll_x.config(command=self.student_table.xview)
     scroll_y.config(command=self.student_table.yview)

     self.student_table.heading("StudentName", text="Student Name")
     self.student_table.heading("Department", text="Department")
     self.student_table.heading("Date", text="Date")
     self.student_table.heading("Time", text="Time")
     self.student_table.heading("Status", text="Status")

     self.student_table["show"] = "headings"

     self.student_table.column("StudentName", width=98)
     self.student_table.column("Department", width=98)
     self.student_table.column("Date", width=98)
     self.student_table.column("Time", width=98)
     self.student_table.column("Status", width=98)

     self.student_table.pack(fill=BOTH, expand=1)
     self.student_table.bind("<ButtonRelease>", self.get_cursor)
     #self.fetch_data()

     # =========================Buttons =================================
     # =========================Save =================================
     save = Image.open(r"Images_GUI\icons8-import-csv-80.png")
     save = save.resize((80, 80), Image.ANTIALIAS)
     self.photosave = ImageTk.PhotoImage(save)

     b1 = Button(main_frame3,command=self.importCsv,image=self.photosave, cursor="hand2")
     b1.place(x=20, y=290, width=80, height=80)

     b1_1 = Button(main_frame3, text="Import", cursor="hand2", command=self.importCsv, font=("times new roman", 15, "bold"),
                   bg="#888888",
                   fg="black")
     b1_1.place(x=20, y=370, width=80, height=40)

     # =========================Update =================================

     updt = Image.open(r"Images_GUI\Update.webp")
     updt = updt.resize((80, 80), Image.ANTIALIAS)
     self.photoupdt = ImageTk.PhotoImage(updt)

     b1 = Button(main_frame3,command=self.action, image=self.photoupdt, cursor="hand2")
     b1.place(x=150, y=290, width=80, height=80)

     # =========================Export Csv =================================
     dlt = Image.open(r"Images_GUI\icons8-export-csv-80.png")
     dlt = dlt.resize((80, 80), Image.ANTIALIAS)
     self.photodlt = ImageTk.PhotoImage(dlt)

     b1 = Button(main_frame3,command=self.exportCsv, image=self.photodlt, cursor="hand2")
     b1.place(x=280, y=290, width=80, height=80)

     b1_2 = Button(main_frame3, text="Export", cursor="hand2", command=self.exportCsv,
                   font=("times new roman", 15, "bold"),
                   bg="#888888",
                   fg="black")
     b1_2.place(x=280, y=370, width=80, height=40)

     # =========================Reset =================================
     rst = Image.open(r"Images_GUI\reset.jpg")
     rst = rst.resize((80, 80), Image.ANTIALIAS)
     self.photorst = ImageTk.PhotoImage(rst)

     b1 = Button(main_frame3,command=self.reset_data,image=self.photorst, cursor="hand2")
     b1.place(x=410, y=290, width=80, height=80)

   def fetch_data(self):
       conn = mysql.connector.connect(host="localhost", username="root", password="g9vscqk5",
                                      database="face_recognizer")
       my_cursor = conn.cursor()
       my_cursor.execute("select * from attendance")
       data = my_cursor.fetchall()

       if len(data) != 0:
           self.student_table.delete(*self.student_table.get_children())
           for i in data:
               self.student_table.insert("", END, values=i)
               conn.commit()
           conn.close()

   def fetchData(self, rows):
       global mydata
       mydata = rows
       self.student_table.delete(*self.student_table.get_children())
       for i in rows:
           self.student_table.insert("", END, values=i)

   def get_cursor(self, event=""):
       cursor_focus = self.student_table.focus()
       content = self.student_table.item(cursor_focus)
       data = content["values"]
       # self.var_faculty.set(data[0]),
       self.var_time2.set(data[3]),
       self.var_department.set(data[1]),
       self.var_time.set(data[2]),
       # self.var_year.set(data[2]),
       # self.var_semester.set(data[3]),
       # self.var_class.set(data[4]),
       # self.var_std_id.set(data[5]),
       self.var_std_name.set(data[0]),
       # self.var_dob.set(data[7]),
       # self.var_mob.set(data[8]),

       self.var_gender.set(data[4])

   #export upadte
   def action(self):
       if self.var_time.get() == "" :
          messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
       else:
               try:
                   conn = mysql.connector.connect(host="localhost", username="root", password="g9vscqk5",database="face_recognizer")
                   mycursor = conn.cursor()
                   mycursor.execute("UPDATE attendance SET Status=%s where date=%s", (

                       self.var_gender.get(),
                       self.var_time.get()
                       #self.var_std_name.get()
                   ))

                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success", "All Records are Saved in Database!", parent=self.root)
               except Exception as es:
                   messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    #export csv
   def exportCsv(self):
        # try:
        #     if len(Mydata)<1:
        #         messagebox.showerror("No Data","No Data found to export",parent=self.root)
        #         return False
        #     filename=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        #     with open(filename,mode="w",newline="") as myfile:
        #         exp_write=csv.writer(myfile,delimiter=",")
        #         for i in Mydata:
        #           exp_write.writerow(i)
        #         messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(filename)+"succesfully")
        # except Exception as es :
        #         messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        SQL_QUERY = "SELECT * FROM attendance "

        # embedding passwords in code gets nasty when you use version control
        # the environment is not much better, but this is an example
        # https://stackoverflow.com/questions/12461484
        # SQL_USER = os.environ["root"]
        # SQL_PASS = os.environ['g9vscqk5']

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='g9vscqk5',
                                     db='face_recognizer')

        with contextlib.closing(connection):
            with connection.cursor() as cursor:
                cursor.execute(SQL_QUERY)
                # Hope you have enough memory :)
                results = cursor.fetchall()

        filename=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        #output_file = 'TodayAttendance706.csv'
        with open(filename, 'w', newline='') as csvfile:
            # http://stackoverflow.com/a/17725590/2958070 about lineterminator
            csv_writer = csv.writer(csvfile, lineterminator='\n')
            csv_writer.writerows(results)
        messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(filename)+"succesfully")

   #import csv
   def importCsv(self):
        global Mydata
        Mydata.clear()
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(filename) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
               Mydata.append(i)
            self.fetchData(Mydata)

   def reset_data(self):
       self.var_std_name.set("")
       self.var_department.set("")
       self.var_time.set("")
       self.var_gender.set("")


if __name__ == "__main__":
    root = Tk()
    obj = ImportExport(root)
    root.mainloop()
