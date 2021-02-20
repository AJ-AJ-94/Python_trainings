num = input("Choose the number: ")
check = input("Choose the number to divide by: ")

if int(num) % int(check) == 0:
    print("The number can be divide.")
    if int(num) % 2 == 0:
        print("The number is also even.")
else:
    print("The number is odd.")