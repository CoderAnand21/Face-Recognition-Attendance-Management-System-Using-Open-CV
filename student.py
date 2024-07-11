from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class student:
 #============Main==================  
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Advance Faciometry")
        
        #============variables===================
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        #bg image
        img3=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\bgf.jpg")
        img3=img3.resize((1530,900),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=900)

        title_lbl=Label(bg_img,text="Student Panel",font=("Arial Rounded MT Bold",35,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1470,height=705)
        
        # Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("Arial Rounded MT Bold",15,"bold"))
        Left_frame.place(x=0,y=0,width=780,height=700)
        
        img_left=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\first.jpg")
        img_left=img_left.resize((750,200),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=15,y=0,width=750,height=200)
        
        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("Arial Rounded MT Bold",15,"bold"))
        current_course_frame.place(x=15,y=200,width=750,height=125)
        
        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="White")
        dep_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","Civil","Mechanical","Electrical",)
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        #Course
        
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="White")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly")
        course_combo["values"]=("Select Course","AIML","DS","IT","CS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="White")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly")
        year_combo["values"]=("Select Year","First Year","Second Year","Third Year","Fourth Year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="White")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly")
        semester_combo["values"]=(" ","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("Arial Rounded MT Bold",15,"bold"))
        class_student_frame.place(x=15,y=330,width=750,height=340)
        
        
        #studentId:
        studentid_label=Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="White")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        #student name
        studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="White")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        #class Division
        class_division_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="White")
        class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=20)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #Roll No:
        Roll_No_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="White")
        Roll_No_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        Roll_No_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        Roll_No_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        #Gender
        Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="White")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="White")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        #Email:
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="White")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        #Phone No.
        Phone_no_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="White")
        Phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        Phone_No_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        Phone_No_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        
        
        #Adress
        Address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="White")
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        Address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
        #Teacher Name
        teacher_name_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="White")
        teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #Radio Buttons
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=6,column=0)
        
        #Radio BUtton2
        
        radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=6,column=1)
        
        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=225,width=745,height=55)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",bd=5)
        save_btn.grid(row=0,column=0,)
        
        #update Button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",bd=5)
        update_btn.grid(row=0,column=1,)
        
        #Delete
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",bd=5)
        delete_btn.grid(row=0,column=2,)
        
        #Reset
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",bd=5)
        reset_btn.grid(row=0,column=3,)
        
        
        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=265,width=745,height=43)
        
        # Add  photo sample
        take_photo_btn=Button(btn_frame,text="Add Photo Sample",command=self.genrate_dataset,width=73,font=("times new roman",13,"bold"),bg="blue",fg="white",bd=5)
        take_photo_btn.grid(row=0,column=0,)
        
        
        
        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Arial Rounded MT Bold",15,"bold"))
        Right_frame.place(x=790,y=0,width=670,height=700)
        
        
        img_right=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\Photos.jpg")
        img_right=img_right.resize((650,200),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=0,width=650,height=200)
        
        
        # ===================Search System===================
        
        viewstudent_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="white",text="View Student Details",font="comicsansms 12 bold")
        viewstudent_frame.place(x=10,y=205,width=650,height=60)

        Search_label=Label(viewstudent_frame,text="Details",bg="blue",font="comicsansms 20 bold",fg="white",width=40)
        Search_label.place(x=0,y=0)
        
        #===============Table Frame=============
        
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=275,width=650,height=390)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")

        self.student_table.heading("gender",text="Gender")

        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
      #=====================Function Decleration fro adding data ===================== 
    def add_data(self):
      if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()==""or self.var_std_name.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
          try:
            conn=mysql.connector.connect(host="localhost",username="root",password="anand2018",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                              ))
            conn.commit()
            self.fetch_data()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
          except Exception as es:
              messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
              
  #=========================Fetch Data=================
    def fetch_data(self):                      
      conn=mysql.connector.connect(host="localhost",username="root",password="anand2018",database="face_recognizer")
      my_cursor=conn.cursor()
      my_cursor.execute("Select * from student")
      data=my_cursor.fetchall()
      
      if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
      conn.close()
      
      
  #==============get cursor=====================For updating the database information
    def get_cursor(self,event=""): 
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)   #for table content we use item()
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        
        self.var_year.set(data[2]),
             
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
   #============Update Function==================
    def update_data(self):
      if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

      else:
         try:
            update=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
            if update > 0:
                  conn=mysql.connector.connect(host="localhost",username="root",password="anand2018",database="face_recognizer")
                  my_cursor=conn.cursor()
                  my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Name=%s,PhotoSample=%s where Student_id=%s",(
                                    
                                    
                                    
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_std_id.get()==id+1
                                    
                                    
                                    
                                                                                                                                             ))

            else:
              if not update:
                  return  
            messagebox.showinfo("Success","Student details successfully updates",parent=self.root)
            conn.commit()
            self.fetch_data()
            conn.close()
         except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)  
       
   # Delete Function Button
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Data Delete Page","Do you want to delete this student data",parent=self.root)
                if delete>0:
                  conn=mysql.connector.connect(host="localhost",username="root",password="anand2018",database="face_recognizer")
                  my_cursor=conn.cursor()
                  sql="delete from student where Student_id=%s"
                  val=(self.var_std_id.get(),)
                  my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student detials",parent=self.root)
            except Exception as es:
                  messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)      
    #============Reset Button================
    def reset_data(self):
      self.var_dep.set("Select Department"),
      self.var_course.set("Select Course"),
      self.var_year.set("Select Year"),
      self.var_semester.set("Select Semester"),
      self.var_std_id.set(""),
      self.var_std_name.set(""),
      self.var_div.set("Select Division"),
      self.var_roll.set(""),
      self.var_gender.set("Male"),
      self.var_dob.set(""),
      self.var_email.set(""),
      self.var_phone.set(""),
      self.var_address.set(""),
      self.var_teacher.set(""),
      self.var_radio1.set("")
    #=================Genrate Data set and take PHOTo Samples ====================   
    def genrate_dataset(self):
      if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)

      else:
          try:
            conn=mysql.connector.connect(host="localhost",username="root",password="anand2018",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
                id+=1
            my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Name=%s,PhotoSample=%s where Student_id=%s",(
                                    
                                    
                                    
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_std_id.get()==id+1
                                                                                                                                ))
                                    
                                    
                                                                                                                                        
            
                
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
            #==============================Load Predefine data on face frontal from opencv=====================

            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#C:\\Users\\PC\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
            right_eye_classifier=cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")
            left_eye_classifier=cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
            smile_classifier=cv2.CascadeClassifier("haarcascade_smile.xml")
            def face_cropped(img):
              
              print(os.path.isfile("haarcascade_frontalface_default.xml"))
             
              print("Welcome 1")
              gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #BGRColor image into grey image
              faces=face_classifier.detectMultiScale(gray,1.3,5)
             
              #1.3 means Scaling Factor
               #Minimum Neighbour = 5
              for (x,y,w,h) in faces: #for making Triangle
                face_cropped=img[y:y+h,x:x+w]
                print("Welcom 2")  
                return face_cropped
              
              
               
                #====For opening the Camera=======
            cap=cv2.VideoCapture(0)  # 0 means bydefault laptop camera will open
            img_id=0
            while True:
                ret,my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                  img_id+=1
                  face=cv2.resize(face_cropped(my_frame),(500,500))
                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                  file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                  cv2.imwrite(file_name_path,face)
                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,500,0),2)
                  cv2.imshow("Cropped Face",face)

                if cv2.waitKey(1)==13 or int(img_id)==100:
                    break
            print("Welcome 5")
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data sets completed!!!")
          except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
          print("Welcome 6") 
 
      
      
      
      
if __name__ == "__main__":
  root=Tk()
  obj= student(root)
  root.mainloop()
