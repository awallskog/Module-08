"""
Author: Alicia Wallskog
Date: 10/12/24
File: finalProjectMod06.py
Github link: https://github.com/awallskog/Module-08.git


The purpose of this application is to assist customers with an easy online option for signing up for a gym membership through 
Forever Fit Health Club. This application will have a welcome page with information about the gym and its options for 
memberships and fees. The next page will allow the user to make decisions and sign up for different memberships: family, 
individual, and exercise classes. The user can total their payment by clicking on what applies to them and have their monthly or 
yearly payment displayed.

"""

from breezypythongui import EasyFrame
import tkinter as tk


# Other import statements
from tkinter import PhotoImage, messagebox
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
        font = Font(family = "Arial", size = 20, slant = "italic") 
        textLabel["font"] = font
        textLabel["foreground"] = "blue" 
        textLabel["background"] = "gray"

        # Add labels and buttons to window
        self.addEnterBtn = self.addButton(text = "Enter Here", row = 2, column = 0, columnspan = 4, command = self.openNewWindow) 


    # To open the new window.
    def openNewWindow(self):
        NewWindow(self)
        self.destroy()


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
        self.outputArea = self.addTextArea("", row = 10, column = 1, columnspan = 2, width = 50, height = 10)

        # Add buttons.
        self.totalButton = self.addButton(text = "Annual Total", row= 9, column = 1, columnspan = 2, command = self.total)
        self.backBtn = self.addButton(text = "Back", row = 11, column = 1, command = self.backScreen) 
        self.exitBtn = self.addButton(text = "Exit", row = 11, column = 2, command = lambda:quit())


    # Close first screen when opening second.
    def backScreen(self):
        self.destroy()
        SplashScreen()


    # Event handling method
    def total(self):   
        message = self.membType.getSelectedButton()["text"]
        if message == "Individual = $360 annually":
            membAmount = 360
        else:
            membAmount = 540
        message2 = self.classOption.getSelectedButton()["text"]
        if message2 == "All Classes = $120 annually":
            classAmount = 120
        else:
            classAmount = 0
        # Computes the annual total 
        totalAmount = membAmount + classAmount

        name = self.nameField.getText()
        address = self.addressField.getText()
        phone = self.phoneField.getText()

        # Add error box if all fields are not filled out.
        if not name or not address or not phone:
            messagebox.showerror("Input Error", "All fields must be filled.")

        """Append and validate the information and total 
        def validateInput(self):
            name = self.nameField.getText()
            if name != name.isalpha():
                print("Only enter letters for Name. No digits or special characters.")
            else:
                name = name
            #address = self.addressField.getText()
            #phone = self.phoneField.getText()
            if phone != phone.isnumeric():
                print("Only numbers for Phone Number. No letters or special characters.")
            else:
                phone = phone
        """
        
        memberInfo = name + "\n" + str(address) + "\n" + str(phone) + "\n" + "Total annual amount is $" + str(totalAmount)
    
        # Output the result while preserving the read-only status
        self.outputArea["state"] = "normal"
        self.outputArea.setText(memberInfo)
        self.outputArea["state"] = "disabled"


def main():
    SplashScreen().mainloop()


if __name__ == "__main__":
    main()

