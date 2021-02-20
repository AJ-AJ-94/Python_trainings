x = range(1, 50)

def divisorGenerator():
    num = input("Choose the number: ")
    for elem in x:
        if int(num) % elem == 0:
            print("divisor: ", elem)
    exit()

print(divisorGenerator())
