def calculate_volume_of_sphere(radius):
	pi = 3.14
	volume = (4/3) * pi * radius * radius * radius
	return volume

radius1 = 1
volume1 = calculate_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {volume1}")

radius2 = 2
volume2 = calculate_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {volume2}")
