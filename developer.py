from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer Information")
        
        title_lbl = Label(self.root, text="DEVELOPERS", font=("Arial", 36, "bold"), bg="green", fg="White")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        img_top=Image.open(r"C:\Users\PERSONAL\Code\python web framework\ndkc_face_recognition_system\college_images\sssssssssssssss.jpeg")
        img_top=img_top.resize((1275,630),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1275,height=630) 
        
        # Frame
        main_frame = Frame(f_lbl, bd=2,bg="white")
        main_frame.place(x=830,y=0,width=425,height=520) 
        
        img_top1=Image.open(r"C:\Users\PERSONAL\Code\python web framework\ndkc_face_recognition_system\college_images\1708415386074211.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=225,y=0,width=200,height=200)   
        
        #Developer info
        dev_label = Label(main_frame,text="Hello!I'm Jerwin D.", font = ("times new roman", 13, "bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=5)
        
        dev_label = Label(main_frame,text="And I'm Delving into the ", font = ("times new roman", 13, "bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=30)
        
        dev_label = Label(main_frame,text="world of programming.", font = ("times new roman", 13, "bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=55)
        
        dev_label = Label(main_frame,text="Excited to learn and create!", font = ("times new roman", 13, "bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=80)
        
        img2=Image.open(r"college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2=img2.resize((500,310),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=310) 
        
        
        
if __name__ == "__main__":
    root=Tk()
    objects=Developer(root)
    root.mainloop()
