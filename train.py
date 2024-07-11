from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox as tsmg
import mysql.connector
import os
import numpy as np
import cv2
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        img_bottom=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\facial-recognition-software_52683-104208.webp")
        img_bottom=img_bottom.resize((1535,790),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=0,width=1535 ,height=790)
    
        
        

        #==========Button=========
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=420,y=725,width=700,height=60)



    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            #for calculating grid of gray image we use numpy array
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            # C:\Users\PC\Desktop\new\data\user.3.1.jpg
            #  0                            1
            #                                0   1 2


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==10  #for closing window after 13 sec
        ids=np.array(ids)
       # ======================== Train classifier ANd Save================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        print("True")
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        tsmg.showinfo("Result","Training dataset completed!")
if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()