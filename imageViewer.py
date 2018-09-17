# imports EasyFrame from breezypythongui folder
from breezypythongui import EasyFrame
# imports PhotoImage from tkinter
from tkinter import PhotoImage

#sets up the programs class with EasyFrame as the argument
class ImageViewer(EasyFrame):
	"""Application with three images that appear and dissapear on click"""
	#main shell for the window
	def __init__(self):
		"""Sets up the window and widgets."""
		#Main Title of application
		EasyFrame.__init__(self, title = "Image Viewer 1.0")
		#Adds a label inside app 
		self.addLabel(text = "Image Viewer 1.0", row = 0, column = 2)
		#Adds a blank label which will hold an image
		self.imageLabel = self.addLabel(text = "", row = 2, column = 0,)
		#Button that when clicked runs the firstImage function 
		self.addButton(text = "click", row = 4, column = 0, command = self.firstImage)
		#Adds a blank label which will hold an image
		self.imageLabel2 = self.addLabel(text = "", row = 2, column = 2)
		#Button that when clicked runs the secondImage function 
		self.addButton(text = "click", row = 4, column = 2, command = self.secondImage)
		#Blank label which will hold an image
		self.imageLabel3 = self.addLabel(text = "", row = 2, column = 4)
		#Button that when clicked runs the thirdImage function
		self.addButton(text = "click", row = 4, column = 4, command = self.thirdImage)
		
	#Event handling method for the first button
	def firstImage(self):
		"""Method which adds the image to imageLabel"""
		#if imageLabel text is empty, this variable holds gif image
		if self.imageLabel["text"] == "":
			#if the text is blank, this establishes a Variable that holds gif image
			self.image = PhotoImage(file = "image1.gif")
			#Adds the file image to blank imageLabel
			self.imageLabel["image"] = self.image
			#Changes the text field from empty to a string which now makes the if statement false
			self.imageLabel["text"] = "HTML"
			#Sets the state of the imageLabel to normal
			self.imageLabel["state"] = "normal"
		#The else to the methods if statement
		else:
			#Sets the image back to blank which removes the image
			self.imageLabel["image"] = ""
			#Sets the text back to an empty string so the if statement is now true
			self.imageLabel["text"] = ""
			#Sets the state of the imageLabel to disabled
			self.imageLabel["state"] = "disabled"
	#Event handling method for the second button
	def secondImage(self):
		"""Method which adds the image to imageLabel2"""
		#if statement that tests if the text within the imageLabel2 is empty
		if self.imageLabel2["text"] == "":
			#if imageLabel2 text is empty, this variable holds gif image
			self.image2 = PhotoImage(file = "image2.gif")
			#Adds the file image to blank imageLabel2
			self.imageLabel2["image"] = self.image2
			#Changes the text field from empty to a string which now makes the if statement false
			self.imageLabel2["text"] = "JAVASCRIPT"
			#Sets the state of the imageLabel to normal
			self.imageLabel2["state"] = "normal"
		#The else to the methods if statement
		else:
			#Sets the image back to blank which removes the image
			self.imageLabel2["image"] = ""
			#Sets the text back to an empty string so the if statement is now true
			self.imageLabel2["text"] = ""
			#Sets the state of the imageLabel2 to disabled
			self.imageLabel2["state"] = "disabled"
			
		#Event handling method for the third button	
	def thirdImage(self):
		"""Method which adds the image to imageLabel3"""
		#if statement that tests if the text within the imageLabel2 is empty
		if self.imageLabel3["text"] == "":
			#if imageLabel3 text is empty, this variable holds gif image
			self.image3 = PhotoImage(file = "image3.gif")
			#Adds the file image to blank imageLabel3
			self.imageLabel3["image"] = self.image3
			#Changes the text field from empty to a string which now makes the if statement false
			self.imageLabel3["text"] = "CSS"
			#Sets the state of the imageLabel3 to disabled
			self.imageLabel3["state"] = "normal"
		#The else to the methods if statement
		else:
			#Sets the image back to blank which removes the image
			self.imageLabel3["image"] = ""
			#Sets the text back to an empty string so the if statement is now true
			self.imageLabel3["text"] = ""
			#Sets the state of the imageLabel3 to disabled
			self.imageLabel3["state"] = "disabled"
#the main method which executes program		
def main():
	"""Main method that executes program"""
	#The call to the programs class
	ImageViewer().mainloop()
#The call to the main method
main()