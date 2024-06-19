from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from main import Face_Recognition_System

OUTPUT_PATH_LOGIN = Path(__file__).parent
ASSETS_PATH_LOGIN = OUTPUT_PATH_LOGIN / Path(r"C:\Users\didoy\Downloads\drive-download-20240222T025407Z-001\login\build\assets")

def relative_to_assets_login(path: str) -> Path:
    return ASSETS_PATH_LOGIN / Path(path)

def login(event=None):
    entered_username = entry_2.get()
    entered_password = entry_1.get()

    if entered_username == "Admin" and entered_password == "12345":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        window_login.destroy()  # Close the login window

        # Open the main window after successful login
        root = Tk()
        app = Face_Recognition_System(root)
        root.mainloop()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Login Window
window_login = Tk()
window_login.title("Log In")
window_login.geometry("663x360")
window_login.configure(bg="#FDFDFD")

canvas_login = Canvas(
    window_login,
    bg="#FDFDFD",
    height=360,
    width=663,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas_login.place(x=0, y=0)

button_image_1 = PhotoImage(
    file=relative_to_assets_login("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_1.place(
    x=303.0,
    y=228.0,
    width=253.0,
    height=84.0
)

canvas_login.create_text(
    97.0,
    228.0,
    anchor="nw",
    text="PASSWORD",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets_login("entry_1.png"))
entry_bg_1 = canvas_login.create_image(
    133.0,
    199.0,
    image=entry_image_1
)

# Use show='*' to display asterisks for password
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    show='*'
)
entry_1.place(
    x=30.0,
    y=180.0,
    width=206.0,
    height=36.0
)

canvas_login.create_text(
    97.0,
    141.0,
    anchor="nw",
    text="USERNAME",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets_login("entry_2.png"))
entry_bg_2 = canvas_login.create_image(
    133.0,
    112.0,
    image=entry_image_2
)

# Bind Enter key to login function
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=30.0,
    y=93.0,
    width=206.0,
    height=36.0
)
entry_2.bind('<Return>', login)  # Bind Enter key to login function

# Image 1
image_image_1 = PhotoImage(
    file=relative_to_assets_login("image_1.png"))
image_1 = canvas_login.create_image(
    331.0,
    10.0,
    image=image_image_1
)

# Image 2
image_image_2 = PhotoImage(
    file=relative_to_assets_login("image_2.png"))
image_2 = canvas_login.create_image(
    331.0,
    350.0,
    image=image_image_2
)

# Rectangles
canvas_login.create_rectangle(
    253.0,
    57.0,
    343.0,
    147.0,
    fill="#FFFFFF",
    outline=""
)

canvas_login.create_rectangle(
    253.0,
    99.0,
    274.0,
    125.0,
    fill="#FFFFFF",
    outline=""
)

canvas_login.create_rectangle(
    253.0,
    188.0,
    273.0,
    211.0,
    fill="#FFFFFF",
    outline=""
)

# Image 3
image_image_3 = PhotoImage(
    file=relative_to_assets_login("School_seal_of_Notre_Dame_of_Kidapawan_College.png"))
image_3 = canvas_login.create_image(
    432.0,
    141.0,
    image=image_image_3
)

window_login.resizable(False, False)
window_login.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()