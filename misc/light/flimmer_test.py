import random

def add_random_range(x, add = 30, wheel = 256):

	random.seed(42)

	if bool(random.getrandbits(1)):

		x = x + random.randint(0,30)

	else:

		x = x - random.randint(0,30)

	x = x % wheel

	return(x)

def flimmer(color):

	color2 = [0,0,0]

	for i in range(3):

		color2[i] = add_random_range(color[i])

	return(color2)

color1 = [0,0,256]

color2 = flimmer(color1)

print(color1)
print(color2)