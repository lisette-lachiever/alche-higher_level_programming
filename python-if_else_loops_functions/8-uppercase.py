#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) not in range(65, 91):
            letter = (chr(ord(letter) - 32) if ord(letter) != 32 and ord(letter) != 44 else letter)
            print("{}".format(letter), end="")
        elif ord(letter) in range(65, 91):
            print("{}".format(letter), end="")
