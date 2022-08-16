import os
import time
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar, Style
import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import PyQt5
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
engine.setProperty('voice', voices[0].id)  # 1 is for female voice and 0 is for male voice

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

class TrainingImages:
   def __init__(self, root):
     self.root = root
     self.root.geometry("1200x675+0+0")
     self.root.title("Training Images")

     header = Image.open(r"Images_GUI\Training2.jpg")
     header = header.resize((1200,200), Image.ANTIALIAS)
     self.photoheader = ImageTk.PhotoImage(header)
     f_lbl = Label(self.root, image=self.photoheader)
     f_lbl.place(x=0, y=0)

     train = Image.open(r"Images_GUI\Train34.jpg")
     train = train.resize((1200, 475), Image.ANTIALIAS)
     self.phototrain = ImageTk.PhotoImage(train)

     f_lbl = Label(self.root, image=self.phototrain)
     f_lbl.place(x=0, y=200)

     trn = Image.open(r"Images_GUI\TrainButton.jpg")
     trn = trn.resize((210, 220), Image.ANTIALIAS)
     self.phototrn = ImageTk.PhotoImage(trn)

     b1 = Button(self.root, image=self.phototrn, cursor="hand2")
     b1.place(x=500, y=300)

     b1_1 = Button(self.root, text="Train the Images",command=self.train_classifier,cursor="hand2",font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
     b1_1.place(x=500, y=525,width=215)



   def train_classifier(self):
     data_dir = ("data")
     # get the path of all the files in the folder
     path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

     faces = []
     #create empty face list
     ids = []
     #create empty ID list
     for image in path: # now looping through all the image paths and loading the Ids and the images
       img = Image.open(image).convert("L")  # loading the image and converting it to gray scale
       imageNp = np.array(img, 'uint8') #Now we are converting the PIL image into numpy array
       id = int(os.path.split(image)[1].split('.')[1]) #getting the Id from the image

       faces.append(imageNp)  # extract the face from the training image sample
       ids.append(id)
       cv2.imshow("Training", imageNp)
       cv2.waitKey(1) == 13

     ids = np.array(ids)
     #####TRAIN THE CLASSIFIER AND SAVE ######
     clf = cv2.face.LBPHFaceRecognizer_create()
     clf.train(faces, ids) #Train the model using the faces and ids
     clf.write("classifier.xml")  #Save the model into classifier.xml
     print("Total faces: ", len(faces)) #Checking how many faces are there
     print("Total labels: ", len(ids)) # Checking how many ids are there
     cv2.destroyAllWindows()
     messagebox.showinfo("Result", "Training dataset completed")
     speak_va("Training dataset completed")





if __name__ == "__main__":
    root = Tk()
    obj = TrainingImages(root)
    root.mainloop()
