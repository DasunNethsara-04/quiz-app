# IMPORTS
import requests
import html
import random
import os

# IMPORTANT VARIABLES
total: int = 0
average: float = 0

# FETCH ALL THE QUESTION CATEGORIES
def fetch_question_categoriy() -> int:
    url = "https://opentdb.com/api_category.php"
    response_json = requests.get(url).json()
    print("Select Question Category,\n")
    category = response_json['trivia_categories']
    for i in category:
        print(f"{i['id']-8} - {i['name']}")
    
    choice: int = int(input("Enter the Category Number: "))
    if choice in range(1, 25):
        # clear the entire terminal window
        os.system("cls")
        return choice + 8
    else:
        print("Invalid Input.")
    # return response_json['trivia_categories']

# GET A POOL OF TRIVIA QUESTION
def get_question_pool(amount: int, category: int) -> list:
    url: str = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response_json = requests.get(url).json()
    return response_json['results']

# SHUFFLE THE ANSWERS FOR A QUESTION
def shuffle_choices(choices: list) -> list:
    random.shuffle(choices)
    return(choices)

# PRINT THE ANSWER CHOICES
def print_choices(choices: list) -> None:
    for index, choice_txt in enumerate(choices):
        print(f"{index+1}. {html.unescape(choice_txt)}")

# GET THE USER'S CHOICE
def get_user_input() -> int:
    while True:
        user_input = int(input("Enter the number os your choice: "))
        if user_input in range(1, 5):
            return user_input - 1
        else:
            print("Invalid user input. Enter the number os your choice")

# PLAY THE GAME
def play_game(amount: int, category: int) -> None:
    global total
    question_pool: list = get_question_pool(amount, category)
    for question in question_pool:
        question_text: str = html.unescape(question['question'])
        print("\n" + question_text)
        choices: list = question['incorrect_answers']
        choices.extend([question['correct_answer']])
        shuffled_choices: list = shuffle_choices(choices)
        print_choices(shuffled_choices)
        
        user_choice_index: int = get_user_input()
        user_choice_text = shuffled_choices[user_choice_index]
        correct_choice_text = html.unescape(question["correct_answer"])
        if user_choice_text == correct_choice_text:
            total += 1
            print("Correct! You got 1 point\n")
        else:
            print(f"Incorrect! Answer is {correct_choice_text}\n")
        # clear the entire terminal window
    print(f"\nGame Over...\nYour Marks: {total}/{amount}")
    print(f"Average Marks: {total/amount}")


# RUN THE GAME
if __name__ == "__main__":
    os.system('cls')
    category = fetch_question_categoriy()
    amount = int(input("Question Amount: "))
    play_game(amount, category)