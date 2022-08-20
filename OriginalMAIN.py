from tkinter import ttk
from tkinter import *
from PIL import ImageTk,Image
from cv2 import cv2

from AttendanceRecord import AttendanceRecord
from DataList import DataList
from FaceDetect import FaceDetect
from ImportExport import ImportExport
from StudentEnroll import StudentEnroll
from TrainingImages import TrainingImages
from Recognition import Recognition
#from MaskDetect import MaskDetect

class OriginalMAIN:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x675+0+0")
        self.root.title("Face_Recognition_System")
        self.root.resizable(0, 0)
        #self.root.state('zoomed')



        # #Background Image
        bg=Image.open(r"Images\MainWallpaper.png")
        self.photobg= ImageTk.PhotoImage(bg)

        bg_img=Label(self.root, image=self.photobg)
        bg_img.place(x=0, y=0)

        #  first image
        img = Image.open(r"Images\Face-Recognition-Based-Attendance-System-1024x311.jpg")
        img = img.resize((1200, 180), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(bg_img, image=self.photoimg)
        f_lbl.place(x=0, y=0)



        # ========================================================================
        # ============================Student Button==============================
        # ========================================================================
        newstd = Image.open(r"Images\NewStudentEnrollment.png")
        newstd = newstd.resize((200, 100), Image.ANTIALIAS)
        self.photonewstd = ImageTk.PhotoImage(newstd)

        b1 = Button(bg_img,command=self.student_pannels, image=self.photonewstd, cursor="hand2",bd=2,bg="black")
        b1.place(x=0, y=533, width=170, height=100)

        b1_1 = Button(bg_img, text="Student Enrollment", cursor="hand2",font=("yu gothic ui", 13, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=632, width=170, height=40)

        # ========================================================================
        # ============================Face Detector===============================
        # ========================================================================
        detect = Image.open(r"Images\det1.jpg")
        detect = detect.resize((200, 100), Image.ANTIALIAS)
        self.photodetect = ImageTk.PhotoImage(detect)

        b1 = Button(bg_img,command=self.face_detect,image=self.photodetect, cursor="hand2",bd=2,bg="black")
        b1.place(x=170, y=533, width=170, height=100)

        b1_1 = Button(bg_img,command=self.face_detect,text="Face Detector", cursor="hand2",font=("yu gothic ui", 13, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=170, y=632, width=170, height=40)

        # ========================================================================
        # ============================Train Data =================================
        # ========================================================================
        train = Image.open(r"Images\Train2.jpg")
        train = train.resize((200, 100), Image.ANTIALIAS)
        self.phototrain = ImageTk.PhotoImage(train)

        b1 = Button(bg_img,command=self.train_pannels, image=self.phototrain, cursor="hand2", bd=2, bg="black")
        b1.place(x=340, y=533, width=170, height=100)

        b1_1 = Button(bg_img, text="Train Dataset", cursor="hand2",font=("yu gothic ui", 13, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=340, y=632, width=170, height=40)

        # ========================================================================
        # ============================Face Recognition============================
        # ========================================================================
        rcg = Image.open(r"Images\KlasikFace.jpeg")
        rcg = rcg.resize((200, 100), Image.ANTIALIAS)
        self.photorcg = ImageTk.PhotoImage(rcg)

        b1 = Button(bg_img,command=self.face_data, image=self.photorcg, cursor="hand2", bd=2, bg="black")
        b1.place(x=510, y=533, width=170, height=100)

        b1_1 = Button(bg_img, text="Face Recognition", cursor="hand2",font=("yu gothic ui", 13, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=510, y=632, width=170, height=40)
        
        # ========================================================================
        # ============================Mask Detection=============================
        # ========================================================================
        mask = Image.open(r"Images\Search.jpg")
        mask = mask.resize((200, 100), Image.ANTIALIAS)
        self.photomask = ImageTk.PhotoImage(mask)

        b1 = Button(bg_img,command=self.data_list,image=self.photomask, cursor="hand2", bd=2, bg="black")
        b1.place(x=680, y=533, width=170, height=100)

        b1_1 = Button(bg_img,text="Search Student", cursor="hand2", font=("yu gothic ui", 13, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=680, y=632, width=170, height=40)
        
        # ========================================================================
        # ============================Attendance=============================
        # ========================================================================
        
        att = Image.open(r"Images\att.jpg")
        att = att.resize((200, 100), Image.ANTIALIAS)
        self.photoatt = ImageTk.PhotoImage(att)
        
        b1 = Button(bg_img,command=self.attendance_data, image=self.photoatt, cursor="hand2", bd=2, bg="black")
        b1.place(x=850, y=533, width=170, height=100)
        
        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",font=("yu gothic ui", 13, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=850, y=632, width=170, height=40)

        # ========================================================================
        # ============================Import/Export===============================
        # ========================================================================

        ie = Image.open(r"Images\ImportExport.png")
        ie = ie.resize((180, 100), Image.ANTIALIAS)
        self.photoie = ImageTk.PhotoImage(ie)

        b1 = Button(bg_img,command=self.importexport, image=self.photoie, cursor="hand2", bd=2, bg="black")
        b1.place(x=1020, y=533, width=180, height=100)

        b1_1 = Button(bg_img, text="Import / Export", cursor="hand2", font=("yu gothic ui", 13, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=1020, y=632, width=180, height=40)

        # ========================================================================
        # ============================Functions=============================
        # ========================================================================

    def student_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = StudentEnroll(self.new_window)

    def train_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = TrainingImages(self.new_window)

    def face_detect(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceDetect(self.new_window)

    def data_list(self):
        self.new_window = Toplevel(self.root)
        self.app = DataList(self.new_window)

    # def maskdetect(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = MaskDetect(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = AttendanceRecord(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Recognition(self.new_window)

    def importexport(self):
        self.new_window= Toplevel(self.root)
        self.app= ImportExport(self.new_window)


if __name__ == "__main__":
        root=Tk()
        obj=OriginalMAIN(root)
        root.mainloop()
