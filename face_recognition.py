from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        
        title_lbl = Label(self.root, text="        FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        # 1st Image
        img_top=Image.open(r"college_images\face_detector1.jpg")
        img_top=img_top.resize((590,610),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=590,height=610) 
        
        # 2nd Image
        img_bottom=Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom=img_bottom.resize((740,610),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=550,y=55,width=740,height=610) 
        
        # Button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=270,y=540,width=200,height=30)
        
                #================Attendance================
    def mark_attendance(self, i, r, n, d):
        with open("shintakino.csv", "a+", newline="\n") as f:
            f.seek(0)  # Move the file pointer to the beginning
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

        
        
        # ===========Face Recognition ======================
    
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))
                
                conn = mysql.connector.connect(host="localhost", username="root", password="shintakino", database="face_recognizer")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                
                if confidence > 77:
                    cv2.putText(img, f"Roll: {i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Student ID: {r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 225), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            
            return img
        
        def recognize(img, clf, faceCascade):
            return draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
            
            key = cv2.waitKey(1)
            if key == 13:  # Press Enter key to close camera
                break
            elif key == ord('q'):  # Press 'Q' key to break the loop and close camera
                break

        video_cap.release()
        cv2.destroyAllWindows()

        
        
        
        
if __name__ == "__main__":
    root=Tk()
    objects=Face_recognition(root)
    root.mainloop()