# 🎂 Days of Your Life

A simple Python command-line application that calculates how much of your life you have lived and tells you how many days remain until your next birthday.

This project was created as a small practical Python project for learning **date/time handling, functions, user input, validation, and basic programming logic**.

## ✨ Features

* 📅 Enter your date of birth
* 🎂 Calculate your current age
* 📆 Calculate your age in years, months, and days
* ⏳ Calculate the total number of days you have lived
* 🎉 Calculate how many days remain until your next birthday
* ⚠️ Validate incorrect date input
* 🚫 Prevent future birth dates

## 🛠️ Technologies

* **Python 3**
* `datetime` — working with dates and times
* `calendar` — handling the number of days in months and leap years

No external Python packages are required.

## 📁 Project Structure

```text
days_of_your_life/
│
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mohamadfarivar/days_of_your_life.git
```

### 2. Navigate to the project

```bash
cd days_of_your_life
```

### 3. Run the program

```bash
python main.py
```

On some systems you may need:

```bash
python3 main.py
```

## 💻 Usage

After starting the program, enter your date of birth using the following format:

```text
YYYY-MM-DD
```

For example:

```text
Enter your birth date (YYYY-MM-DD): 2000-05-15
```

The program will then display information similar to:

```text
You have lived for 26 years, 3 months, and 21 days.

You have lived for a total of 9584 days.

There are 243 days until your next birthday.
```

The exact result depends on the current date.

## 🧠 How It Works

The application is built around three main operations.

### Calculate Age

The `calculate_age()` function determines the difference between the birth date and the current date.

It handles:

* Years
* Months
* Remaining days
* Leap years
* Different month lengths

### Calculate Days Lived

The `calculate_days_lived()` function calculates the total number of days between the user's birth date and today.

```python
days_lived = (current_date - birth_date).days
```

### Calculate Next Birthday

The program creates the user's birthday for the current year and checks whether it has already happened.

If it has, the birthday is moved to the following year.

```python
next_birthday = birth_date.replace(year=current_date.year)
```

The difference between today and the next birthday gives the number of remaining days.

## 📚 What I Learned

This project helped me practice several fundamental Python concepts:

* Functions
* Function parameters and return values
* `datetime`
* `calendar`
* `try` / `except`
* `while` loops
* `if` statements
* User input
* String formatting
* Date arithmetic
* Error handling
* Leap-year considerations
* Basic Git and GitHub workflow

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Add hours, minutes, and seconds lived
* [ ] Show the exact date of the next birthday
* [ ] Add a countdown to the next birthday
* [ ] Add weeks lived
* [ ] Add months lived
* [ ] Add percentage of an expected lifetime
* [ ] Add support for different date formats
* [ ] Add unit tests
* [ ] Improve the command-line interface
* [ ] Add a graphical interface
* [ ] Add support for Persian calendar dates

## 🎯 Project Goal

The goal of this project is not to build a complex application, but to practice Python by building something small, useful, and understandable.

It is part of my journey to improve my **Python programming and software development skills through practical projects**.

## 📄 License

This project is licensed under the MIT License.

See the [`LICENSE`](LICENSE) file for more information.

---

⭐ If you find this project useful, feel free to star the repository!
