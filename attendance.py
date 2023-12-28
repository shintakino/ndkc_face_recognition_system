from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        #================== Variables ===========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        #Fist Image
        img=Image.open(r"college_images\smart-attendance.jpg")
        img=img.resize((650,170),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=650,height=170)       

        #Second Image
        img1=Image.open(r"college_images\iStock-182059956_18390_t12.jpg")
        img1=img1.resize((650,170),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=650,y=0,width=650,height=170)
        
        #bg Image
        img3=Image.open(r"college_images\bg1.jpg")
        img3=img3.resize((1530,740),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=170,width=1530,height=740)
        
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 20, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1250,height=520)
        
        #Left Label Frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="attendance Attendance Details", font = ("times new roman", 11, "bold"))
        Left_frame.place(x=15,y=5,width=605,height=500)
        
        img_left=Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((595,110),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=595,height=110)
        
        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=115,width=600,height=330)
        
        # Label and Entry
        # Attendance ID
        attendanceId_label = Label(left_inside_frame,text="AttendanceID:", font = ("times new roman", 11, "bold"),bg="white")
        attendanceId_label.grid(row=0,column=0)
        
        attendanceID_entry =ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id, font = ("times new roman", 11, "bold"))
        attendanceID_entry.grid(row=0,column=1,pady=3)
        
        #Roll
        rollLabel = Label(left_inside_frame,text="Roll:", font = ("times new roman", 11, "bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=6)
        
        atten_roll =ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll, font = ("times new roman", 11, "bold"))
        atten_roll.grid(row=0,column=3,pady=6)
        
        #Name
        nameLabel = Label(left_inside_frame,text="Name:", font = ("times new roman", 11, "bold"),bg="white")
        nameLabel.grid(row=1,column=0)
        
        atten_name =ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name, font = ("times new roman", 11, "bold"))
        atten_name.grid(row=1,column=1,pady=6)
        
        #Department
        depLabel = Label(left_inside_frame,text="Department:", font = ("times new roman", 11, "bold"),bg="white")
        depLabel.grid(row=1,column=2)
        
        atten_dep =ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep, font = ("times new roman", 11, "bold"))
        atten_dep.grid(row=1,column=3,pady=6)
        
        #Time
        timeLabel = Label(left_inside_frame,text="Time:", font = ("times new roman", 11, "bold"),bg="white")
        timeLabel.grid(row=2,column=0)
        
        atten_time = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time, font = ("times new roman", 11, "bold"))
        atten_time.grid(row=2,column=1,pady=6)
        
        #Date
        dateLabel = Label(left_inside_frame,text="Date:", font = ("times new roman", 11, "bold"),bg="white")
        dateLabel.grid(row=2,column=2)
        
        atten_date = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date, font = ("times new roman", 11, "bold"))
        atten_date.grid(row=2,column=3,pady=6)
        
        #attendance status  
        attendanceLabel = Label(left_inside_frame,text="Attendance Status:", font = ("times new roman", 11, "bold"),bg="white")
        attendanceLabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_attendance,font = ("times new roman", 11, "bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=6)
        self.atten_status.current(0)
        
        #Bbuttons Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=230,width=590,height=35)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=16, font = ("times new roman", 11, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=15, font = ("times new roman", 11, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update",width=15, font = ("times new roman", 11, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16, font = ("times new roman", 11, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        #Right Label Frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details", font = ("times new roman", 11, "bold"))
        Right_frame.place(x=625,y=5,width=605,height=500)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=590,height=360)
        
        #================Scroll Bar===============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
        #================Fetch Data =================
    def fetch_Data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #Import CSV        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File", "*.csv"), ("ALL Files", "*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_Data(mydata)
            
    #Export CSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),parent=self.root)
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {es}", parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

        
        
        
if __name__ == "__main__":
    root=Tk()
    objects=Attendance(root)
    root.mainloop()