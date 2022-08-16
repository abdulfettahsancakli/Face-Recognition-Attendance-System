from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
# from mysqlx.protobuf import val
import cv2
import PyQt5



class FaceDetect:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x675+0+0")
        self.root.title("Student")
        self.root.resizable(0,0)

        # ========variables==========#
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

        # first image
        img = Image.open(r"Images_GUI\banner.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(r"Images_GUI\banner.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"Images_GUI\banner.jpg")
        img2 = img2.resize((550, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=0, y=0, width=550, height=130)


        main_frame = Frame(self.root, bd=2, bg="#888888")
        main_frame.place(x=0, y=0, width=1200, height=675)


         # left label frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Capture Video",font=("times new roman", 12, "bold"))
        left_frame.place(x=0, y=0, width=730, height=550)


        info_label = Label(main_frame,text="Face Detection ",font=("yu gothic ui", 15, "bold"),bg="#888888")
        info_label.place(x=1025,y=10)

        userıd_label = Label(main_frame, text="User ID ", font=("yu gothic ui", 14, "bold"), bg="#888888")
        userıd_label.place(x=750, y=45)
        userıd_entry = ttk.Entry(main_frame,textvariable=self.var_std_id, width=15, font=("times new roman", 14, "bold"))
        userıd_entry.place(x=860,y=50)

        dep_label = Label(main_frame, text="Department ", font=("yu gothic ui", 14, "bold"), bg="#888888")
        dep_label.place(x=730, y=95)
        department_entry = ttk.Entry(main_frame,textvariable=self.var_department,width=15, font=("times new roman", 14, "bold"))
        department_entry.place(x=860, y=100)

        name_label = Label(main_frame, text="Student Name ", font=("yu gothic ui", 14, "bold"), bg="#888888")
        name_label.place(x=730, y=145)
        name_entry = ttk.Entry(main_frame,textvariable=self.var_std_name ,width=15, font=("times new roman", 14, "bold"))
        name_entry.place(x=860, y=150)

        course_label = Label(main_frame, text="Course ", font=("yu gothic ui", 14, "bold"),bg="#888888")
        course_label.place(x=730, y=195)
        course_entry = ttk.Entry(main_frame,textvariable=self.var_department, width=15, font=("times new roman", 14, "bold"))
        course_entry.place(x=860, y=200)


        dtct = Image.open(r"Images_GUI\det1.jpg")
        dtct = dtct.resize((150, 100), Image.ANTIALIAS)
        self.photodtct = ImageTk.PhotoImage(dtct)

        b1 = Button(main_frame,command=self.generate_dataset, image=self.photodtct, cursor="hand2")
        b1.place(x=860, y=250, width=150, height=100)

        b1_1 = Button(main_frame, text="Detect the Face", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b1_1.place(x=860, y=350, width=150, height=40)


        # =================TABLE FRAME =============#

        table_frame = Frame(main_frame, bd=2, bg="white",relief=RIDGE)
        table_frame.place(x=0, y=425, width=1200, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
        "Faculty", "Department", "Year", "Semester", "Class", "Student ID", "Student Name", "Date of Birth",
        "Mobile Number", "Gender"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

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
        self.student_table.column("Class", width=3, )
        self.student_table.column("Student ID", width=30)
        self.student_table.column("Student Name", width=40)
        self.student_table.column("Date of Birth", width=40)
        self.student_table.column("Mobile Number", width=40)
        self.student_table.column("Gender", width=40)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

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



        # =====Generate Dataset or Take Photo Samples==

    def generate_dataset(self):
         if self.var_department.get() == "" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
             messagebox.showerror("Error", "All fields are required", parent=self.root)
         else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="g9vscqk5",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from unistudents")
                result = my_cursor.fetchall()
                print(result)
                id = 0
                for x in result:
                    id = id + 1
                my_cursor.execute(
                    "update unistudents set Faculty=%s,Department=%s, Year=%s, Semester=%s,Class=%s, StudentName=%s, Dateofbirth=%s,MobileNumber=%s,Gender=%s where Studentid=%s",
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
                        self.var_std_id.get() == id + 1,

                    ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except:
                pass
            ### Load Predifiend data on face frontals from opencv

                face_classifier = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    face_cropped = img[y:y + h, x:x + w]
                    return face_cropped

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame),(500, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                    cv2.imwrite(file_name_path, face)
                    #cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating data set completed")


if __name__ == "__main__":
    root = Tk()
    obj = FaceDetect(root)
    root.mainloop()
