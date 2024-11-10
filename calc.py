print()
print("            THE SIMPLE CALCULATOR")
print()

num1 = int(input("Enter first number here....?"))
print("+")
print("-")
print("*")
print("/")
calc = input("Operator here....?")
num2 = int(input("Enter second number here....?"))
print()

if calc == "+":
   print(num1, calc, num2, "= ", num1 + num2)
elif calc == "-":
   print(num1, calc, num2, "= ", num1 - num2)
elif calc == "*":
    print(num1, calc, num2, "= ", num1 * num2)
elif calc == "/":
     print(num1, calc, num2, "= ", num1 / num2)
else:
    print("unsupported operator")