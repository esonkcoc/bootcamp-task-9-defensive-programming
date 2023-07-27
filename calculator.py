# Consulted w3 Schools to learn how to create, write, open and read file in Python
file=open("calculations.txt", "w")

#I have employed while loop blocks throughout so the programme keeps commanding the user until they enter a valid input to proceed.
while True:
#If the user enters anything other than a numerical value, they will be met with an error message and prompted to try again until a valid input.
    try:
        Num1=float(input("Enter your first number:"))
        Num2=float(input("Enter your second number:"))
        break
    except ValueError:
        print("Invalid number. Try again.\n")

while True:
    Op=(input("\nEnter the operation (+,-,*,/,%) you'd like to perform on your two numbers:")) 
#If the user enters anything other than an arithmatical operator, they will be met with an error message and prompted to try again until a valid input. 
    if Op in ["+", "-", "*", "/", "%"]:
        break
    else:
        print("Invalid operation. Try again.\n")
    if Op=="+":
        calculation=Num1+Num2
    elif Op=="-":
        calculation=Num1-Num2
    elif Op=="*":
        calculation=Num1*Num2
    elif Op=="/":
        try:
#If the user tries to divide by 0, they will be met with an error message and prompted to divide by a number other than 0. 
            calculation=Num1/Num2
        except ZeroDivisionError:
            print("Error: Division by zero.")
            Num2=float(input("Enter another second number other than 0: "))
    elif Op=="%":
        calculation=Num1%Num2
 
calculation = eval(f"{Num1} {Op} {Num2}")        
# The method .write() writes the calculation and answer to the variable named ‘file’ which is assigned the value "calculations.txt", “w". /n Will start a new line for the next calculation and answer to be displayed neatly.
file.write(f"{Num1} {Op} {Num2} = {calculation}\n")
print(f"{Num1} {Op} {Num2} = {calculation}")

while True:
    next_step=input("\nEnter 'Calculate' if you want to continue calculating or 'Answers' to see all the calculations you've made so far:").lower()
    if next_step == "calculate":

        while True:
            try:
                Num1=float(input("\nEnter your first number:"))
                Num2=float(input("Enter your second number:"))
                break
            except ValueError:
                print("Invalid number. Try again.\n")

        while True:
            Op=(input("\nEnter the operation (+,-,*,/,%) you'd like to perform on your two numbers:"))
            if Op in ["+", "-", "*", "/", "%"]:
                break
            else:
                print("Invalid operation. Try again.\n")
            if Op=="+":
                calculation=Num1+Num2
            elif Op=="-":
                calculation=Num1-Num2  
            elif Op=="*":
                calculation=Num1*Num2
            elif Op=="/":
                try:
                    calculation=Num1/Num2
                except ZeroDivisionError:
                    print("Error: Division by zero.")
                    Num2=float(input("Enter another second number other than 0: "))
            elif Op=="%":
                calculation=Num1%Num2

        calculation = eval(f"{Num1} {Op} {Num2}")        
        file.write(f"{Num1} {Op} {Num2} = {calculation}\n")
        print(f"{Num1} {Op} {Num2} = {calculation}")
        
    elif next_step == "answers":

        while True:
            file_execute=input("\nEnter 'calculations.txt' to see all the calculations you've made so far:").lower()
            if file_execute == "calculations.txt":
                try:
                    with open(file_execute, "r") as file:
                        contents=file.read()
                        print (contents)
                        break
                except FileNotFoundError:
                    print("Invalid file name. Try again.\n")
            else:
                print("Invalid input. Please enter 'calculations.txt'.")
        break
    else:
        print("Invalid option. Try again.\n")

"""The above elif section was assisted by Chat GPT.
Originally I prompted the user to enter the name of the file they want to open and read from.
Their input was stored in the 'file_execute' variable.
I tired to use 'file.read(file_execute)' to open and read the file. 
Chat GPT informed me this wouldn't work because the .read() method takes a None argument or takes an interger argument that specifies the number of bytes to read from the file. It doesn't take a filename as an argument.
To read the contents of a file, I needed to open the file in read mode using the open() function, then call the .read() method on the file object.
By passing None through the .read() argument the entire contents of the file will be read. This value is stored as "contents" which is then outputted via print() 
ChatGPT recommended I open the file to be read via 'with' and 'as'. This would ensure the file is closed when finished reading."""

"""Traceback (most recent call last):
  File "/Users/abhi/hello/Task 9/calculator.py", line 74, in <module>
    calculation = eval(f"{Num1} {Op} {Num2}")        
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 1, in <module>
ZeroDivisionError: float division by zero"""