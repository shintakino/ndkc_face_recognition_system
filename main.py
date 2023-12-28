from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import  Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        #Fist Image
        img=Image.open(r"college_images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)       

        #Second Image
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130) 
        
        #Third Image
        img2=Image.open(r"college_images\u.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130) 

        #bg Image
        img3=Image.open(r"college_images\bg1.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710) 
        
        title_lbl = Label(bg_img, text="    FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        #============================Time=========================
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)
            
        lbl = Label(title_lbl, font = ("times new roman", 14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=(-5),width=110, height=50)
        time()
        
        #Student Button
        img4=Image.open(r"college_images\student.jpg")
        img4=img4.resize((170,170),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=70,width=170,height=170)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details  ,cursor="hand2",font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100,y=230,width=170,height=40)
        
        #Detect Face Button
        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((170,170),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img, image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=70,width=170,height=170)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=400,y=230,width=170,height=40)
        
        #Attendance Face Button
        img6=Image.open(r"college_images\smart-attendance.jpg")
        img6=img6.resize((170,170),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=70,width=170,height=170)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=700,y=230,width=170,height=40)
        
        #Help Face Button
        img7=Image.open(r"college_images\help.jpg")
        img7=img7.resize((170,170),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=70,width=170,height=170)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1000,y=230,width=170,height=40)
        
        #Train Face Button
        img8=Image.open(r"college_images\Train.jpg")
        img8=img8.resize((170,170),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=330,width=170,height=170)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100,y=490,width=170,height=40)
        
        #Photos Face Button
        img9=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img9=img9.resize((170,170),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=330,width=170,height=170)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=400,y=490,width=170,height=40)
        
        #Developer Face Button
        img10=Image.open(r"college_images\DEV1.jpg")
        img10=img10.resize((170,170),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img, image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=330,width=170,height=170)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=700,y=490,width=170,height=40)
        
        #Exit Face Button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((170,170),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img, image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=330,width=170,height=170)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1000,y=490,width=170,height=40)
        
        #==========Functions Buttons=============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
    def open_img(self):
        os.startfile("data") 
        
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition", "Are you sure exit this project",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
        
        
        
        
        
        


if __name__ == "__main__":
    root=Tk()
    objects=Face_Recognition_System(root)
    root.mainloop()
