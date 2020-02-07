#math notes
#10,000km between npole and equator
#90 degrees between npole and equator
#1 degree = 60 min
#1 min = 1 mile

#Request the inputs
kilometer = int(input("Enter the number of kilometers: "))

# Compute the nautical miles
nauticalMiles = ( kilometer / 10000 ) * 90 * 60

# Display the corresponding nautical miles
print("The corresponding number of nautical miles is " + str(nauticalMiles))
