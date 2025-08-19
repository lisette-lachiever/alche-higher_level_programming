#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) not in range(65, 91):
            if ord(letter)!= 32 and ord(letter)!= 44:
                letter = chr(ord(letter) - 32)
            print("{}".format(letter), end="")
        elif ord(letter) in range(65, 91):
            print("{}".format(letter), end="")
