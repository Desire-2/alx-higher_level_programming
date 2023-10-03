#!/usr/bin/python3
output = ""
for letter in range(ord('a'), ord('z') + 1):
    if letter != ord('q') and letter != ord('e'):
        output += chr(letter)
print(output)
