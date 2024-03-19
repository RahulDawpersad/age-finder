from datetime import datetime

def calculate_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    birth_date = datetime(birth_year, birth_month, birth_day)
    current_date = datetime(current_year, current_month, current_day)
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    return age

def main():
    try:
        birth_year = int(input("Enter the year you were born: "))
        birth_month = int(input("Enter the month you were born (1-12): "))
        birth_day = int(input("Enter the day you were born (1-31): "))
        
        current_year = datetime.now().year
        current_month = datetime.now().month
        current_day = datetime.now().day
        
        age = calculate_age(birth_year, birth_month, birth_day, current_year, current_month, current_day)
        print("Your age is:", age)
        
    except ValueError:
        print("Invalid input: Please enter valid years, months, and days as integers.")

if __name__ == "__main__":
    main()

