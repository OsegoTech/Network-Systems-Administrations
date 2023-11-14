def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

#main loop
while True:
    print("     CALCULATOR     ")
    num1 = (float(input("ENter the first number:")))
    num2 = (float(input("ENter the second number:")))
    print("1.Addition\n" "2.subtraction\n" "3.multiplication\n" "4.division\n" "5.exit\n")
    choice=(str(input("choose operation (use 1/2/3/4/5):")))
    
    if choice == '5':
        break
    if choice == '1':
        print("result" , add(num1,num2))
    if choice == '2':
        print("result" , subtract(num1,num2))
    if choice == '3':
        print("result" , multiply(num1,num2))
    if choice == '4':
        print("result" , divide(num1,num2))