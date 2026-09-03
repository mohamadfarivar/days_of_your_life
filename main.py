from calendar import monthrange
from datetime import datetime


def calculate_age(birth_date, current_date=None):
    if current_date is None:
        current_date = datetime.now()

    if birth_date > current_date:
        raise ValueError("Birth date cannot be in the future.")

    years = current_date.year - birth_date.year
    try:
        anniversary = birth_date.replace(year=birth_date.year + years)
    except ValueError:
        anniversary = birth_date.replace(year=birth_date.year + years, day=28)

    if anniversary > current_date:
        years -= 1
        try:
            anniversary = birth_date.replace(year=birth_date.year + years)
        except ValueError:
            anniversary = birth_date.replace(year=birth_date.year + years, day=28)

    months = 0
    while True:
        total_months = anniversary.month - 1 + months + 1
        next_month = total_months % 12 + 1
        next_year = anniversary.year + total_months // 12
        next_day = min(anniversary.day, monthrange(next_year, next_month)[1])
        next_anniversary = anniversary.replace(
            year=next_year, month=next_month, day=next_day
        )
        if next_anniversary > current_date:
            break
        months += 1

    month_anniversary = anniversary
    total_months = anniversary.month - 1 + months
    month_anniversary = month_anniversary.replace(
        year=anniversary.year + total_months // 12,
        month=total_months % 12 + 1,
        day=min(
            anniversary.day,
            monthrange(
                anniversary.year + total_months // 12,
                total_months % 12 + 1,
            )[1],
        ),
    )
    days = (current_date - month_anniversary).days
    return years, months, days


def calculate_days_lived(birth_date, current_date=None):
    if current_date is None:
        current_date = datetime.now()

    if birth_date > current_date:
        raise ValueError("Birth date cannot be in the future.")

    days_lived = (current_date - birth_date).days
    return days_lived


def get_birth_date_from_user():

    while True:
        try:
            birth_date_input = input("\nEnter your birth date (YYYY-MM-DD): ")
            birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
            return birth_date
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# Example usage:
if __name__ == "__main__":
    # Get the birth date from the user
    birth_date = get_birth_date_from_user()
    current_date = datetime.now()       # Current date

    years, months, days = calculate_age(birth_date, current_date)
    print(f"\nYou have lived for {years} years, {months} months, and {days} days.")

    # Calculate the number of days lived
    days_lived = calculate_days_lived(birth_date, current_date)
    print(f"You have lived for a total of {days_lived} days.")

    # Calculate the number of days until the next birthday
    next_birthday = birth_date.replace(year=current_date.year)
    if next_birthday < current_date:
        next_birthday = next_birthday.replace(year=next_birthday.year + 1)

    days_until_birthday = (next_birthday - current_date).days
    print(f"There are {days_until_birthday} days until your next birthday.\n")
