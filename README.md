# 🔐 PassGuard: Password Analysis and Generation Toolkit

## 📌 Overview
PassGuard is a Python desktop application that helps users evaluate password strength and generate secure passwords. The project combines fundamental software engineering concepts with practical cybersecurity principles by providing a simple, interactive graphical interface for password security.

This project was developed as a hands on learning exercise to explore how cybersecurity concepts can be implemented through software development and how modular programming can improve application organization and maintainability.

---

## ✨ Features

### 🔍 Password Strength Analysis
PassGuard analyzes passwords based on:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Passwords are classified as:

- Weak
- Moderate
- Strong

The application also provides suggestions to help users create stronger passwords.

Example:

```
Strength: Weak

Suggestions:
- Use at least 8 characters.
- Add uppercase letters.
- Add special characters.
```

---

### 🔐 Secure Password Generation
PassGuard can generate random passwords containing:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Example:

```
Generated Password:
kV!7xP9@rT4#
```

---

## 🏗️ Project Structure

```text
PassGuard/
│
├── passguard.py
├── password_analyzer.py
├── password_generator.py
├── README.md
└── .gitignore
```

### File Responsibilities

**passguard.py**
- Acts as the application's entry point
- Builds the graphical user interface using Tkinter
- Connects the analyzer and generator modules

**password_analyzer.py**
- Contains the logic for evaluating password strength
- Generates security recommendations

**password_generator.py**
- Contains the logic for generating secure random passwords

---

## 🛠️ Built With

- **Python** – Core application logic
- **Tkinter** – Graphical User Interface (GUI)
- **Random Module** – Secure password generation
- **String Module** – Character handling and validation
- **Git** – Version control
- **GitHub** – Project hosting and collaboration

---

## 🚀 How to Run the Project

1. Clone or download this repository.
2. Open the project folder.
3. Run:

```bash
python passguard.py
```

---

## 🧠 Concepts Practiced

- Python programming fundamentals
- Functions and modules
- Imports and modular programming
- Graphical user interface development with Tkinter
- Password security principles
- Software organization and maintainability
- Version control using Git and GitHub

---

## 🔮 Future Improvements

Possible future enhancements include:

- Password strength meter
- Password copy button
- Password length selector
- Detection of commonly used passwords
- Password entropy calculation
- Dark mode interface
- Password history feature

---


## 👨🏾‍💻 Author

**Adeniyi Adelsoye**

Computer Engineer | Software Engineering & Cybersecurity Enthusiast

I enjoy building practical projects that explore the intersection of software engineering and cybersecurity while continuously learning and improving through hands on development.
