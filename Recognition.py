import csv
from datetime import datetime, time
from math import ceil
from tkinter import *
from tkinter import ttk
import time
import pandas as pd
from PIL import Image, ImageTk
from tkinter import messagebox
import keyboard
from time import sleep
import mysql.connector
# from mysqlx.protobuf import val
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


class Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x675+0+0")
        self.root.title("Face Recognition")
        #self.root.resizable(0,0)

        img = Image.open(r"Images\Recognition.webp")
        img = img.resize((1200,150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1200, height=150)

        ie = Image.open(r"Images\FaceRecognitionButton.webp")
        ie = ie.resize((180, 100), Image.ANTIALIAS)
        self.photoie = ImageTk.PhotoImage(ie)

        b1_1 = Button(self.root, text="Face Recognition",image=self.photoie, cursor="hand2",command=self.face_recognition,font=("times new roman", 18, "bold"), bg="red", fg="white")
        b1_1.place(x=280, y=380)


        b1_1 = Button(self.root, text="Face Recognition", cursor="hand2", font=("yu gothic ui", 13, "bold"), bg="darkblue",fg="white")
        b1_1.place(x=280, y=485,width=186 )



        # b1_2 = Button(self.root, text="Face Recognition", cursor="hand2", command=self.snapshot,
        #               font=("times new roman", 18, "bold"), bg="red", fg="white")
        # b1_2.place(x=0, y=350, width=200, height=40)


        img2 = Image.open(r"Images\Recoognition2.webp")
        img2 = img2.resize((1200,150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=0, y=525, width=1200, height=150)

        # img3 = Image.open(r"Images_GUI\Recoognition2.webp")
        # img3 = img3.resize((200, 200), Image.ANTIALIAS)
        # self.photoimg3 = ImageTk.PhotoImage(img3)
        #
        # f_lbl = Label(self.root, image=self.photoimg3)
        # f_lbl.place(x=0, y=525, width=200, height=200)
        table_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=705, y=150, width=495, height=375)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          column=("StudentName", "Department", "Date","Time","Status"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("StudentName", text="Student Name")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Date", text="Date")
        self.student_table.heading("Time",text="Time")
        self.student_table.heading("Status", text="Status")

        self.student_table["show"] = "headings"

        self.student_table.column("StudentName", width=98)
        self.student_table.column("Department", width=98)
        self.student_table.column("Date", width=98)
        self.student_table.column("Time",width=98)
        self.student_table.column("Status", width=98)


        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>")
        self.fetch_data()

    def devamsızlık(self,d,n):
        kayıt=0
        self.var_name=n
        self.var_department=d
        self.var_status="Present"
        # self.var_roll=n

        now = datetime.now()
        self.var_d1 = now.strftime("%d/%m/%Y")
        self.var_dtString = now.strftime("%H:%M")

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="g9vscqk5",database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT IGNORE into attendance values(%s,%s,%s,%s,%s)",(
                self.var_name,
                self.var_department,
                self.var_d1,
                self.var_dtString,
                self.var_status,
            ))

            my_cursor.execute("select * from attendance")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"Due To{str(es)}", parent=self.root)
            kayıt=1
        return kayıt


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

    def mark_attendance(self, n, r, d):
        with open("attendance2.csv", "r+", newline="\n") as f:
                myDatalist = f.readlines()
                name_list = []

                for line in myDatalist:
                    entry = line.split((","))
                    name_list.append(entry[0])
                    if ((n not in name_list)) and ((r not in name_list)) and ((d not in name_list)):
                        now = datetime.now()
                        d1 = now.strftime("%d/%m/%Y")
                        dtString = now.strftime("%H:%M:%S")
                        f.writelines(f"\n{n}, {r}, {d},{dtString},{d1}, Present")




    def face_recognition(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                featuers = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                coord = []

                for (x, y, w, h) in featuers:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                    confidence = int((100 * (1 - predict / 300)))
                    #the algorithm is already trained
                    # find the image that matches the input image
                    # we just need to compare two histograms and return the image with the closest histogram
                    # We can use euclidean distance
                    # the algorithm output is the ID from the image with the closest histogram.
                    # The algorithm should also return the calculated distance, which can be used as a ‘confidence’ measurement.

                    conn = mysql.connector.connect(host="localhost", username="root", password="g9vscqk5",
                                                   database="face_recognizer")
                    cursor = conn.cursor()

                    cursor.execute("select StudentName from unistudents where Studentid=" + str(id))
                    n = cursor.fetchone()
                    n = '' + ''.join(n)

                    cursor.execute("select Studentid from unistudents where Studentid=" + str(id))
                    r = cursor.fetchone()
                    r = '' + ''.join(r)

                    cursor.execute("select Department from unistudents where Studentid=" + str(id))
                    d = cursor.fetchone()
                    d = '' + ''.join(d)

                    # If the value from our formula is over 77,
                    # we display the information of that person from the database on the screen.
                    if confidence > 77:
                        cv2.putText(img, f"Student ID:{r}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223),2)
                        cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                        cv2.putText(img, f"Department:{d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                        #cv2.putText(img, str(ceil(confidence)) + "%", (x, y - 20), cv2.FONT_HERSHEY_DUPLEX, .5 # (0, 255, 0))
                        self.devamsızlık(d, n)




                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                    coord = [x, y, w, h]

                return coord

            # ==========
        def recognize(img, clf, faceCascade):
                coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
                return img
        #The features required in our face recognition class are our haarcascade face classifier and our classifier.xml file.
        faceCascade = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        videoCap.set(3,700)
        videoCap.set(4,370)
        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1)==13 :

                speak_va("Attendance has been taken succesfully")
                messagebox.showinfo("Success","Student Attendance Successfully")

                break
        videoCap.release()
        cv2.destroyAllWindows()



    # df_state = pd.read_csv("C:/Users/FET-PC/Desktop/Face/attendance2.csv")
    # DF_RM_DUP = df_state.drop_duplicates(keep=False)
    # DF_RM_DUP.to_csv('attendance.csv', index=False)


if __name__ == "__main__":
    root = Tk()
    obj = Recognition(root)
    root.mainloop()
