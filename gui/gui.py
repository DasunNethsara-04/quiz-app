"""
CTkMessageBox icons
    -> info
    -> check
    -> warning
    -> cancel
    -> question
"""

# IMPORTS
from tkinter import StringVar
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import requests

# IMPORTANT VARIABLES
CURRENT_USER: str = ""
TOTAL: int = 0
CHOSEN_CATEGORY_ID: str = ""
CHOSEN_Q_AMOUNT: int = 5  # default number is 5

# IMPORTANT USER INTERFACE SETTINGS
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

# FUNCTIONS
def get_question_categories() -> None:
    '''Get the Question Categories'''
    url = "https://opentdb.com/api_category.php"
    response_json = requests.get(url).json()
    choices_json = response_json["trivia_categories"]
    categories = [f"{x['id']-8}. {x['name']}" for x in choices_json]
    category_combo.configure(values=categories)
    category_combo.set(categories[0])

def clear_frame(frame_name) -> None:
    '''Clean every widgets in a selected frame'''
    for widgets in frame_name.winfo_children():
      widgets.destroy()

def get_user_data_home() -> None:
    '''Get user inputs (name, question category, question amount)'''
    global CHOSEN_CATEGORY_ID, CURRENT_USER, CHOSEN_Q_AMOUNT
    if name_entry.get() != "" or amount_entry.get() != "":
        name: str = name_entry.get()
        category: str = category_combo.get()
        pos, category = category.split(". ")
        CHOSEN_CATEGORY_ID = int(pos)+8
        CURRENT_USER = name
        try:
            amount: int = int(amount_entry.get())
        except:
            CTkMessagebox(master=root, title="Error", message="Question Amount should be a number!", icon="cancel")
            amount: int = 5
        CHOSEN_Q_AMOUNT = amount
        header_lbl.configure(text=category)
        clear_frame(home_frame)
        btn_txt.set("Check Answer")
        btn.configure(command=check_answer)
    else:
        CTkMessagebox(master=root, title="Alert", message="All fields are required", icon="warning")

def get_question_pool(amount: int, category: int) ->  list:
    '''Get the question pool for selected question category from Trivia API'''
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response_json = requests.get(url).json()
    questions = response_json['results']
    return questions

def check_answer() -> None:
    '''Check the answer'''
    print("OK")

def play_game() -> None:
    question_pool = get_question_pool()

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
header_lbl = ctk.CTkLabel(root, text="QUIZ APP", text_color="#18cc5d", font=("Ubuntu", 55))
header_lbl.pack(pady=20)

# FRAME FOR HOME WINDOW
home_frame = ctk.CTkFrame(root, width=850, height=400)
home_frame.pack(pady=50)

# WIDGETS FOR HOME FRAME
txt_name = ctk.CTkLabel(home_frame, text="Your Name", font=("Poppins", 18))
txt_name.grid(row=0, column=0, pady=20, padx=15)
name_entry = ctk.CTkEntry(home_frame, font=("Ubuntu", 16, "bold"), width=300)
name_entry.grid(row=0, column=1, pady=20, padx=15)

txt_category = ctk.CTkLabel(home_frame, text="Question Category", font=("Poppins", 18))
txt_category.grid(row=1, column=0, pady=20, padx=15)
category_combo = ctk.CTkComboBox(home_frame, width=300, font=("Ubuntu", 16, "bold"), state="readonly")
category_combo.grid(row=1, column=1, pady=20, padx=15)

txt_amount = ctk.CTkLabel(home_frame, text="Question Amount", font=("Poppins", 18))
txt_amount.grid(row=2, column=0, pady=20, padx=15)
amount_entry = ctk.CTkEntry(home_frame, font=("Ubuntu", 16, "bold"), width=300)
amount_entry.grid(row=2, column=1, pady=20, padx=15)

# START BUTTON
btn_txt = StringVar()
btn_txt.set("Start Quiz")
btn = ctk.CTkButton(root, textvariable=btn_txt, font=("Ubuntu", 25), height=50, width=170, command=get_user_data_home)
btn.pack(pady=50)


if __name__ == "__main__":
    get_question_categories()
    root.mainloop()