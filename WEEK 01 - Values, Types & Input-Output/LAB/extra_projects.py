# =================================
# PROJECT 1: BAND NAME GENERATOR
# =================================

print("Welcome to the Band Name Generator!")

print("\nLet's create your band name!\n")

city = input("What city did you grow up in? ")
pet = input("What is the name of your pet? ")
band_name = city + " " + pet

print(f"Your band name could be: {band_name}")



# =================================
# PROJECT 2: TIP CALCULATOR
# =================================

bill = float(input("What was the total bill? £"))
people = int(input("How many people are splitting the bill? "))
tip = int(input("What percentage tip would you like to give? "))

tip_amount = bill * (tip / 100)
total_with_tip = bill + tip_amount
amount_per_person = total_with_tip / people

print(f"Each person should pay: £{amount_per_person:.2f}")