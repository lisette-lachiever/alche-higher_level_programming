#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add sub mul div 
    a = 10
    b = 5
    operation = input("Enter operation(*,/,-,+): ")

    if operation == "+":
        print("{} {} {} = {}" .format(a, operation, b, add(a, b)))
    elif operation == "-":
        print("{} {} {} = {}" .format(a, operation, b, sub(a, b)))
    elif operation == "*":
        print("{} {} {} = {}" .format(a, operation, b, mul(a, b)))
    elif operation == "/":
        print("{} {} {} = {}" .format(a, operation, b, div(a, b)))
