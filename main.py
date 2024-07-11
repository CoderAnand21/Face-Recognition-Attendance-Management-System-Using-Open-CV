from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from student import student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from help import Help



class Face_Recognization_system:
#============Main==================  
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognization System")
        
         
        
        #bg image
        img3=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\bg.webp")
        img3=img3.resize((1535,900),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1535,height=795)

        title_lbl=Label(bg_img,text="Advance Faciometry",font=("Arial Rounded MT Bold",35,"bold"),fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        
        #Student Button 
        img4=Image.open(r"C:\Users\anand\OneDrive\Desktop\My folder\new\College_image\student.webp")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white",bd=5)
        b1_1.place(x=200,y=300,width=220,height=40)
         
        
        #Face Detector
        img5=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\Second_2.webp")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white",bd=5)
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
        #Attendance 
        img6=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\go2.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance ",cursor="hand2",command=self.attendence,font=("Arial Rounded MT Bold",15,"bold"),bg="darkblue",fg="white", bd=5)
        b1_1.place(x=800,y=300,width=220,height=40)
        
        
         # Help Desk Button 
        img7=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\helpdesk.jpeg")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help)
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help,font=("times new roman",15,"bold"),bg="darkblue",fg="white",bd=5)
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        # Train Face Button 
        img8=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\Attendence.jpeg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white",bd=5)
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        # Photos  
        img9=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\1000_F_502160894_Y9200cB3peg6HpPjujhriBZAzPmwteh8.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white",bd=5)
        b1_1.place(x=500,y=580,width=220,height=40)
        
        
         # Devloper Button 
        img10=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\developer.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white",bd=5)
        b1_1.place(x=800,y=580,width=220,height=40)
        
        
         # Exit Button
        img11=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\exit.jpeg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit Button",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white",bd=5)
        b1_1.place(x=1100,y=580,width=220,height=40)
        
        
    def open_img(self):
        os.startfile("data")  
        
    #=====EXIT ======
    def iExit(self):
           self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this window",parent=self.root)
           if self.iExit > 0:
                  self.root.destroy()
           else:
                  return
        
        
        #========Function Button 1=======
        
    def student_details(self):
     self.new_window=Toplevel(self.root)
     self.app=student(self.new_window)
     
      #========Function Button 2=======
        
    def train_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Train(self.new_window)
     
      #========Function Button 3=======
        
    def face_data(self):
     self.new_window=Toplevel(self.root)
     self.app=Face_Recognition(self.new_window)
     
      #========Function Button 4=======
        
    def attendence(self):
     self.new_window=Toplevel(self.root)
     self.app=Attendence(self.new_window)          
        
      #========Function Button 4=======
        
    def help(self):
     self.new_window=Toplevel(self.root)
     self.app=Help(self.new_window)          
                
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_system(root)
    root.mainloop()
