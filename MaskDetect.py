from tkinter import Tk
import cv2

class MaskDetect:
   def __init__(self, root):
     self.root = root
     self.root.geometry("1200x675+0+0")
     self.root.title("Mask")





face_cascade = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
mouth_cascade = cv2.CascadeClassifier("Haarcascades/haarcascade_mcs_mouth.xml")
org = (30,30)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
weared_mask = "Thank you for wearing MASK"
not_weared_mask = "Please wear MASK to defeat CORONA"
cap = cv2.VideoCapture(0)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Frame doesn't open")

    gray_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image, 1.1, 7)

    if(len(faces) == 0):
        cv2.putText(frame, "No face found", org, fontFace, fontScale, (255,255,255), 2)
    else:
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
            roi_gray = gray_image[y:y+h, x:x+w]

            mouth = mouth_cascade.detectMultiScale(roi_gray,1.4, 15)
            i = 0
            if(len(mouth) == 0):
                #speak('Thanks wearing')
                #engine.runAndWait()
                cv2.putText(frame, weared_mask, org, fontFace,fontScale, (0,255,0), 2, cv2.LINE_AA)


            else:
                #speak('Please wear mask')
                cv2.putText(frame, not_weared_mask, org, fontFace, fontScale, (0,0,255),4, cv2.LINE_AA)

                for mx, my, mw, mh in mouth:
                    if i == 0:
                        i+=1
                        cv2.rectangle(frame, (mx+x,my+y),
                                      (mx+x+mw, my+y+mh), (0,0,255),3)
                    else:
                        pass

    cv2.imshow("Mask Detection",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = MaskDetect(root)
    root.mainloop()
