def exception():
    try:
        x = int(input("x is: "))
        y = int(input("y is: "))
        print("The value is:", x / y)
    except ZeroDivisionError:
        print("Divide by zero exception")
    finally:
        print("Byee")

exception()
