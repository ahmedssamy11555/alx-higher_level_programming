#!/usr/bin/python3
def uppercase(str):
    length = 0
    for _ in str:
        length+=1
    result= ""
    for charIndex in range(length):
        if ord('a') <= ord(str[charIndex]) <= ord('z'):
            result += chr(ord(str[charIndex]) - 32 )
        else:
            result += str[charIndex]

    print('{}'.format(result))
    