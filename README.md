# 💕 Love Calculator

```text
██╗      ██████╗ ██╗   ██╗███████╗
██║     ██╔═══██╗██║   ██║██╔════╝
██║     ██║   ██║██║   ██║█████╗
██║     ██║   ██║╚██╗ ██╔╝██╔══╝
███████╗╚██████╔╝ ╚████╔╝ ███████╗
╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝

        💕 LOVE CALCULATOR 💕
        ❤️ Find Your Love Score ❤️
```

> 🐍 A beginner-friendly Python project that calculates a **Love Score** based on the names entered by two people.

---

## ✨ Features

* 👤 Takes two names from the user
* 🔤 Converts names to lowercase
* 🔎 Counts letters from **TRUE**
* ❤️ Counts letters from **LOVE**
* 🧮 Combines both results into a two-digit Love Score
* 💻 Runs directly in the terminal
* 🎨 Includes a custom ASCII art interface

---

## 🧠 How It Works

The program combines both names and checks every letter against two groups:

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

### ❤️ Example

If the program finds:

```text
TRUE = 4
LOVE = 2
```

The final Love Score becomes:

```text
42
```

---

## 🚀 Example

### Input

```text
what is your name?
Kanye West

what is your lover name?
Kim Kardashian
```

### Output

```text
your love score is 42
```

---

## 🖥️ Terminal Preview

```text
██╗      ██████╗ ██╗   ██╗███████╗
██║     ██╔═══██╗██║   ██║██╔════╝
██║     ██║   ██║██║   ██║█████╗
██║     ██║   ██║╚██╗ ██╔╝██╔══╝
███████╗╚██████╔╝ ╚████╔╝ ███████╗
╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝

        💕 LOVE CALCULATOR 💕
        ❤️ Find Your Love Score ❤️

what is your name?
Kanye West

what is your lover name?
Kim Kardashian

your love score is 42
```

---

## 🛠️ Built With

```text
🐍 Python
```

### Python Concepts Used

* 🔹 Functions
* 🔹 Variables
* 🔹 User Input
* 🔹 Strings
* 🔹 `for` loops
* 🔹 `if` statements
* 🔹 `in` operator
* 🔹 `.lower()` method
* 🔹 String formatting

---

## 📚 What I Learned

While building this project, I practiced:

* Creating and calling functions
* Working with user input
* Iterating through strings
* Using conditional statements
* Counting characters
* Working with strings
* Using the `in` operator
* Making a simple interactive terminal program

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project

```bash
cd love-calculator
```

### 3. Run the program

```bash
python love_calculator.py
```

---

## 🎯 Project Status

```text
Status: ✅ Completed
Level:  🟢 Beginner
Language: 🐍 Python
```

This project was created as part of my journey to learn Python and build projects from scratch.

---

## 👨‍💻 Author

### Nour Eldeen

🐍 Learning Python
💻 Building Projects
📈 Improving Every Day

---

⭐ **If you like the project, feel free to star the repository!**
