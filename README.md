# 💕 Love Calculator

A simple **Love Calculator** built with Python 🐍 that calculates a compatibility score between two names based on the occurrence of letters from the words **TRUE** and **LOVE**.

---

## ✨ Features

* 👤 Takes two names from the user
* 🔤 Converts names to lowercase for consistent results
* 🔎 Counts letters from **TRUE**
* ❤️ Counts letters from **LOVE**
* 🧮 Combines both scores into a two-digit Love Score
* 💻 Runs directly in the terminal

---

## 🧠 How It Works

The program follows a simple process:

```text
        👤 Name 1
           +
        👤 Name 2
           │
           ▼
     🔤 Convert to lowercase
           │
           ▼
      ┌─────────────┐
      │    TRUE     │
      │ Count chars │
      └──────┬──────┘
             │
             ▼
        🔢 First digit
             │
             +
      ┌─────────────┐
      │    LOVE     │
      │ Count chars │
      └──────┬──────┘
             │
             ▼
       🔢 Second digit
             │
             ▼
       💕 LOVE SCORE
```

### Example

If the program calculates:

```text
TRUE = 4
LOVE = 2
```

The final score will be:

```text
42%
```

---

## 🚀 Example

### Input

```text
What is your name?
Kanye West

What is your lover name?
Kim Kardashian
```

### Output

```text
Your love score is 42
```

---

## 🛠️ Technologies Used

* 🐍 Python
* 🔁 `for` loops
* ❓ `if` statements
* 🔤 Strings
* 🔢 Variables
* ⌨️ `input()`
* 🔠 `.lower()`
* 📦 Functions

---

## 📚 What I Learned

This project helped me practice:

* Creating and calling functions
* Working with user input
* Iterating through strings
* Using conditional statements
* Counting characters
* String manipulation
* Combining variables to create a final result

---

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate to the project folder:

```bash
cd love-calculator
```

Run the program:

```bash
python love_calculator.py
```

---

## 📸 Project Preview

```text
╔══════════════════════════════════╗
║        💕 LOVE CALCULATOR 💕     ║
╠══════════════════════════════════╣
║                                  ║
║  👤 Your Name:                   ║
║  💘 Lover's Name:                ║
║                                  ║
║       ❤️ LOVE SCORE: 42          ║
║                                  ║
╚══════════════════════════════════╝
```

---

## 🎯 Project Status

**Completed ✅**

This is a beginner Python project created as part of my journey to improve my programming skills.

---

## 👨‍💻 Author

**Nour Eldeen**

Learning Python 🐍 | Building Projects 🚀 | Improving Every Day 📈

---

⭐ If you found this project interesting, feel free to star the repository!
