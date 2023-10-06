def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A, Addition")
    print("B, Substarction")
    print("C, Multiple")
    print("D, Divition")
    print("E, Exit")

    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Input First Number: "))
        b = int(input("Enter Second Number: "))
        add(a,b)
    elif choice == "b" or choice == "B":
        print("Subscration")
        a = int(input("Input First Number: "))
        b = int(input("Enter Second Number: "))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multiple")
        a = int(input("Input First Number: "))
        b = int(input("Enter Second Number: "))
        mul(a,b)
    elif choice == "d" or choice == "D":
        print("Divition")
        a = int(input("Input First Number: "))
        b = int(input("Enter Second Number: "))
        div(a,b)
    elif choice == "e" or choice == "E":
        print("program ended")
        quit()