import time
import board
import displayio
from adafruit_matrixportal.matrixportal import MatrixPortal
from blocks import get_random_block
from colors import get_random_color


matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=True)

# Create a new displayio Group
group = displayio.Group()
import time
import board
import displayio
from adafruit_matrixportal.matrixportal import MatrixPortal
from blocks import get_random_block
from colors import get_random_color, colors
import random

width = 128

matrixportal = MatrixPortal(width=width, status_neopixel=board.NEOPIXEL, debug=True)

# Create a new displayio Group
group = displayio.Group()

# Create a new Bitmap object
bitmap = displayio.Bitmap(matrixportal.display.width, matrixportal.display.height, 6)

# Create a new Palette object with a single color
palette = displayio.Palette(6)
palette[0] = 0x000000  # Black
palette[1] = colors[1]
palette[2] = colors[2]
palette[3] = colors[3]
palette[4] = colors[4]
palette[5] = colors[5]

# Create a new TileGrid object using the Bitmap and Palette objects
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Add the TileGrid to the Group
group.append(tile_grid)

# Define the tetris block
tetris_block = get_random_block()
print(tetris_block)

# Define the starting position of the tetris block
tetris_x = 32
tetris_y = 0

# Define the speed of the tetris block
tetris_speed = 1

# Define the size of the tetris block
tetris_size = len(tetris_block[0])

color = random.randint(1, len(colors))

# Define the function to draw the tetris block
def draw_tetris_block(block):
	for x in range(len(block)):
		for y in range(len(block[0])):
			if block[x][y] == 1:
				bitmap[tetris_x + x, tetris_y + y] = color

# Define the function to erase the tetris block
def erase_tetris_block(block):
	for x in range(len(block)):
		for y in range(len(block[0])):
			if block[x][y] == 1:
				bitmap[tetris_x + x, tetris_y + y] = 0

# Draw the initial tetris block
draw_tetris_block(tetris_block)

# Add the Group to the display
matrixportal.display.show(group)

hit_bottom = False
hit_block = False
# Define the main loop
while True:
	# Erase the current tetris block
	if not hit_block and not hit_bottom:
		print("erase at ", tetris_y)
		erase_tetris_block(tetris_block)

	# Move the tetris block down
	tetris_y += tetris_speed

	hit_bottom = tetris_y + tetris_size > matrixportal.display.height
	hit_block = False

	# Check if the tetris block has hit another block
	if not hit_bottom:
		for x in range(len(tetris_block)):
			if tetris_block[x][tetris_size-1] == 1:
				if bitmap[tetris_x + x, tetris_y + tetris_size-1] != 0:
					hit_block = True
	if hit_bottom:
		print("hit bottom at", tetris_y)
	if hit_block:
		print("hit block at", tetris_y)

	if hit_block or hit_bottom:
		# Reset the tetris block to the top
		tetris_y = 0
		tetris_x = random.randint(0, 124)
		# New block
		tetris_block = get_random_block()
		tetris_size = len(tetris_block[0])
		color = random.randint(1, len(colors))

	# Draw the updated tetris block
	draw_tetris_block(tetris_block)
	print("draw at ", tetris_y)

	# Wait for a short time
	time.sleep(0.2)

# Create a new Bitmap object
bitmap = displayio.Bitmap(128, matrixportal.display.height, 1)

# Create a new Palette object with a single color
palette = displayio.Palette(2)
palette[0] = 0x000000  # Black
palette[1] = get_random_color()  # Block

# Create a new TileGrid object using the Bitmap and Palette objects
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Add the TileGrid to the Group
group.append(tile_grid)

# Define the tetris block
tetris_block = get_random_block()
print(tetris_block)

# Define the starting position of the tetris block
tetris_x = 32
tetris_y = 0

# Define the speed of the tetris block
tetris_speed = 1

# Define the size of the tetris block
tetris_size = len(tetris_block[0])

# Define the color of the tetris block
tetris_color = 0xFFFFFF

# Define the function to draw the tetris block
def draw_tetris_block(block):
	for x in range(len(block)):
		for y in range(len(block[0])):
			if block[x][y] == 1:
				color = 1 if tetris_color else 0
				bitmap[tetris_x + x, tetris_y + y] = color

# Define the function to erase the tetris block
def erase_tetris_block(block):
	for x in range(len(block)):
		for y in range(len(block[0])):
			if block[x][y] == 1:
				bitmap[tetris_x + x, tetris_y + y] = 0

# Draw the initial tetris block
draw_tetris_block(tetris_block)

# Add the Group to the display
matrixportal.display.show(group)

# Define the main loop
while True:
	# Erase the current tetris block
	erase_tetris_block(tetris_block)

	# Move the tetris block down
	tetris_y += tetris_speed

	# Check if the tetris block has reached the bottom
	if tetris_y + tetris_size > matrixportal.display.height:
		# Reset the tetris block to the top
		tetris_y = 0
		# New block
		tetris_block = get_random_block()
		tetris_size=len(tetris_block[0])
		palette[1] = get_random_color()  # Block

	# Draw the updated tetris block
	draw_tetris_block(tetris_block)

	# Wait for a short time
	time.sleep(0.1)
