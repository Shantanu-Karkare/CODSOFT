#Task 1:-
#Design a simple calculator with basic arithmetic Operations.
print("\"Simple Calculator\"")
print("----------------------")
#Take user input
num1=float(input("Enter the First number:"))
num2=float(input("Enter the Second Number:"))
#operation choice!!
print("Choose an option:")
print("1-Addition (+)")
print("2-Subtraction (-)")
print("3-Multiplication (X)")
print("4-Division (/)")
choice=int(input("Enter your choice(1/2/3/4):"))
#Perform the calculation
if choice==1:
    Addition=num1 + num2
    print(f"Addition: {num1} + {num2} = {Addition}")
elif choice==2:
     Subtraction=num1 - num2
     print(f"Subtraction: {num1} - {num2} = {Subtraction}")
elif choice==3:
     Multiplication=num1 * num2
     print(f"Multiplication: {num1} X {num2} = {Multiplication}")
elif choice ==4:
     Division=num1/num2
     print(f"Division: {num1} / {num2} = {Division}")
else:
     print("Invalid choice,Please select 1,2,3 or 4") 