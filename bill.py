#Creating a bill calculator program
import sys

# Electricity Unit Price
# Defining electricity price constants here
ELECTRICITY_CHARGE_ONE = 5
ELECTRICITY_CHARGE_TWO = 10
ELECTRICITY_CHARGE_THREE = 15

# Water Unit Price
# Defining Water price constants here
WATER_CHARGE_ONE = 50
WATER_CHARGE_TWO = 60
WATER_CHARGE_THREE = 70

# Implementation

# Input 1 Validation
# getting the bill type from user
print("Enter the type of bill you want to calculate:")
print(" 1. Electricity")
print(" 2. Water")
billType = int(input("Your choice: "))

# checking if bill type is valid
if billType > 2 or billType < 0:
    print("Error! enter a number to choose a bill type from the list")
    sys.exit()

# Input 2 Validation
# getting the meter reading from the user
if billType == 1:
    electricityReading = input("Enter your electricity meter reading in kwH: ")
    # getting the number of people from the household
    numberOfPeople = input("Enter the number of people in your household (max - 20 people): ")
    numberOfPeople = int(numberOfPeople)
    # checking if meter reading is valid
    try:
        electricityReading = int(electricityReading)
        print("")       
    except ValueError:
        print("Error! Please enter a numerical meter reading")
        
    #checking if the number of people is between 0 and 20
    if numberOfPeople > 0 and numberOfPeople <= 20:
        print()
    else:
        print("The maximum people is 20")
        sys.exit()
        
    # Bill Calculation
    # calculating and displaying the bill
    print("\nCalculating Electricity bill...")
    if electricityReading < 100:
        electricityBill = ELECTRICITY_CHARGE_ONE * electricityReading
        print(f"\nYour total Electricity Bill is ${electricityBill}.")
        billPerPerson = electricityBill / numberOfPeople
        if billPerPerson <= 300:
            print(f"Your per person usage bill is {billPerPerson} - This is considered normal.\n")
        else:
            print(f"Your per person usage bill is {billPerPerson} - This is considered above average.\n")
            
    elif electricityReading < 1000:
        electricityBill = ELECTRICITY_CHARGE_TWO * electricityReading
        print(f"\nYour total Electricity Bill is ${electricityBill}.")
        billPerPerson = electricityBill / numberOfPeople
        if billPerPerson <= 300:
            print(f"Your per person usage bill is {billPerPerson} - This is considered normal.\n")
        else:
            print(f"Your per person usage bill is {billPerPerson} - This is considered above average.\n")
    else:
        electricityBill = ELECTRICITY_CHARGE_THREE * electricityReading
        print(f"\nYour total Electricity Bill is ${electricityBill}.")
        billPerPerson = electricityBill / numberOfPeople
        if billPerPerson <= 300:
            print(f"Your per person usage bill is {billPerPerson} - This is considered normal.\n")
        else:
            print(f"Your per person usage bill is {billPerPerson} - This is considered above average.\n")
            
else:
    waterMeterReading = int(input("Enter you water meter reading in m^3: "))
    # getting the number of people from the household
    numberOfPeople = input("Enter the number of people in your household (max - 20 people): ")
    numberOfPeople = int(numberOfPeople)
    #checking if meter reading is valid
    try:
        waterMeterReading = int(waterMeterReading)
        print("\nCalculating Water bill...")       
    except ValueError:
        print("Error! Please enter a numerical meter reading")
        
    #checking if the number of people is between 0 and 20
    if numberOfPeople > 0 and numberOfPeople <= 20:
        print()
    else:
        print("The maximum people is 20")
        sys.exit()
        
    # Bill Calculation
    # calculating and displaying the bill
    if waterMeterReading <= 500 and waterMeterReading >= 0:
        waterBill = WATER_CHARGE_ONE * waterMeterReading
        print(f"\nYour total Water Bill is ${waterBill}.")
        billPerPerson = waterBill / numberOfPeople
        if billPerPerson <= 500:
            print(f"Your per person usage bill is {billPerPerson} - This is considered normal.\n")
        else:
            print(f"Your per person usage bill is {billPerPerson} - This is considered above average.\n")
    elif waterMeterReading > 500 and waterMeterReading <= 2500:
        waterBill = WATER_CHARGE_TWO * waterMeterReading
        print(f"\nYour total Water Bill is ${waterBill}.")
        billPerPerson = waterBill / numberOfPeople
        if billPerPerson <= 500:
            print(f"Your per person usage bill is {billPerPerson} - This is considered normal.\n")
        else:
            print(f"Your per person usage bill is {billPerPerson} - This is considered above average.\n")
    else:
        waterBill = WATER_CHARGE_THREE * waterMeterReading
        print(f"\nYour total Water Bill is ${waterBill}.")
        billPerPerson = waterBill / numberOfPeople
        if billPerPerson <= 500:
            print(f"Your per person usage bill is {billPerPerson} - This is considered normal.\n")
        else:
            print(f"Your per person usage bill is {billPerPerson} - This is considered above average.\n")
