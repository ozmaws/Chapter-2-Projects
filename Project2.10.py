#Initialize the constants

#Request the inputs
hourlyWage = int(input("Enter your hourly wage: "))
totalReg = int(input("Enter your total regular hours: "))
totalOver = int(input("Enter your total overtime hours: "))

# Calculate total pay
totalPay = ( hourlyWage * totalReg) + (totalOver * (hourlyWage * 1.5))

# Display total weekly pay
print("Your total weekly pay is $" + str(totalPay))
