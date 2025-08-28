Here’s a cleaned-up and well-structured **README.md** for your project. I improved formatting, badges, consistency, and readability while keeping all important details intact:

---

# 🎭 NDKC Face Recognition Attendance System

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge\&logo=opencv\&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

A comprehensive **facial recognition-based attendance system** for **Notre Dame of Kidapawan College**

📌 Modernizing attendance tracking with AI-powered facial recognition technology

---

### 🚀 Features • 📁 Project Structure • 🛠️ Installation • 📊 Usage

</div>  

---

## 🎯 Overview

The **NDKC Face Recognition Attendance System** is a **Python-based application** that automates student attendance tracking using **facial recognition**.
This system replaces traditional manual attendance methods with a **secure, efficient, and contactless solution**.

---

## ✨ Key Features

* 👤 **Facial Recognition** – Real-time face detection & recognition using **LBPH algorithm**
* 📊 **Attendance Management** – Automated tracking with timestamps & dates
* 👨‍🎓 **Student Database** – Manage comprehensive student details
* 📈 **CSV Export/Import** – Flexible data handling for reports & backup
* 🔐 **Secure Login** – Admin authentication system
* 📷 **Photo Capture** – Dataset generation for training recognition models
* ⏰ **Real-time Clock** – Live time display on dashboard
* 🎯 **User-Friendly GUI** – Intuitive **Tkinter-based interface**

---

## 📁 Project Structure

```
ndkc_face_recognition_system/
├── main.py                 # Main application window
├── face_recognition.py     # Facial recognition functionality
├── student.py              # Student management module
├── train.py                # Model training module
├── attendance.py           # Attendance management
├── login.py                # Admin login system
├── help.py                 # Help & support
├── developer.py            # Developer info
├── requirements.txt        # Python dependencies
├── MAINDATA.xlsm           # Main Excel data storage
├── DATA BACKUP/            # Backup directory
├── LOGS/                   # Attendance logs
│   └── Facial Recognition/
└── New folder/             # Additional storage
```

---

## 🛠️ Technologies Used

* **Python 3.x** – Core language
* **OpenCV** – Computer vision & image processing
* **Tkinter** – GUI development
* **MySQL** – Database management
* **PIL (Pillow)** – Image handling
* **LBPH Algorithm** – Face recognition
* **Haar Cascades** – Face detection
* **CSV Module** – Data export/import

---

## 🚀 Installation

### ✅ Prerequisites

* Python **3.7+**
* MySQL Server
* Webcam

### 📌 Setup Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/shintakino/ndkc_face_recognition_system.git
   cd ndkc_face_recognition_system
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Database**

   ```sql
   CREATE DATABASE face_recognizer;
   USE face_recognizer;

   CREATE TABLE student (
       Dep VARCHAR(255),
       course VARCHAR(255),
       Year VARCHAR(255),
       Semester VARCHAR(255),
       Student_id VARCHAR(255) PRIMARY KEY,
       Name VARCHAR(255),
       Division VARCHAR(255),
       Roll VARCHAR(255),
       Gender VARCHAR(255),
       Dob VARCHAR(255),
       Email VARCHAR(255),
       Phone VARCHAR(255),
       Address VARCHAR(255),
       Professor VARCHAR(255),
       PhotoSample VARCHAR(255)
   );
   ```

4. **Configure Database Connection**
   Update MySQL credentials in all relevant Python files:

   ```python
   conn = mysql.connector.connect(
       host="localhost",
       username="your_username",
       password="your_password",
       database="face_recognizer"
   )
   ```

5. **Run the Application**

   ```bash
   python login.py
   ```

---

## 📊 Usage Guide

1. **Login**

   * Default: `Username: Admin`, `Password: 12345`
   * Secured admin authentication

2. **Student Registration**

   * Add student info (ID, name, department, etc.)
   * Capture **200+ facial samples** for training

3. **Train Model**

   * Processes collected images
   * Generates **classifier.xml** model

4. **Attendance Taking**

   * Recognize faces in real-time
   * Attendance auto-marked & stored in **vaqjammon.csv**

5. **Attendance Management**

   * View & export records
   * Filter by date, department, or student
   * Export to **CSV**

---

## 🎨 System Modules

* **Main Dashboard (`main.py`)** – Central control panel with real-time clock
* **Facial Recognition (`face_recognition.py`)** – Detects & recognizes faces
* **Student Management (`student.py`)** – CRUD operations for student data
* **Training (`train.py`)** – Processes images & trains recognition model
* **Attendance (`attendance.py`)** – Manage & export attendance logs
* **Login (`login.py`)** – Admin authentication
* **Help (`help.py`)** – User guidance
* **Developer Info (`developer.py`)** – Project credits

---

## 🔧 Configuration

* **Database** – Update MySQL credentials in config section
* **File Paths** – Adjust images accordingly:

  ```python
  img = Image.open(r"college_images\smart-attendance.jpg")
  ```
* **Camera Index** – Modify if using external camera:

  ```python
  video_cap = cv2.VideoCapture(1)  # 0 = default webcam
  ```

---

## 📝 Output Files

* `classifier.xml` – Trained recognition model
* `vaqjammon.csv` – Attendance records
* `data/` – Student face dataset
* `LOGS/` – Attendance logs

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch:

   ```bash
   git checkout -b feature/improvement
   ```
3. Commit changes:

   ```bash
   git commit -am "Add new feature"
   ```
4. Push branch:

   ```bash
   git push origin feature/improvement
   ```
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file.

---

## 👨‍💻 Developer Information

**Jerwin D. Jamon**
📧 Email: [didoyjamon18@gmail.com](mailto:didoyjamon18@gmail.com)
💡 Passionate about programming & creating innovative solutions

---

## 🆘 Support

* Check `help.py`
* Email: [didoyjamon18@gmail.com](mailto:didoyjamon18@gmail.com)
* In-system help documentation

---

<div align="center">

🌟 **Future Enhancements**

* 📱 Mobile App Integration
* ☁️ Cloud-based Database
* 📊 Advanced Analytics
* 👥 Multi-face Simultaneous Recognition
* 🏫 Integration with College Systems

🚀 Transform your attendance management with **AI-powered technology**!

💻 Developed with ❤️ for **Notre Dame of Kidapawan College**

</div>  

---

