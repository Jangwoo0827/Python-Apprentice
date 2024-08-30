"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
num1 = simpledialog.askinteger("Num1", "Give me a number.") 
# Ask the user for the second number
num2 = simpledialog.askinteger("Num2", "Give me another number.") 
# Ask the user for the math operation
num3 = simpledialog.askstring("Operation", "Choose one. Multiply, Divide, Add, or Subtract") 
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if num3 == "Multiply":
   num4 = num1 * num2
   messagebox.showinfo("Num4", num4)
elif num3 == "Divide":
   num4 = num1/num2
   messagebox.showinfo("Num4", num4)
elif num3 == "Add":
   num4 = num1 + num2
   messagebox.showinfo("Num4", num4)
elif num3 == "Subtract":
   num4 = num1 - num2
   messagebox.showinfo("Num4", num4)
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
else:
   messagebox.showerror("Nooooooooooooo", "YOU CAN'T USE THIS OPERATION!!")
# Keep the window open
window.mainloop()