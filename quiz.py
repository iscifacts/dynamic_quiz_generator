import tkinter as tk
from tkinter import messagebox


question_bank = {
    "arrays": {
        "beginner": [
            {"question": "What is an array?", "options": ["A linear data structure", "A non-linear data structure", "A tree data structure"], "answer": 0},
            {"question": "What is the time complexity of accessing an element in an array?", "options": ["O(1)", "O(log n)", "O(n)"], "answer": 0}
        ],
        "intermediate": [
            {"question": "What is a dynamic array?", "options": ["An array with a fixed size", "An array that grows dynamically", "An array with random access"], "answer": 1},
            {"question": "What is the time complexity of inserting an element in an array?", "options": ["O(1)", "O(log n)", "O(n)"], "answer": 2}
        ],
        "advanced": [
            {"question": "What is an array data structure?", "options": ["A collection of elements", "A sorted collection of elements", "A binary tree"], "answer": 0},
            {"question": "What is the space complexity of an array?", "options": ["O(1)", "O(log n)", "O(n)"], "answer": 0}
        ]
    },
    "linked_lists": {
        "beginner": [
            {"question": "What is a linked list?", "options": ["A linear data structure", "A non-linear data structure", "A tree data structure"], "answer": 0},
            {"question": "What is the time complexity of accessing an element in a linked list?", "options": ["O(1)", "O(log n)", "O(n)"], "answer": 2}
        ],
        "intermediate": [
            {"question": "What is a doubly linked list?", "options": ["A linked list with two heads", "A linked list with two tails", "A linked list with both forward and backward links"], "answer": 2},
            {"question": "What is the time complexity of inserting an element at the beginning of a linked list?", "options": ["O(1)", "O(log n)", "O(n)"], "answer": 0}
        ],
        "advanced": [
            {"question": "What is a circular linked list?", "options": ["A linked list with a loop", "A linked list with a cycle", "A linked list with a sentinel node"], "answer": 1},
            {"question": "What is the space complexity of a linked list?", "options": ["O(1)", "O(log n)", "O(n)"], "answer": 0}
        ]
    },
    "Trees": {
        "beginner": [
            {"question": "What is a tree?", "options": ["A linear data structure", "A non-linear data structure", "A tree data structure"], "answer": 0},
            {"question": "What is the time complexity of accessing an element in a tree?", "options": ["O(1)", "O(log n)", "O(n)"], "answer": 2}
        ],
        "intermediate": [
            {"question": "What is a binary search tree?", "options": ["A linked list with two heads", "A linked list with two tails", "A linked list with both forward and backward links"], "answer": 2},
            {"question": "What is the time complexity of inserting an element at the beginning of a linked list?", "options": ["O(1)", "O(log n)", "O(n)"], "answer": 0}
        ],
        "advanced": [
            {"question": "What is a circular linked list?", "options": ["A linked list with a loop", "A linked list with a cycle", "A linked list with a sentinel node"], "answer": 1},
            {"question": "What is the space complexity of a linked list?", "options": ["O(1)", "O(log n)", "O(n)"], "answer": 0}
        ]
    }
}

def generate_quiz(selected_topics, difficulty_level):
    selected_questions = []
    for topic in selected_topics:
        if topic in question_bank and difficulty_level in question_bank[topic]:
            selected_questions.extend(question_bank[topic][difficulty_level])
    return selected_questions

def present_quiz(quiz):
    score = 0
    current_question_index = 0
    answer_vars = []

    clear_window()

    quiz_frame = tk.Frame(root)
    quiz_frame.pack()

    def display_question():
        nonlocal current_question_index
        nonlocal answer_vars

        for widget in quiz_frame.winfo_children():
            widget.destroy()

        question = quiz[current_question_index]

        question_label = tk.Label(quiz_frame, text=f"Question {current_question_index+1}: {question['question']}", font=("Arial", 12, "bold"))
        question_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        answer_var = tk.IntVar()
        answer_vars.append(answer_var)
        for j, option in enumerate(question['options']):
            option_radio = tk.Radiobutton(quiz_frame, text=option, variable=answer_var, value=j)
            option_radio.grid(row=j+1, column=0, sticky="w", padx=10, pady=2)

    def next_question():
        nonlocal current_question_index
        nonlocal score
        selected_option = answer_vars[current_question_index].get()
        correct_answer = quiz[current_question_index]['answer']
        if selected_option == correct_answer:
            score += 1
        current_question_index += 1
        if current_question_index < len(quiz):
            display_question()
        else:
            messagebox.showinfo("Quiz Ended", f"Your score: {score}/{len(quiz)}")
            clear_window()

    display_question()

    next_button = tk.Button(quiz_frame, text="Next", command=next_question)
    next_button.grid(row=len(quiz[current_question_index]['options'])+1, column=0, pady=10)

    submit_button = tk.Button(quiz_frame, text="Submit", command=lambda: submit_answers(quiz, answer_vars))
    submit_button.grid(row=len(quiz[current_question_index]['options'])+1, column=1, pady=10)


    
def submit_answers(quiz, answer_vars):
    score = 0
    for i, question in enumerate(quiz):
        selected_option = answer_vars[i].get()
        correct_answer = question['answer']
        if selected_option == correct_answer:
            score += 1
    messagebox.showinfo("Quiz Ended", f"Your score: {score}/{len(quiz)}")
    clear_window()
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()





root = tk.Tk()
root.title("Quiz Generator")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 400
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

topics_label = tk.Label(root, text="Select Topics:")
topics_label.grid(row=0, column=0, padx=10, pady=10)

topics_var = tk.StringVar()
topics_combobox = tk.OptionMenu(root, topics_var, *question_bank.keys())
topics_combobox.grid(row=0, column=1, padx=10, pady=10)

difficulty_label = tk.Label(root, text="Select Difficulty Level:")
difficulty_label.grid(row=1, column=0, padx=10, pady=10)

difficulty_var = tk.StringVar()
difficulty_combobox = tk.OptionMenu(root, difficulty_var, "beginner", "intermediate", "advanced")
difficulty_combobox.grid(row=1, column=1, padx=10, pady=10)

start_button = tk.Button(root, text="Start Quiz", command=lambda: start_quiz())
start_button.grid(row=2, columnspan=2, padx=10, pady=10)

def start_quiz():
    selected_topics = [topics_var.get()]
    difficulty_level = difficulty_var.get()
    if selected_topics[0] and difficulty_level:
        quiz = generate_quiz(selected_topics, difficulty_level)
        present_quiz(quiz)
    else:
        messagebox.showwarning("Incomplete Selection", "Please select both topics and difficulty level.")

root.mainloop()
