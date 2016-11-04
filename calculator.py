import operator
#Import founction operator
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
#List of usefull operators for calculator
def result(num1, num2, operator):
    return operations[operator](num1, num2)
#Choosing the operator from the list and performs the calculation,
#is returning results
if __name__ == '__main__':
    operator_string = ', '.join(operations)
    while True:
        try:
            number1 = int(input("Enter the first number (or a letter to exit): "))
            #Import first numer
        except:
            break
            #If not a number - close program
        try:
            number2 = int(input("Enter the second number: "))
            #Import second numer
        except:
            print("That is not a number!")
            continue
            #If not a number - repeat program
        operator = input("Enter an operation: ")
        #Import operation
        try:
            print(result(number1, number2, operator))
            #Print result - if bad operation, print error and repeat program
        except:
            print("Invalid operation!")
