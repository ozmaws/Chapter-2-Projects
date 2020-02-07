# Initialize the constants
NEW_RATE = 3.00
OLD_RATE = 2.00

# Request the inputs
newVideos = int(input("Enter the number of new videos: "))
oldVideos = int(input("Enter the number of oldies: "))

# Compute the total charge
totalCharge = ( newVideos * NEW_RATE ) + ( oldVideos * OLD_RATE )

# Display the total charge
print("The total charge is $" + str(totalCharge))

