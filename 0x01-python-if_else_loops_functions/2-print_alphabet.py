#!/usr/bin/python3
alphabet = ""
for letter in range(ord('a'), ord('z') + 1):
    if letter != ord('q') and letter != ord('e'):
        alphabet += chr(letter)
print("{}".format(alphabet))
