from tkinter import *
from tkinter import messagebox, ttk
import mysql
from PIL import ImageTk, Image
import mysql.connector

from OriginalMAIN import OriginalMAIN
from Register import Register
#from main import Face_Recognition_System
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
# --------------------------
#from train import Train
#from student import Student
#from attendance import Attendance
import os


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1200x675')
        self.window.resizable(0, 0)
        # self.window.state('zoomed')
        self.window.title('Login Page')


        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_password2=StringVar()
        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('Images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600,bd=2)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",fg='white',bd=5,relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('Images\\GirişOriginal.jpg')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=50, y=120,width=400)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('Images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('Images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('Images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN',command=self.login ,font=("yu gothic ui", 13, "bold"), width=25, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame,command=self.forgetpass,text="Forgot Password ?",font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT, activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)
        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame,text='No account yet?', font=("yu gothic ui", 11, "bold"),relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)


        # ========================================================================
        # ============================Sıgn Up Button==============================
        # ========================================================================
        self.signup_img = ImageTk.PhotoImage(file='Images\\register.png')
        self.signup_button_label = Button(self.lgn_frame,command=self.registerwindow, image=self.signup_img, bg='#98a65d', cursor="hand2",borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)


        # ======== Password icon ================
        self.password_icon = Image.open('Images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='Images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='Images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def registerwindow(self):
        self.new_window=Toplevel(self.window)
        self.app= Register(self.new_window)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')

    def login(self):

        if (self.username_entry.get()=="" or self.password_entry.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.username_entry.get()=="admin" and self.password_entry.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='g9vscqk5',host='localhost',database='users')
            mycursor = conn.cursor()
            mycursor.execute("select * from ınfousers where username=%s and password=%s",(
                self.username_entry.get(),
                self.password_entry.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.window)
                    self.app=OriginalMAIN(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
    def forgetpass(self):
        if self.username_entry.get() == "":
            messagebox.showerror("Error", "Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='g9vscqk5', host='localhost',database='users', )
            mycursor = conn.cursor()
            query = ("select * from ınfousers where username=%s")
            value = (self.username_entry.get(),)
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("Error", "Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                self.root2.resizable(0, 0)

                self.forgetten_frame = Frame(self.root2, bg='#040405', width=400, height=400, bd=2)
                self.forgetten_frame.place(x=0, y=0)

                l=Label(self.forgetten_frame,text="Forget Password",font=("yu gothic ui", 13, "bold"),bg="#040405", fg="white")
                l.place(x=0,y=10,relwidth=1)


                # -------------------fields-------------------
                #label1
                ssq =lb1= Label(self.forgetten_frame,text="Select Security Question:",font=("yu gothic ui", 13, "bold"),bg="#040405", fg="white")
                ssq.place(x=70,y=80)

                #ComboBox1
                self.combo_security = ttk.Combobox(self.forgetten_frame,textvariable=self.var_securityQ,font=("yu gothic ui", 13, "bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2
                sa =lb1= Label(self.forgetten_frame,text="Security Answer:",font=("yu gothic ui", 13, "bold"),bg="#040405", fg="white")
                sa.place(x=70,y=150)

                #entry2
                self.txtpwd=ttk.Entry(self.forgetten_frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2
                new_pwd =lb1= Label(self.forgetten_frame,text="New Password:",font=("yu gothic ui", 13, "bold"),bg="#040405", fg="white")
                new_pwd.place(x=70,y=220)

                #entry2
                self.new_pwd=ttk.Entry(self.forgetten_frame,textvariable=self.var_password2,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)
                ##############################################



                #Creating Button New Password
                resetbtn=Button(self.forgetten_frame,command=self.reset_pass,text="Reset Password",font=("yu gothic ui", 13, "bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                resetbtn.place(x=70,y=300,width=270,height=35)

    def reset_pass(self):
        if self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question!", parent=self.root2)
        elif (self.var_securityA.get() == ""):
            messagebox.showerror("Error", "Please Enter the Answer!", parent=self.root2)
        elif (self.var_password2.get() == ""):
            messagebox.showerror("Error", "Please Enter the New Password!", parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='g9vscqk5', host='localhost',database='users')
            mycursor = conn.cursor()
            query = ("select * from ınfousers where email=%s and securityQ=%s and securityA=%s")
            value = (self.username_entry.get(), self.var_securityQ.get(), self.var_securityA.get())
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please Enter the Correct Answer!", parent=self.root2)
            else:
                query = ("update ınfousers set password=%s where email=%s")
                value = (self.var_password2.get(), self.username_entry.get())
                mycursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Successfully Your password has been rest, Please login with new Password!",parent=self.root2)

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
