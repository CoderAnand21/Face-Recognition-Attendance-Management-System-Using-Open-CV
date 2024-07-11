from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as tsmg
import mysql.connector
import os
import numpy as np
import cv2
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Advance Feciometry")
        
        

        title_label=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),fg="green",bg="white")
        title_label.place(x=0,y=0,width=1530,height=45)   
          
        #bg image
        img3=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\facial-recognition-collage-concept_23-2150038883.webp")
        img3=img3.resize((1535,900),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1535,height=795)

        #========Second Image=============
        img_bottom=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\Second_2.webp")
        img_bottom=img_bottom.resize((500,500),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=500,y=55,width=500 ,height=500)


        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",font=("times new raoman",18,"bold"),fg="white",bg="darkblue",command=self.face_recog,)
        b1_1.place(x=0,y=458,width=500,height=40)
    #=================Attendence==================
    def mark_attendence(self,i,r,n,d):
        with open(r"Present.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))     
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present") 


#=============face recognition=======================

    def face_recog(self):
        def draw_boundray(img,classifier,ScaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,ScaleFactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                

                conn=mysql.connector.connect(host="localhost",username="root",password="anand2018",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confidence > 77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord
        def recognizer(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\classifier.xml")   

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognizer(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
    
    