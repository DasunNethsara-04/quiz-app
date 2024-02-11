# IMPORTS
import customtkinter as ctk

# IMPORTANT USER INTERFACE SETTINGS
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


# USER INTERFACE 
root = ctk.CTk()
root.title("Quiz App - v1.0")
root.resizable(width=False, height=False)
root.iconbitmap(False, "img/icon.ico")
width_of_window: int = 1280
height_of_window: int = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = (screen_width / 2) - (width_of_window / 2)
y_cordinate = (screen_height / 2) - (height_of_window / 2)
root.geometry(
    "%dx%d+%d+%d" % (width_of_window, height_of_window, x_cordinate, y_cordinate)
)

# USER INTERFACE WINDOW WIDGETS
ctk.CTkLabel(root, text="QUIZ APP", text_color="#18cc5d", font=("Ubuntu", 55)).pack(pady=20)

# FRAME FOR HOME WINDOW
home_frame = ctk.CTkFrame(root, width=750, height=400)
home_frame.pack(pady=50)

# WIDGETS FOR HOME FRAME
txt_name = ctk.CTkLabel(home_frame, text="Your Name", font=("Poppins", 18))
txt_name.grid(row=0, column=0, pady=20, padx=15)
name_entry = ctk.CTkEntry(home_frame, font=("Ubuntu", 16, "bold"), width=300)
name_entry.grid(row=0, column=1, pady=20, padx=15)

txt_category = ctk.CTkLabel(home_frame, text="Question Category", font=("Poppins", 18))
txt_category.grid(row=1, column=0, pady=20, padx=15)
category_entry = ctk.CTkEntry(home_frame, font=("Ubuntu", 16, "bold"), width=300)
category_entry.grid(row=1, column=1, pady=20, padx=15)

txt_amount = ctk.CTkLabel(home_frame, text="Question Amount", font=("Poppins", 18))
txt_amount.grid(row=2, column=0, pady=20, padx=15)
amount_entry = ctk.CTkEntry(home_frame, font=("Ubuntu", 16, "bold"), width=300)
amount_entry.grid(row=2, column=1, pady=20, padx=15)

# START BUTTON
ctk.CTkButton(root, text="Start Quiz", font=("Ubuntu", 25), height=50, width=170).pack(pady=50)


if __name__ == "__main__":
    root.mainloop()