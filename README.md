# Customizable Password Generator

A lightweight, command-line Python utility that generates secure, random passwords based on user-defined criteria. Users can customize the password length and choose whether to include uppercase letters, lowercase letters, numbers, and special characters.

---

## Features

* **Custom Length:** Generate passwords of any desired length.
* **Character Filtering:** Explicitly include or exclude:
    * Uppercase letters (`A-Z`)
    * Lowercase letters (`a-z`)
    * Digits (`0-9`)
    * Special symbols/punctuation (`!@#$`, etc.)
* **Error Handling:** Basic validation to ensure at least one character type is selected.

---

## How It Works

The script leverages Python's built-in `random` and `string` modules:
1. It prompts the user for the desired password length and character preferences.
2. It dynamically builds a pool of allowed characters based on the user's inputs.
3. It randomly selects characters from that pool using a list comprehension and joins them into a final password string.

---

## Prerequisites

To run this project, you only need **Python 3.x** installed on your system. No external dependencies or third-party libraries are required.

---

## Getting Started

### 1. Clone or Download the Script
Save the code into a file named `password_generator.py`.

### 2. Run the Script
Open your terminal or command prompt, navigate to the directory where the file is saved, and run:

```bash
python password_generator.py
