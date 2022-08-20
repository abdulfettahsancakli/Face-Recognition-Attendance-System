from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import PyQt5
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[0].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()


class StudentEnroll:
   def __init__(self, root):
     self.root = root
     self.root.geometry("1200x675+0+0")
     self.root.title("New Student Enroll")

     self.var_faculty = StringVar()
     self.var_department = StringVar()
     self.var_year = StringVar()
     self.var_semester = StringVar()
     self.var_class = StringVar()
     self.var_std_id = StringVar()
     self.var_std_name = StringVar()
     self.var_dob = StringVar()
     self.var_mob = StringVar()
     self.var_gender = StringVar()

     img2 = Image.open(r"Images\NEW STUDENT ENROLLMENT.png")
     img2 = img2.resize((1200,180), Image.ANTIALIAS)
     self.photoimg2 = ImageTk.PhotoImage(img2)

     f_lbl = Label(self.root, image=self.photoimg2)
     f_lbl.place(x=0, y=0)


     # ========================================================================
     # ============================MAIN FRAME===============================
     # ========================================================================
     main_frame = Frame(self.root, bd=2, bg="#888888" )
     main_frame.place(x=0, y=180, width=350, height=675)

     main_frame2 = Frame(self.root, bd=2, bg="#888888")
     main_frame2.place(x=350, y=180, width=350, height=675)

     main_frame3 = Frame(self.root, bd=2, bg="#888888")
     main_frame3.place(x=700, y=180, width=500, height=675)

     # ============================Faculty Image===============================
     faculty = Image.open(r"Images\Faculty-Information.jpg")
     faculty = faculty.resize((400, 82), Image.ANTIALIAS)
     self.photofaculty = ImageTk.PhotoImage(faculty)

     f_lbl = Label(main_frame, image=self.photofaculty)
     f_lbl.place(x=0,y=-5,width=400)
     # =====================================================================

     # ============================Student Information Image===============================
     stdinfo = Image.open(r"Images\StudentInformation.png")
     stdinfo = stdinfo.resize((400, 80), Image.ANTIALIAS)
     self.photostdinfo = ImageTk.PhotoImage(stdinfo)

     f_lbl = Label(main_frame2, image=self.photostdinfo)
     f_lbl.place(x=0, y=-5, width=400)
     # =====================================================================


     # =========================Faculty Combobox============================================
     fac_label = Label(main_frame, text="Faculty : ", font=("times new roman", 15, "bold"),bg="#888888")
     fac_label.place(x=40, y=100)
     # ========================================================================
     fac_combo = ttk.Combobox(main_frame, textvariable=self.var_faculty ,font=("times new roman", 12, "bold"), state="readonly", width=20)
     fac_combo["values"] = ("Select Faculty", "Engineering", "Education", "Law", "Communication")
     fac_combo.current(0)
     fac_combo.place(x=130, y=102)

     # =========================Department Combobox============================================
     dep_label = Label(main_frame, text="Department : ", font=("times new roman",15, "bold"),bg="#888888")
     dep_label.place(x=0,y=165)
     # ========================================================================
     dep_combo = ttk.Combobox(main_frame,textvariable=self.var_department, font=("times new roman", 12, "bold"),state="readonly", width=20)
     dep_combo["values"] = ("Select Department", "Computer", "IT", "Mechanic")
     dep_combo.current(0)
     dep_combo.place(x=130,y=170)
     # ========================================================================

     # =========================Year Combobox============================================
     year_label = Label(main_frame, text="  Year : ", font=("times new roman", 15, "bold"),bg="#888888")
     year_label.place(x=50, y=240)
     # ========================================================================
     year_combo = ttk.Combobox(main_frame, textvariable=self.var_year ,font=("times new roman", 12, "bold"), state="readonly", width=20)
     year_combo["values"] = ("Select Year", "2018", "2019", "2020","2021","2022")
     year_combo.current(0)
     year_combo.place(x=130, y=240)
     # ========================================================================
     #
     # =========================Semester Combobox============================================
     semester_label = Label(main_frame, text="Semester : ", font=("times new roman", 15, "bold"), bg="#888888")
     semester_label.place(x=20, y=305)
     # ========================================================================
     semester_combo = ttk.Combobox(main_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly", width=20)
     semester_combo["values"] = ("Select Semester", "Fall", "Spring")
     semester_combo.current(0)
     semester_combo.place(x=130, y=310)
     # ========================================================================

     # =========================Class Combobox============================================
     class_label = Label(main_frame, text="Class : ", font=("times new roman", 15, "bold"), bg="#888888")
     class_label.place(x=50, y=375)
     # ========================================================================
     dep_combo = ttk.Combobox(main_frame, textvariable=self.var_class ,font=("times new roman", 12, "bold"), state="readonly", width=20)
     dep_combo["values"] = ("Select Instruction", "1", "2")
     dep_combo.current(0)
     dep_combo.place(x=130, y=380)
     # ========================================================================

     # =========================Student ID Entry================================
     studentID_label = Label(main_frame2, text="Student ID : ", font=("times new roman", 15, "bold"),bg="#888888")
     studentID_label.place(x=25,y=98)

     studentID_entry = ttk.Entry(main_frame2, textvariable=self.var_std_id,width=20,font=("times new roman", 12, "bold"))
     studentID_entry.place(x=140,y=100)
     # ========================================================================

    # =========================Student Name Entry================================
     studentName_label = Label(main_frame2, text="Student Name : ", font=("times new roman", 15, "bold"),bg="#888888")
     studentName_label.place(x=0,y=165)

     studentName_entry = ttk.Entry(main_frame2, textvariable=self.var_std_name,width=20,font=("times new roman", 12, "bold"))
     studentName_entry.place(x=140,y=168)
     # ========================================================================


     # =========================Date Of Birth================================
     studentdob_label = Label(main_frame2, text="Date of Birth :  ", font=("times new roman", 15, "bold"),bg="#888888")
     studentdob_label.place(x=10, y=235)

     studentdob_entry = ttk.Entry(main_frame2, textvariable=self.var_dob,width=20, font=("times new roman", 12, "bold"))
     studentdob_entry.place(x=140, y=235)
     # ========================================================================

     # =========================Mobile Number =================================
     studentMobileNo_label = Label(main_frame2, text="Mobile-No :  ", font=("times new roman", 15, "bold"), bg="#888888")
     studentMobileNo_label.place(x=20, y=305)

     studentMobileNo_entry = ttk.Entry(main_frame2, textvariable=self.var_mob ,width=20, font=("times new roman", 12, "bold"))
     studentMobileNo_entry.place(x=140, y=305)
     # ========================================================================

     # =========================Gender Combobox============================================
     gender_label = Label(main_frame2, text="Gender : ", font=("times new roman", 15, "bold"), bg="#888888")
     gender_label.place(x=30, y=375)
     # ========================================================================
     gender_combo = ttk.Combobox(main_frame2, textvariable=self.var_gender ,font=("times new roman", 12, "bold"), state="readonly", width=20)
     gender_combo["values"] = ("Select Gender", "Male", "Female")
     gender_combo.current(0)
     gender_combo.place(x=140, y=380)
     # ========================================================================

     # =================TABLE FRAME =============#
     table_frame = Frame(main_frame3, bd=2, bg="white", relief=RIDGE)
     table_frame.place(x=0, y=23, width=495, height=250)

     FacultyChange_label = Label(main_frame3, text="CHOOSE A STUDENT WHO UPDATE STUDENT INFORMATIONS ", font=("times new roman", 12, "bold"), bg="#888888")
     FacultyChange_label.place(x=0, y=0)

     scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
     scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

     self.student_table = ttk.Treeview(table_frame, column=("Faculty", "Department","Year","Semester","Class", "Student ID", "Student Name", "Date of Birth","Mobile Number","Gender"),
     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

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



     self.student_table.column("Faculty", width=50)
     self.student_table.column("Department", width=50)
     self.student_table.column("Year", width=40)
     self.student_table.column("Semester", width=40)
     self.student_table.column("Class", width=3,)
     self.student_table.column("Student ID", width=30)
     self.student_table.column("Student Name", width=40)
     self.student_table.column("Date of Birth", width=40)
     self.student_table.column("Mobile Number", width=40)
     self.student_table.column("Gender", width=40)

     self.student_table.pack(fill=BOTH, expand=1)
     self.student_table.bind("<ButtonRelease>", self.get_cursor)
     self.fetch_data()

     # =========================Buttons =================================
     # =========================Save =================================
     save = Image.open(r"Images\Save.webp")
     save = save.resize((80,80), Image.ANTIALIAS)
     self.photosave = ImageTk.PhotoImage(save)

     b1 = Button(main_frame3,command=self.add_data,image=self.photosave, cursor="hand2")
     b1.place(x=20, y=290, width=80, height=80)

     # =========================Update =================================

     updt = Image.open(r"Images\Update.webp")
     updt = updt.resize((80, 80), Image.ANTIALIAS)
     self.photoupdt = ImageTk.PhotoImage(updt)

     b1 = Button(main_frame3, command=self.update_data, image=self.photoupdt, cursor="hand2")
     b1.place(x=150, y=290, width=80, height=80)

     # =========================Delete =================================
     dlt = Image.open(r"Images\Delete2.webp")
     dlt = dlt.resize((80, 80), Image.ANTIALIAS)
     self.photodlt = ImageTk.PhotoImage(dlt)

     b1 = Button(main_frame3, command=self.delete_data, image=self.photodlt, cursor="hand2")
     b1.place(x=280, y=290, width=80, height=80)

     # =========================Reset =================================
     rst = Image.open(r"Images\reset.jpg")
     rst = rst.resize((80, 80), Image.ANTIALIAS)
     self.photorst = ImageTk.PhotoImage(rst)

     b1 = Button(main_frame3, command=self.reset_data, image=self.photorst, cursor="hand2")
     b1.place(x=410, y=290, width=80, height=80)


   def add_data(self):
     if self.var_std_name.get() == "" or self.var_std_id.get() == "":
       messagebox.showerror("Error", "All fields are required", parent=self.root)
     else:
       try:
         conn = mysql.connector.connect(host="localhost", username="root", password="g9vscqk5", database="face_recognizer")
         my_cursor = conn.cursor()
         my_cursor.execute("insert into unistudents values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
           self.var_faculty.get(),
           self.var_department.get(),
           self.var_year.get(),
           self.var_semester.get(),
           self.var_class.get(),
           self.var_std_id.get(),
           self.var_std_name.get(),
           self.var_dob.get(),
           self.var_mob.get(),
           self.var_gender.get()

         ))
         conn.commit()
         self.fetch_data()
         conn.close()
         speak_va('Student Details has been added successfully.')
         messagebox.showinfo("Success", "Student added ", parent=self.root)
       except Exception as es:
         messagebox.showerror("Error", f"Due To{str(es)}", parent=self.root)

       # ==============================Delete Function=========================================
   def delete_data(self):
           if self.var_faculty.get() == "":
               messagebox.showerror("Error", "Student Id Must be Required!", parent=self.root)
           else:
               try:
                   delete = messagebox.askyesno("Delete", "Do you want to Delete?", parent=self.root)
                   if delete > 0:
                       conn = mysql.connector.connect(username='root', password='g9vscqk5', host='localhost',
                                                      database='face_recognizer')
                       mycursor = conn.cursor()
                       sql = "delete from unistudents where Faculty=%s"
                       val = (self.var_faculty.get(),)
                       mycursor.execute(sql, val)
                   else:
                       if not delete:
                           return

                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Delete", "Successfully Deleted!", parent=self.root)
               except Exception as es:
                   messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

   def update_data(self):
       if self.var_department.get() == "Select Department" :
           messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
       else:
           try:
               Update = messagebox.askyesno("Update", "Do you want to Update this Student Details!", parent=self.root)
               if Update > 0:
                   conn = mysql.connector.connect(username='root', password='g9vscqk5', host='localhost',
                                                  database='face_recognizer')
                   mycursor = conn.cursor()
                   mycursor.execute(
                       "update unistudents set Faculty=%s,Department=%s,Year=%s,Semester=%s,Class=%s,Studentname=%s,Dateofbirth=%s,MobileNumber=%s,Gender=%s where Studentid=%s",
                       (
                           self.var_faculty.get(),
                           self.var_department.get(),
                           self.var_year.get(),
                           self.var_semester.get(),
                           self.var_class.get(),
                           self.var_std_name.get(),
                           self.var_dob.get(),
                           self.var_mob.get(),
                           self.var_gender.get(),
                           self.var_std_id.get(),
                       ))
               else:
                   if not Update:
                       return
               messagebox.showinfo("Success", "Successfully Updated!", parent=self.root)
               conn.commit()
               self.fetch_data()
               conn.close()
           except Exception as es:
               messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

   def reset_data(self):
       self.var_faculty.set("Select Faculty"),
       self.var_department.set("Select Department"),
       self.var_year.set("Select Year"),
       self.var_semester.set("Select Semester"),
       self.var_class.set("Select Class"),
       self.var_std_id.set(""),
       self.var_std_name.set(""),
       self.var_dob.set(""),
       self.var_mob.set(""),
       self.var_gender.set("Select Semester")



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

   def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_faculty.set(data[0]),
        self.var_department.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_class.set(data[4]),
        self.var_std_id.set(data[5]),
        self.var_std_name.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_mob.set(data[8]),
        self.var_gender.set(data[9])



if __name__ == "__main__":
    root = Tk()
    obj = StudentEnroll(root)
    root.mainloop()
