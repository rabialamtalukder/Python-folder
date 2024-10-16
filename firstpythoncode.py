while(True):
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    print("======================")

    print("1) + Adition")
    print("2) - Sub")
    print("3) * Multiplication")
    print("4) / Division")
    print("5) X Exit")


    print("======================")
    z = int (input("Enter the 1, 2, 3 or 4 : "))

    if (z == 1):
        print(x + y)
    elif (z == 2):
        print(x - y)
    elif(z == 3):
        print(x*y)
    elif (z == 4):
        print(x / y)
    elif (z == 5):
        break
    else:
        print("Please, enter correct function!!!!!")

