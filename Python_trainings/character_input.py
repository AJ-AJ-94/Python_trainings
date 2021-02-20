import datetime

name = input("Whats your name? ")
age = input("Print your age, please: ")

counting_years = 100 - int(age)
today = datetime.date.today().year
calculation = int(today) + int(counting_years)

# year = str((2021 - age)+100)

print("Hi " + name + "\n" "You are " + age + ".")
print("In " + str(calculation) + " you will turn 100 years. Congrats!")