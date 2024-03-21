# Defining class to store all features involved within the button
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		# Image to rendered
		self.image = image
		# Positioning
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		# Font
		self.font = font
		# Base font colour and hovering colour
		self.base_color, self.hovering_color = base_color, hovering_color
		# text Rendering
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		# Will not render any image if image is set to None
		if self.image is None:
			self.image = self.text
		# Setting position of the button
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	# Function to not render any image if image is set to None
	def update(self, screen):
		if self.image is not None:
			# Rendering image onto screen
			screen.blit(self.image, self.rect)
		# Rendering text onto screen
		screen.blit(self.text, self.text_rect)

	# Function to detect any input on the button
	def checkForInput(self, position):
		# If mouse position is in the range of the area of the button, return True
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		# If no positioning is detected, return false
		return False

	# Function to change colour of text if hovering over button
	def changeColor(self, position):
		# If mouse position is in the range of the area of the button, change the colour of text to hovering colour
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		# If no positioning is detected, keep text colour to base colour
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)