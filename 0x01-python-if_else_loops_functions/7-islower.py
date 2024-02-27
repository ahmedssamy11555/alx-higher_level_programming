#!/usr/bin/python3
def islower(c):
    if ord('a') >= ord(c) <= ord('z'):
        return True
    if ord('A') >= ord(c) <= ord('Z'):
        return False
