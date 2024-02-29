#!/usr/bin/python3
lower = ""
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        lower += chr(i)
    else:
        lower += chr(i).upper()
print("{}".format(lower), end="")
