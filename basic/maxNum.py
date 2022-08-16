num1=int(input("Enter the Number1 Value:"))
num2=int(input("Enter the Number2 Value:"))
num3=int(input("Enter the Number3 Value:"))

if num1>num2 and num1>num3:
    print("Max Number:",num1)

elif num2>num1 and num2>num3:
    print("Max Number:",num2)
else:
    print("Max Number:",num3)