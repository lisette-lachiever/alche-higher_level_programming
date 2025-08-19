#!/usr/bin/python3
for number in range(90):
    if number//10 < number % 10:
        print("{}{}".format(number//10, number % 10), end="")
        if number!= 89:
            print(", ", end="")
print("")
