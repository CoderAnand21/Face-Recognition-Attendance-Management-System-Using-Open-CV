from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as tsmg
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Advance Faciometry")
       
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="Blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\download.jpeg")
        img_top=img_top.resize((1530,750),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbll=Label(self.root,image=self.photoimg_top)
        f_lbll.place(x=0,y=55,width=1530 ,height=750)

        #======FRAME Ajay Kumar =========
        main_frame=LabelFrame(f_lbll,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=1140,y=310,width=380,height=425)
        
        img_top1=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\images\Ajay Kumar .jpg")
        img_top1=img_top1.resize((380,380),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=0,y=0,width=380 ,height=380)
        
        # Developer Info
        current_label=Label(main_frame,text="Ajay Kumar",font="lucida 25 bold",bg="dark blue",fg="white")
        current_label.place(x=0,y=380,width=380)
        
         # Anand=================
        main_frame3=LabelFrame(f_lbll,bd=2,relief=RIDGE,bg="white")
        main_frame3.place(x=380,y=310,width=380,height=425)

        img_top3=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\images\Anand.jpg")
        img_top3=img_top3.resize((380,380),Image.Resampling.LANCZOS)
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)

        f_lbl=Label(main_frame3,image=self.photoimg_top3)
        f_lbl.place(x=0,y=0,width=380 ,height=380)
         # Developer Info
        current_label=Label(main_frame3,text="Anand",font="lucida 25 bold",bg="dark blue",fg="white")
        current_label.place(x=0,y=380,width=380)
        
        #===========Harshit Tiwari 
        main_frame2=LabelFrame(f_lbll,bd=2,relief=RIDGE,bg="white")
        main_frame2.place(x=0,y=0,width=380,height=425)
        
        img_top2=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\images\Harshit Tiwari.jpg")
        img_top2=img_top2.resize((380,380),Image.Resampling.LANCZOS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_frame2,image=self.photoimg_top2)
        f_lbl.place(x=0,y=0,width=380 ,height=380)
        # Developer Info
        current_label=Label(main_frame2,text="Harshit Tiwari",font="lucida 25 bold",bg="blue",fg="white")
        current_label.place(x=0,y=380,width=380)

       
        # Anshika Yadav======================
        main_frame4=LabelFrame(f_lbll,bd=2,relief=RIDGE,bg="white")
        main_frame4.place(x=760,y=0,width=380,height=425)

        img_top4=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\images\Anshika Yadav.jpg")
        img_top4=img_top4.resize((380,380),Image.Resampling.LANCZOS)
        self.photoimg_top4=ImageTk.PhotoImage(img_top4)

        f_lbl=Label(main_frame4,image=self.photoimg_top4)
        f_lbl.place(x=0,y=0,width=380 ,height=380)
        # Developer Info
        current_label=Label(main_frame4,text="Anshika Yadav",font="lucida 25 bold",bg="blue",fg="white")
        current_label.place(x=0,y=380,width=380)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()


