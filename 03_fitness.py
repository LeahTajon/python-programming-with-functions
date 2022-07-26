# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Please enter your gender (M/F): ')
    bdate = input('Please enter your date of birth (YYYY-MM-DD): ')
    w = float(input('Enter your weight in pounds: '))
    h = float(input('Enter your height in inches: '))

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(bdate)
    weight = kg_from_lb(w)
    height = cm_from_in(h)

    bmi = body_mass_index(weight, height)
    bmr = basal_metabolic_rate(gender, weight, height, age)

    # Print the results for the user to see.
    
    # Please enter your gender (M or F): F
    # Enter your birthdate (YYYY-MM-DD): 2001-03-21
    # Enter your weight in U.S. pounds: 125
    # Enter your height in U.S. inches: 54
    # Age (years): 19
    # Weight (kg): 56.70
    # Height (cm): 137.2
    # Body mass index: 30.1
    # Basal metabolic rate (kcal/day): 1315
    
    print(f'Your age is: {age}')
    print(f'Weight in kilograms: {weight:.2f}')
    print(f'Height in centimeters: {height:.2f}')
    print(f'Body Mass Index: {bmi:.2f}')
    print(f'Basal Metabolic Rate: {bmr:.2f}')




def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.

    1 lb = 0.45359237 kg
    """
    kilo = pounds * 0.45359237

    return kilo


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.

    1 in = 2.54 cm
    """
    centi = inches * 2.54

    return centi


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / height ** 2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.

    (women)  bmr = 447.593 + 9.247 weight + 3.098 height − 4.330 age
    (men)  bmr = 88.362 + 13.397 weight + 4.799 height − 5.677 age
    """
    if gender.lower() == 'm':
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    elif gender.lower() == 'f':
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    
    return bmr


# Call the main function so that
# this program will start executing.
main()
