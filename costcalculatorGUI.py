"""
Program: costcalculatorGUI.py, final project of Python.
Author: Md Suhel Rana 06/15/2022

GUI-based calculator which will allow the user to enter in the cost of an item and also the quantity (amount) of that item being purchased and then output the total cost.
*** The file "breezypythongui.py" must be in the same directory.
*** Need image file: "table.png" in the same directory
*** Need sound file: "click.wav" too in the same directory
*** import pygame, PhotoImage and Font form tkinter and import math to run this App. Thank you! 
"""

from breezypythongui import EasyFrame
import pygame
from tkinter import PhotoImage
from tkinter.font import Font
import math

class CostCalculator(EasyFrame):
	"""Calculates and displays the total cost of an item and quantity."""
	# definition of the __init__() method which is our class constructor
	def __init__(self):
		"""Sets up the window and widgets."""
		EasyFrame.__init__(self, title = "Cost calculator", background = "#9ec2e6", width = 600, height = 700, resizable = False)
		
		# Creating Image logo object and load.
		self.imageLogo = self.addLabel(text = "", row = 0, column = 0, sticky = "NEWS", background = "#9ec2e6", columnspan = 2)
		self.image = PhotoImage(file = "table1.png")
		self.imageLogo["image"] = self.image
		self.imageLogo["height"] = 300


		# Creating and designing the titles
		titleFont = Font(family = "Impact", size = 40, weight = "bold")
		self.addLabel(text = "MDWebDesignLLC.com", row = 1, column = 0, background = "#9ec2e6", sticky = "NEWS", font = titleFont, foreground = "white", columnspan = 2) 
		costFont = Font(family = "Verdana", size = 25, weight = "bold")
		self.addLabel(text = "Cost Calculator", row = 2, column = 0, background = "#9ec2e6", sticky = "NEWS", font = costFont, columnspan = 2, foreground = "green") 

		# Label and input fields		
		labelFont = Font(family = "Verdana", size = 16)
		self.addLabel(text = "Cost per service,   $:", row = 3, column = 0, font = labelFont, background = "#9ec2e6", sticky= "NE")
		self.inputCost = self.addFloatField(value = 0.0, row = 3, column = 1)
		self.addLabel(text = "Quantity:", row = 4, column = 0, font = labelFont, background = "#9ec2e6", sticky = "NE")
		self.quantity = self.addIntegerField(value = 0, row = 4, column = 1)
		self.quantity["width"] = 20

		# Calculate button
		self.button = self.addButton(text = "Calculate", row = 5, column = 0, columnspan = 2, command = self.calculate)
		# button does not have background or size in upper line, do it like it below
		self.button["background"] = "yellow" 
		self.button["width"] = 16
		self.button["font"] = "Impact"
		self.button["foreground"] = "blue"
		self.button.bind("<Return>", lambda event: self.calculate())

		# Label and output field
		self.addLabel(text = "The total for this order is,   $:", row = 6, column = 0, background = "#9ec2e6", font = labelFont, sticky = "NE")	
		self.outputTotal = self.addFloatField(value = 0.0, row = 6, column = 1, precision = 2, state = "readonly")

		self.addLabel(text= "Thank you, see you again soon!", row = 7, column = 0, font = labelFont, foreground = "green", sticky = "NEWS", background = "#9ec2e6", columnspan = 2)
		self.addLabel(text = "", row = 8, column = 0, background = "#9ec2e6")

		# Event handling method for the button
	def calculate(self):
		# Adding sound effect
		pygame.mixer.init()
		pygame.mixer.music.load("click.wav")
		pygame.mixer.music.play()

		# Compute through calculate button and transfer it to totalCost as output.
		cost = self.inputCost.getNumber()
		orderNumber = self.quantity.getNumber()
		totalCost = cost * orderNumber
		self.outputTotal.setNumber(totalCost)	

# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	CostCalculator().mainloop()

# global call to the main() method
main()
