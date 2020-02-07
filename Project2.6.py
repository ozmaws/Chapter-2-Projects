# Request the inputs
mass = int(input("Enter the mass in kg: "))
velocity = int(input("Enter the velocity in m/s: "))

# compute the momentum
momentum = mass * velocity

# compute kinetic energy
kineticEnergy = (1/2) * mass * velocity ** 2

# Display the momentum and kinetic energy
print("The momentum is " + str(momentum) + " kg*(m/s)")
print("The kinetic energy is " + str(kineticEnergy) + " joules")


