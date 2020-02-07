# Request the inputs
sphereRadius = float(input("Enter the radius: "))

# Compute the diameter
sphereDiameter = 2 * sphereRadius

# Compute the circumference
sphereCircumference = 6.2832 * sphereRadius

# Compute the surface area
sphereSurface = 4 * 3.14 * sphereRadius ** 2

# Compute the volume
sphereVolume = ( 4 / 3 ) * 3.14 * (sphereRadius ** 3) 

# Display the diameter, circumferance, surface are, and volume
print("The diameter is " + str(sphereDiameter))
print("The circumference is " + str(sphereCircumference))
print("The surface area is " + str(sphereSurface))
print("The volume is " + str(sphereVolume))
