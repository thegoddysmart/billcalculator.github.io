
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
if billType > 2:
    print("Error: enter a number to choose a bill type from the list")
    sys.exit()

# Input 2 Validation
# TODO: get the meter reading from the user
if billType == 1:
    electricityMeterReading = int(input("Enter your electricity meter reading in kwH: "))
    # checking if meter reading is valid
    if electricityMeterReading == str():
        print("Error: Please enter a numerical meter reading")  
    else:
        print("\nCalculating Electricity bill...")
        # Bill Calculation
        # TODO: calculating and displaying the bill
        if electricityMeterReading < 100:
            electricityBill = ELECTRICITY_CHARGE_ONE * electricityMeterReading
            print(f"\nYour total Electricity Bill is ${electricityBill}.\n")
        elif electricityMeterReading < 1000:
            electricityBill = ELECTRICITY_CHARGE_TWO * electricityMeterReading
            print(f"\nYour total Electricity Bill is ${electricityBill}.\n")
        else:
            electricityBill = ELECTRICITY_CHARGE_THREE * electricityMeterReading
            print(f"\nYour total Electricity Bill is ${electricityBill}.\n")
    
elif billType == 2:
    waterMeterReading = int(input("Enter you water meter reading in m^3: "))
    #checking if meter reading is valid
    if waterMeterReading == str():
        print("Error: Please enter a numerical meter reading")
    else: 
        print("\nCalculating Water bill...")
        # Bill Calculation
        # calculating and displaying the bill
        if waterMeterReading < 50:
            waterBill = WATER_CHARGE_ONE * waterMeterReading
            print(f"\nYour total Electricity Bill is ${waterBill}.\n")
        elif waterMeterReading < 60:
            waterBill = WATER_CHARGE_TWO * waterMeterReading
            print(f"\nYour total Electricity Bill is ${waterBill}.\n")
        else:
            waterBill = WATER_CHARGE_THREE * waterMeterReading
            print(f"\nYour total Electricity Bill is ${waterBill}.\n")
