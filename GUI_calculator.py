from tkinter import *

# Class for the calculator
class Calculator:
    # Create __init__ 
    def __init__(self, master):
        # Method that initializes the object's attributes

        # Assign reference to the main window of the application
        self.master = master

        # Application name 
        master.title("Python Calculator")

        # Create line to see the equation 
        self.equation = Entry(master, width=24, borderwidth=5, font=('Arial', 12))

        # Assign the position for the equation line in the main application window
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Execute .addButton in main window
        self.createButton()








        


    
    def createButton(self):
        # Method that create the button

        # Buttons list:
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton('+')
        b_sub = self.addButton('-')
        b_mul = self.addButton('*')
        b_div = self.addButton('/')
        b_clr = self.addButton('c')
        b_eq = self.addButton('=')

        # Button arranged in rows
        row1 = [b7, b8, b9, b_add]
        row2 = [b4, b5, b6, b_sub]
        row3 = [b1, b2, b3, b_mul]
        row4 = [b_clr, b0, b_eq, b_div]



        # Arranged in the main window 
        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for b in row:
                b.grid(row=r, column=c, columnspan=1, padx=2, pady=2)
                c += 1
            r += 1






            
    
    # Define addButton
    def addButton(self, value):
        # Method that add the button to the main screen of the application

        return Button(
            self.master,
            text=value,
            width=6,  # Compact width for the buttons
            height=2,  # Compact height for the buttons
            font=('Arial', 12),  # Smaller font size
            command=lambda: self.clickButton(str(value)),
        )
    










    def clickButton(self, value):
        # Method to activate the buttons on the main screen/window in the application

        # Get the equation of the user input 
        current_equation = str(self.equation.get())

        # If user input
        if value == "c":
            self.equation.delete(0, END)
        
        elif value == "=":
            try:
                answer = str(eval(current_equation))
                self.equation.delete(0, END)
                self.equation.insert(0, answer)
            except:
                self.equation.delete(0, END)
                self.equation.insert(0, "Error")
        else:
            self.equation.delete(0, END)
            self.equation.insert(0, current_equation + value)









if __name__ == '__main__':
    # Create the main window of an application
    root = Tk()
    
    # Tell our calculator class to use this window
    my_gui = Calculator(root)
    
    # Executable loop on the application, waits for user input
    root.mainloop()
