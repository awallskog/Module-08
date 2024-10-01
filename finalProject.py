"""
Author: Alicia Wallskog
Date: 09/30/24
File: finalProjectMod06.py
Github link: https://github.com/awallskog/SDEV-140.git


The purpose of this application is to assist customers with an easy online option for signing up for a gym membership through 
Forever Fit Health Club. This application will have a welcome page with information about the gym and its options for 
memberships and fees. The next page will allow the user to make decisions and sign up for different memberships: family, 
individual, and exercise classes. The user can total their payment by clicking on what applies to them and have their monthly or 
yearly payment displayed.

"""

from breezypythongui import EasyFrame

# Other import statements
from tkinter import PhotoImage
from tkinter.font import Font

class SplashScreen(EasyFrame):
    # Displays splash screen
    def __init__(self):
        EasyFrame.__init__(self, "Forever Fit Health Club")
        self.setResizable(True)
        imageLabel = self.addLabel(text = "", row = 0, column = 1, sticky = "NSEW")
        imageLabel2 = self.addLabel(text = "", row = 0, column = 2, sticky ="NSEW")
        textLabel = self.addLabel(text = "Welcome to Forever Fit Health Club", row = 1, column = 1, columnspan = 2, sticky = "NSEW")

        # Load images and associate them with the image label
        self.image = PhotoImage(file = "meghan-holmes-3.gif")
        imageLabel["image"] = self.image
        self.image2 = PhotoImage(file = "victor-freitas-2.gif")
        imageLabel2["image"] = self.image2

        # Set font and color - this is for the caption
        font = Font(family = "Arial", size = 20, slant = "italic") # other option is roman
        textLabel["font"] = font
        textLabel["foreground"] = "blue" # More colors in decimal or hex
        textLabel["background"] = "gray"

        # Add labels and buttons to window
        self.addEnterBtn = self.addButton(text = "Enter Here", row = 2, column = 0, columnspan = 4)


def main():
    SplashScreen().mainloop()
if __name__ == "__main__":
    main()

