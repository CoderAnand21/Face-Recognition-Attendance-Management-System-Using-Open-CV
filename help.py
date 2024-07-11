from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as tsmg
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")
        
        

     
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="Blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"College_image\bg.webp")
        img_top=img_top.resize((1530,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530 ,height=750)

        title_lbl=Label(f_lbl,text="Email : hepldesk@gmail.com",font=("times new roman",35,"bold"),bg="white",fg="Blue")
        title_lbl.place(x=490,y=310)

        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()


