from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox as tsmg
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



 
mydata=[]      # all data come from csv data after importing
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Advance Faciometry")
       
        

        #=====================Variables for upadting it into entry fills=========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()

 #bg image
        img3=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\bgf.jpg")
        img3=img3.resize((1530,900),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=900)

        
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=60,width=1530,height=720)    

        title_lbl=Label(bg_img,text="Advance Faciometry",font=("Arial Rounded MT Bold",35,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        mainframe=Frame(bg_img,borderwidth=2,bg="white")
        mainframe.place(x=5,y=60,width=1520,height=720)
        
        #Left Label frame
        Left_frame=LabelFrame(mainframe,bd=2,relief=RIDGE,bg="white",text="Student Attendence Details",font="comicsansms 12 bold")
        Left_frame.place(x=0,y=0,width=780,height=715)
        


        img4=Image.open(r"C:\Users\anand\OneDrive\Desktop\Face Recogition attendence system\College_image\1000_F_427206216_XXRMtmBkPV8Vgdpej4ltRLSlGUMBoGdC.jpg")
        img4=img4.resize((775,250),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(Left_frame,image=self.photoimg4)
        f_lbl.place(x=5,y=0,width=770,height=250)
        
        left_inside_frame=Frame(Left_frame,borderwidth=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=5,y=250,width=770,height=440)

        #LAbels and entry
        #attendence
        attendenceIDName_label=Label(left_inside_frame,text="Attendence ID:",bg="white",font="comicsansms 13 bold")
        attendenceIDName_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendenceIDName_entry=Entry(left_inside_frame,font="comicsansms 13 bold",width=20,relief=RIDGE,bd=2,textvariable=self.var_atten_id)
        attendenceIDName_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Roll
        rollIDName_label=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansms 13 bold")
        rollIDName_label.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=Entry(left_inside_frame,font="comicsansms 13 bold",width=20,relief=RIDGE,bd=2,textvariable=self.var_atten_roll)
        atten_roll.grid(row=0,column=3,pady=8)


        #name
        namelabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansms 13 bold")
        namelabel.grid(row=1,column=0)

        atten_name  =Entry(left_inside_frame,font="comicsansms 13 bold",width=20,relief=RIDGE,bd=2,textvariable=self.var_atten_name)
        atten_name .grid(row=1,column=1,pady=8)
        #Department
        depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansms 13 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=Entry(left_inside_frame,font="comicsansms 13 bold",width=20,relief=RIDGE,bd=2,textvariable=self.var_atten_dep)
        atten_dep.grid(row=1,column=3,pady=8)

        #time

        timelabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansms 13 bold")
        timelabel.grid(row=2,column=0)

        atten_time=Entry(left_inside_frame,font="comicsansms 13 bold",width=20,relief=RIDGE,bd=2,textvariable=self.var_atten_time)
        atten_time.grid(row=2,column=1,pady=8)
         #Date
        datelabel=Label(left_inside_frame,text="Date:",bg="white",font="comicsansms 13 bold")
        datelabel.grid(row=2,column=2)

        atten_date=Entry(left_inside_frame,font="comicsansms 13 bold",width=20,relief=RIDGE,bd=2,textvariable=self.var_atten_date)
        atten_date.grid(row=2,column=3,pady=8)
        
        #attendence
        attendenceLabel=Label(left_inside_frame,text="Attendence Status:",bg="white",font="comicsansms 13 bold")
        attendenceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,state="readonly",width=18,font="comicsansms 13 bold",textvariable=self.var_atten_attendence)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,pady=8)
        
        # Button frame
        button_frame=LabelFrame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=200,width=765,height=62)

        save_btn=Button(button_frame,bg="blue",cursor="hand2",fg="white",text="Import csv",command=self.importCsv,width=31,font="comicsansms 10 bold",relief=RIDGE,height=3)
        save_btn.grid(row=0,column=0)

        update_btn=Button(button_frame,bg="blue",cursor="hand2",fg="white",text="Export csv",width=31,font="comicsansms 10 bold",relief=RIDGE,command=self.exportCsv,height=3)
        update_btn.grid(row=0,column=1)

        reset_btn=Button(button_frame,bg="blue",cursor="hand2",fg="white",text="Reset",width=30,font="comicsansms 10 bold",relief=RIDGE,command=self.reset_data,height=3)
        reset_btn.grid(row=0,column=3)
        
        
        #right label frame
        Right_frame=LabelFrame(mainframe,bd=2,relief=RIDGE,bg="white",text="Attendence Details",font="comicsansms 12 bold")
        Right_frame.place(x=780,y=2,width=745,height=713)
        
        table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=0,width=735,height=690)


        #===============Scroll Bar table=======================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendenceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)


        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")
        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.column("id",width=110)
        self.AttendenceReportTable.column("roll",width=110)
        self.AttendenceReportTable.column("name",width=110)
        self.AttendenceReportTable.column("department",width=110)
        self.AttendenceReportTable.column("time",width=110)
        self.AttendenceReportTable.column("date",width=110)
        self.AttendenceReportTable.column("attendence",width=110)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)


        #=================Working on import csv============
          #====================== fetch data=============

    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
    #============for showing data in the table of attendence importing data from Aviral.csv===================

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

       #==============Working on Export CSV=========================
       #=====export CSV======
    def exportCsv(self):
        try:
            if len(mydata)<1:
                tsmg.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                tsmg.showinfo("Data Export","Tour data exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
            tsmg.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")

if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()

