x = int(input("Enter the first number: "))
y= int(input("Enter the second number: "))

print("======================")

print("1) + Adition")
print("2) - Sub")
print("3) * Multiplication")
print("4) / Division")


print("======================")
z= int (input("Enter the 1, 2, 3 or 4 : "))

if (z == 1):
    print(x + y)
elif (z == 2):
    print(x - y)
elif (z == 4):
    print(x / y)
else:
    print(x*y)