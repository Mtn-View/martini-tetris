import random

# REMEMBER
# DIMENSIONS ARE INVERTED
square = [
	[1, 1],
	[1, 1]
]

line = [
	[1],
	[1],
	[1],
	[1]
]
left_l = [
	[1, 0],
	[1, 0],
	[1, 1]
]

right_l = [
	[0, 1],
	[0, 1],
	[1, 1]
]

left_z = [
	[1, 1, 0],
	[0, 1, 1]
]

right_z = [
	[0, 1, 1],
	[1, 1, 0]
]

t_block = [
	[1, 1, 1],
	[0, 1, 0]
]


blocks = [square, line, left_l, right_l, left_z, right_z, t_block]

def get_random_block():
	return random.choice(blocks)
	# return random.choice([left_l, right_l])
