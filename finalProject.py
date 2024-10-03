"""
Author: Alicia Wallskog
Date: 09/30/24
File: finalProjectMod06.py
Github link: https://github.com/awallskog/Module-08.git


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
        self.addEnterBtn = self.addButton(text = "Enter Here", row = 2, column = 0, columnspan = 4, command = self.openNewWindow)

    def openNewWindow(self):
        NewWindow(self)

class NewWindow(EasyFrame):
    # Displays the sign up window
    def __init__(self, master):
        EasyFrame.__init__(self, "Forever Fit Health Club--membership sign up")
        self.setResizable(True)
        imageLabel3 = self.addLabel(text = "", row = 0, column = 1, columnspan = 2, sticky = "NSEW")
        textLabel = self.addLabel(text = "Sign up for your membership today!", row = 1, column = 1, columnspan = 2, sticky = "NSEW")

        # Load images and associate them with the image label
        self.image3 = PhotoImage(file = "danielle-cerullo-3.gif")
        imageLabel3["image"] = self.image3

        # Set font and color - this is for the caption
        font = Font(family = "Arial", size = 20, slant = "italic") 
        textLabel["font"] = font
        textLabel["foreground"] = "blue" 
        textLabel["background"] = "gray"

        # Add the label, button group, and buttons for membership options
        self.addLabel(text = "Type of Membership", row = 2, column = 1)
        self.membType = self.addRadiobuttonGroup(row = 3, column = 1, rowspan = 2)
        defaultRB = self.membType.addRadiobutton(text = "Individual = $360 annually")
        self.membType.setSelectedButton(defaultRB)
        self.membType.addRadiobutton(text = "Family = $540 annually")
        # Add the label, button group, and buttons for exercise class selection
        self.addLabel(text = "Exercise Class", row = 2, column = 2)
        self.classOption = self.addRadiobuttonGroup(row = 3, column = 2, rowspan = 2)
        defaultRB = self.classOption.addRadiobutton(text = "All Classes = $120 annually")
        self.classOption.setSelectedButton(defaultRB)
        self.classOption.addRadiobutton(text = "No Thanks")

        # Label and field for the input
        self.addLabel(text = "Name", row = 6, column = 1)
        self.addLabel (text = "Address", row = 7, column = 1)
        self.addLabel(text = "Phone Number", row = 8, column = 1)
        self.nameField = self.addTextField(text = "", row = 6, column = 2)
        self.addressField = self.addTextField(text = "", row = 7, column = 2)
        self.phoneField = self.addTextField(text = "", row = 8, column = 2)

        self.totalButton = self.addButton(text = "Annual Total", row= 9, column = 1, command = self.total)

    def total(self):   #Event handling method
        message = self.membType.getSelectedButton()["text"]
        if message == "Individual = $360 annually":
            membAmount = 360
        else:
            membAmount = 540
        print(membAmount)
        message2 = self.classOption.getSelectedButton()["text"]
        if message2 == "All Classes = $120 annually":
            classAmount = 120
        else:
            classAmount = 0
        print(classAmount)
        totalAmount = membAmount + classAmount
        print(totalAmount)
        # Computes the annual total 
        # Obtain and validate the inputs
        #signUp = input("Would you like to sign up for a membership? Enter Y for yes or N to exit the program -->")
        #while signUp != "N":
            #memberCodeType = input("Enter type of member - I for individual or F for family -->")
            #classOption = input("Would you like to enroll in classes? Enter Y for yes or N for no.-->")
        #if memberCodeType == 'I':
            #dues = 360
            #memberType = "an individual"
        #else:
            #dues = 540
            #memberType = "a family"
        #if classOption == 'Y':
            #dues = dues + 120
        #print()
        #print(signUp + " is " + memberType + " whose dues are $%4d " % dues)
        #print()
        #signUp = input("Would you like to sign up for a membership? Enter Y for yes or N to exit the program -->")
        #print("Program ended.")
        #print()

        #total = self.membType + self.classOption
        #print(total) 


def main():
    SplashScreen().mainloop()
if __name__ == "__main__":
    main()

