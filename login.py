from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk    
from tkinter import messagebox as tsmg
import mysql.connector
from student import student


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        

        
        img3=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\photo-1605379399642-870262d3d051.jpeg")
        img3=img3.resize((1550,800),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbl_bg=Label(self.root,image=self.photoimg3)
        lbl_bg.place(x=0,y=0,width=1550,height=800)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\icon5.png")
        img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimg1,bg="black"  ,borderwidth=0)
        lblimg1.place(x=730,y=165,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=90)


        #Label
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)


        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)


        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #=============Icon image================
        img2=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\icon7.png")
        img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(image=self.photoimg2,bg="black"  ,borderwidth=0)
        lblimg2.place(x=655,y=326,width=25,height=25)

        img4=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\pass.png")
        img4.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(image=self.photoimg4,bg="black"  ,borderwidth=0)
        lblimg4.place(x=655,y=395,width=25,height=25)


        #=====Login Button=======
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg='white',bg='red',activebackground="red",activeforeground='white',cursor="hand2",command=self.login)
        loginbtn.place(x=130,y=300,width=70,height=30)

         #====Register Button=========
        loginbtn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg='white',borderwidth=0,bg='black',activebackground="black",activeforeground='white',cursor="hand2",command=self.register_window)
        loginbtn.place(x=10,y=340,width=160)
         
         #==========forget Button========
        Forgetbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg='white',bg='black',borderwidth=0,activebackground="black",activeforeground='white',cursor="hand2")
        Forgetbtn.place(x=5,y=360,width=160)
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            tsmg.showerror("Error","all Field required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get=="ashu":
            tsmg.showinfo("Success","Welcome to the code with aviral channel pls subscribe and share")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="anand2018",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where  email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()

                                                                                        ))
            
            row=my_cursor.fetchone()
            if row == None:
                tsmg.showerror("Error","Invalid Username and Password")
            else:
                open_main=tsmg.askyesno("Yes or No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)

                    self.app=student(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    
    def reset_pass(self):
        if self.combo_security_Q.get()=='select':
            tsmg.showerror("Error","select security question",parent=self.root2)
        elif self.txt_security.get()=="":
            tsmg.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            tsmg.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="anand2018",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                tsmg.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                tsmg.showinfo("Info","Your password has been reset,Please enter new Password",parent=self.root2)

                self.root2.destroy()
            





     #===========forget pass window============

    def forget_password_window(self):
        if self.txtuser.get()=="":
            tsmg.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="anand2018",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email= %s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                tsmg.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                self.root2.configure(bg='white')

            l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="green",bg="white")
            l.place(x=0,y=10,relwidth=1)
            security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
            security_Q.place(x=50,y=80)
            
            self.combo_security_Q=ttk.Combobox(self.root2,font="lucida 12 bold",state="readonly")
            self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
            self.combo_security_Q.current(0)
            self.combo_security_Q.place(x=50,y=110,width=250)



            security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
            security_A.place(x=50,y=150)


            self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
            self.txt_security.place(x=50,y=180,width=250)

            new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
            new_password.place(x=50,y=220)


            self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
            self.txt_newpass.place(x=50,y=250,width=250)


            btn=Button(self.root2,bg="green",cursor="hand2",fg="white",text="Reset",width=15,font="comicsansms 10 bold",relief=RIDGE,bd=2,command=self.reset_pass)
            btn.place(x=100,y=290)
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("15500x800+0+0")


        #===============Variable============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securitQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #======BG image==========
        imgs1=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\1000_F_334263770_j7ivhTD3ZYez4q7YIgPR9lO4UP5jFJrp.jpg")
        imgs1=imgs1.resize((1550,800),Image.Resampling.LANCZOS)
        self.photoimgs1=ImageTk.PhotoImage(imgs1)

        lbl_bg=Label(self.root,image=self.photoimgs1)
        lbl_bg.place(x=0,y=0,width=1550,height=800)

        img3=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\ne.jpg")
        img3=img3.resize((1550,800),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbl_bg=Label(self.root,image=self.photoimg3)
        lbl_bg.place(x=50,y=100,width=470,height=550)


        #==== Main Frame===

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)


        get_str=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        get_str.place(x=20,y=20)



        #===========label abd entry===

          #   row 1=====
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)


        fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_fname)
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        l_name.place(x=370,y=100)


        self.txt_lname=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_lname)
        self.txt_lname.place(x=370,y=130,width=250)
      
        #  row 2===============

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)


        self.txt_contact=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_contact)
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)


        self.txt_email=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_email)
        self.txt_email.place(x=370,y=200,width=250)

        #======= Row 3=============
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,font="lucida 12 bold",state="readonly",textvariable=self.var_securitQ)
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)



        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_A.place(x=370,y=240)


        self.txt_security=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_securityA)
        self.txt_security.place(x=370,y=270,width=250)


        #=========Row r4===============
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        pswd.place(x=50,y=310)


        self.txt_pswd=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_pass)
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        confirm_pswd.place(x=370,y=310)


        self.txt_confirm_pswd=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_confpass)
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
      
        #=== Check Button=========
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,text="I agree the terms & condition",font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0,variable=self.var_check)
        checkbtn.place(x=50,y=380)
        
        # buttons==========
        img=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\jo1.png")
        img=img.resize((200,40),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        b1=Button(frame,image=self.photoimg,command=self.register_data,bg="blue",cursor="hand2",borderwidth=0,background="white",activebackground='white')
        b1.place(x=10,y=420,width=300)

        img1=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\jo.png")
        img1=img1.resize((200,40),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(frame,image=self.photoimg1,bg="blue",cursor="hand2",borderwidth=0,background="white",activebackground='white',command=self.return_login)
        b1.place(x=330,y=420,width=300)
    #=====================Function Decleration==================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securitQ.get()=="Select":
            tsmg.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            tsmg.showerror("Error","Password and Confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            tsmg.showerror("Error","Please agree our term and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="anand2018",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                tsmg.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_fname.get(),
                                                                                                            self.var_lname.get(),
                                                                                                            self.var_contact.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_securitQ.get(),
                                                                                                            self.var_securityA.get(),
                                                                                                            self.var_pass.get()
                                                                                                            
                                                                                                              ))
            conn.commit()
            
            conn.close()
            tsmg.showinfo("Success","Student details has been added Successfully",parent=self.root)
    

           
        
    def return_login(self):
        self.root.destroy()   
if __name__=="__main__":
    main()