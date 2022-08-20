from tkinter import *
from tkinter import messagebox, ttk

import mysql
from PIL import ImageTk, Image
import mysql.connector


#from main import Face_Recognition_System


class Register:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Register Page')
        # ========================================================================
        # ============================Variables===================================
        # ========================================================================
        self.var_username=StringVar()
        self.var_password=StringVar()
        self.var_password2=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()


        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('Images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # ====== Register Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=1100, height=580)
        self.lgn_frame.place(x=150, y=100)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME TO REGISTER PAGE "
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",fg='white',bd=5,relief=FLAT)
        self.heading.place(x=50, y=30, width=500, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('Images\\YGiriş.jpg')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=55, y=120)

        # ========================================================================
        # ============ Register Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('Images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=700, y=10)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Register", bg="#040405", fg="white",font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=750, y=120)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=170)

        self.username_entry = Entry(self.lgn_frame,textvariable=self.var_username, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=200, width=190)

        self.username_line = Canvas(self.lgn_frame, width=220, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=230)
        # ===== Username icon =========
        self.username_icon = Image.open('Images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=200)


        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('Images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=650, y=450)
        self.login = Button(self.lgn_button_label, text='REGISTER',command=self.register ,font=("yu gothic ui", 13, "bold"), width=25, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)
        # ========================================================================



        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=250)

        self.password_entry = Entry(self.lgn_frame,textvariable=self.var_password, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=580, y=280, width=190)

        self.password_line = Canvas(self.lgn_frame, width=220, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=310)

        # ======== Password icon ================
        self.password_icon = Image.open('Images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=280)
        # ========================================================================
        # ============================Confirm password====================================
        # ========================================================================
        self.password_label2 = Label(self.lgn_frame, text="Confirm Password", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
        self.password_label2.place(x=550, y=330)
        #
        self.password_entry2 = Entry(self.lgn_frame,textvariable=self.var_password2, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry2.place(x=580, y=360, width=190)
        #
        self.password_line2 = Canvas(self.lgn_frame, width=220, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line2.place(x=550, y=390)
        # ========================================================================
        # ============================Confirm Password icon====================================
        self.password_icon = Image.open('Images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=360)


        # ========================================================================
        # ============================Email ====================================
        # ========================================================================
        self.email_label = Label(self.lgn_frame, text="Email", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
        self.email_label.place(x=800, y=170)

        self.email_entry = Entry(self.lgn_frame,textvariable=self.var_email ,highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",font=("yu gothic ui ", 12, "bold"))
        self.email_entry.place(x=825, y=200, width=190)

        self.email_line = Canvas(self.lgn_frame, width=220, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.email_line.place(x=800, y=230)

        self.email = Image.open('Images\\shield .png')
        photo = ImageTk.PhotoImage(self.email)
        self.email_label = Label(self.lgn_frame, image=photo)
        self.email_label.image = photo
        self.email_label.place(x=800, y=201,height=20,width=20)


        # ========================================================================
        # ============================Security Question===========================
        # ========================================================================
        self.security_label = Label(self.lgn_frame, text="Security Question", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
        self.security_label.place(x=800, y=250)

        # self.security_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69", font=("yu gothic ui ", 12, "bold"))
        # self.security_entry.place(x=820, y=280, width=190)

        self.combo_security = ttk.Combobox(self.lgn_frame,textvariable=self.var_securityQ,font=("yu gothic ui ", 12, "bold"),state="readonly")
        self.combo_security["values"] = ("Select", "Your Date of Birth", "Your Nick Name", "Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=825, y=280, width=190)


        self.security_line = Canvas(self.lgn_frame, width=220, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.security_line.place(x=800, y=310)

        self.security = Image.open('Images\\shield .png')
        photo = ImageTk.PhotoImage(self.security)
        self.security_label = Label(self.lgn_frame, image=photo)
        self.security_label.image = photo
        self.security_label.place(x=800, y=282, height=20, width=20)

        # ========================================================================
        # ============================Security Answer=============================
        # ========================================================================
        self.securityA_label = Label(self.lgn_frame, text="Security Answer", bg="#040405", fg="white",font=("yu gothic ui", 13, "bold"))
        self.securityA_label.place(x=800, y=330)

        self.securityA_entry = Entry(self.lgn_frame,textvariable=self.var_securityA ,highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",font=("yu gothic ui ", 12, "bold"))
        self.securityA_entry.place(x=830, y=360, width=190)

        self.securityA_line = Canvas(self.lgn_frame, width=220, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.securityA_line.place(x=800, y=390)

        self.securityA = Image.open('Images\\shield .png')
        photo = ImageTk.PhotoImage(self.securityA)
        self.securityA_label = Label(self.lgn_frame, image=photo)
        self.securityA_label.image = photo
        self.securityA_label.place(x=800, y=360, height=20, width=20)

        # ========================================================================
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='Images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='Images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=760, y=280)

        self.show_button2 = Button(self.lgn_frame, image=self.show_image, command=self.show2, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button2.place(x=760, y=360)

    def show2(self):
        self.hide_button2 = Button(self.lgn_frame, image=self.hide_image, command=self.hide2, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button2.place(x=760, y=360)
        self.password_entry2.config(show='')


    def hide2(self):
        self.show_button2 = Button(self.lgn_frame, image=self.show_image, command=self.show2, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button2.place(x=760, y=360)
        self.password_entry2.config(show='*')

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=760, y=280)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=760, y=280)
        self.password_entry.config(show='*')



    def register(self):
        if (self.var_username.get()=="" or self.var_password.get()=="" or self.var_password2.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA.get()==""):
            messagebox.showerror("Error", "All Field Required!")
        elif (self.var_password.get() != self.var_password2.get()):
            messagebox.showerror("Error", "Please Enter Password & Confirm Password are Same!")
        else:
            try:
                conn = mysql.connector.connect(username='root', password='g9vscqk5', host='localhost', database='users')
                mycursor = conn.cursor()
                query = ("select * from ınfousers where email=%s")
                value = (self.var_email.get(),)
                mycursor.execute(query, value)
                row = mycursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exist,please try another email")
                else:
                    mycursor.execute("insert into ınfousers values(%s,%s,%s,%s,%s,%s)",(
                    self.var_username.get(),
                    self.var_password.get(),
                    self.var_password2.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),

                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.window)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.window)

def page():
    window = Tk()
    Register(window)
    window.mainloop()


if __name__ == '__main__':
    page()
