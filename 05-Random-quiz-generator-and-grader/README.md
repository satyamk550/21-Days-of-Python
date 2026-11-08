# 🧠 Random Quiz Generator and Grader

A command-line quiz application built using Python. It randomly selects questions from a JSON question bank, presents multiple-choice questions to the user, evaluates their answers, and generates a final score with completion time.

## 📌 Project Overview

This project is part of my **21 Days of Python** learning journey.

The objective is to build an interactive quiz application while practicing Python concepts such as file handling, JSON data management, randomization, user input, functions, and time tracking.

## ✨ Features

- **JSON Question Bank:** Stores questions, answer options, and correct answers in a JSON file.
- **Random Question Selection:** Randomly selects questions from the available question bank.
- **Multiple-Choice Questions:** Displays questions with numbered answer options.
- **Automatic Grading:** Evaluates user responses and tracks correct answers.
- **Score Calculation:** Calculates the final score and percentage.
- **Time Tracking:** Measures the time taken to complete the quiz.
- **Interactive CLI:** Allows users to participate through the terminal.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Modules:**
  - `json` – Loads and processes quiz data from a JSON file.
  - `random` – Selects questions randomly without repetition.
  - `time` – Tracks the quiz completion time.

## 📂 Project Structure

```text
05-Random-Quiz-Generator-and-Grader/
│
├── main.py
├── questions.json
└── README.md
```

## 🚀 How to Run

**1. Clone the repository**

```bash
git clone <your-repository-url>
```

**2. Navigate to the project directory**

```bash
cd 05-Random-Quiz-Generator-and-Grader
```

**3. Run the application**

```bash
python main.py
```

**4. Enter the number of questions**

Choose how many questions you want to attempt and answer them through the terminal.

## 🎮 How It Works

1. The application loads questions from `questions.json`.
2. The user specifies the number of questions to attempt.
3. The program randomly selects questions from the question bank.
4. Each question is displayed with multiple answer options.
5. The user selects an answer by entering its corresponding number.
6. The application checks the answer and updates the score.
7. After completing the quiz, the application displays:
   - Total questions
   - Correct answers
   - Final score percentage
   - Total completion time

## 📚 What I Learned

Through this project, I practiced:

- Reading and processing JSON files using Python.
- Working with structured external data.
- Using Python's built-in modules: `json`, `random`, and `time`.
- Implementing functions to organize program logic.
- Generating random selections using `random.sample()`.
- Taking user input and implementing conditional logic.
- Comparing answers and tracking scores.
- Calculating percentages and measuring execution time.
- Debugging file handling and JSON parsing errors.

## 🔮 Future Improvements

- Add input validation for invalid user entries.
- Allow users to retry questions.
- Introduce different difficulty levels.
- Add quiz categories.
- Implement a leaderboard to store high scores.
- Add a countdown timer for each question.
- Display correct answers and explanations after the quiz.
- Build a graphical user interface (GUI).

---

**Part of my 21 Days of Python learning journey 🐍**

*Learning Python through hands-on projects, one day at a time.*