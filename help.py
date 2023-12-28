from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        title_lbl = Label(self.root, text="Help Desk", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        img_top=Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top=img_top.resize((1275,630),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1275,height=630) 
        
        dev_label = Label(f_lbl,text="Email:joshuajaynarvaza@gmail.com", font = ("times new roman", 20, "bold"),bg="white",fg="blue")
        dev_label.place(x=420,y=180)
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    objects=Help(root)
    root.mainloop()
