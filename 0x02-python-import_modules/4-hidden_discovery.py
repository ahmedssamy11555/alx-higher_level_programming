#!/usr/bin/python3
import dis

def main():
    with open("hidden_4.pyc", 'rb') as file:
        pyc_magic_number  = file.read(4)
        if pyc_magic_number != b'\x03\xf3\r\n':
            print("Invalid magic number. Not a valid .pyc file.")
            return
        file.read(4)
        code_object = compile(file.read(), '<pyc_file>', 'exec')
        dis.dis(code_object)

if __name__ == "__main__":
    main()