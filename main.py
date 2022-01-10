#!/usr/bin/env python3

import string
import sys

def can_parse_int(s: str) -> bool:
    '''
    Returns true if s can be parsed into an int
    '''
    try:
        int(s)
        return True
    except:
        return False

def print_command_template() -> None:
    '''
    print out command usage
    '''
    print("ROTN [n; how much rotation; default 1] {text to be translated or name of file} [flag]")
    print("\tflags:")
    print("\t\t-f - input is a filename to translate; next word is file name")
    print("\t\t-o - Use an output file; next word is file name")

def parse_args(args: list) -> [int, str, str]:
    '''
    turn sys.argv into more usable information
    :args: list of arguments passed from the system
    :returns: [the key or how many spaces shifted, text or name of file to be shifted, true/false if reading from file, output file name]
    '''
    result = [1, '', '']
    _ = sys.argv.pop(0)
    o_flag = False
    f_flag = False
    first = True
    while len(sys.argv):
        match sys.argv.pop(0):
            case '-o':
                if o_flag:
                    print('Cannot have more than one o flag', file=sys.stderr)
                    exit(1)
                elif len(sys.argv) < 1:
                    o_flag = True
                    print('Expected argument FILENAME after o flag', file=sys.stderr)
                    exit(1)
                result[2] = sys.argv.pop(0)
            case '-f':
                if f_flag:
                    print('Cannot have more than one f flag', file=sys.stderr)
                    exit(1)
                elif len(sys.argv) < 1:
                    f_flag = True
                    print('Expected argument FILENAME after f flag', file=sys.stderr)
                    exit(1)
                result[1] = open(sys.argv.pop(0), 'r').read()
            case n if first and can_parse_int(n):
                first = False
                result[0] = int(n)
            case s if not f_flag:
                result[1] = f'{result[1]} {s}' if result[1] else s
    if not result[1]:
        result[1] = sys.stdin.read()
    return result


def shift_characters(n: int, inpt: str) -> str:
    '''
    the alpha characters in the string n characters to the right in the alphabet
    :n: number of spaces shifted
    :inpt: text to be shifted
    '''
    result = ""
    size = len(string.ascii_uppercase)
    for char in inpt:
        if char.isalpha():
            if char.isupper():
                result += string.ascii_uppercase[(string.ascii_uppercase.index(char) + n) % size]
            else:
                result += string.ascii_lowercase[(string.ascii_lowercase.index(char) + n) % size]
        else:
            result += char
    return result

def shift_input(n: int, inpt: str, output_file: str) -> None:
    '''
    shift text or input from file and print or put in file
    :n: number of spaces shifted
    :inpt: text to be shifted or path to file
    :output_file: name of file to write to
    '''
    shifted = shift_characters(n, inpt)
    if output_file == '':
        print(shifted)
    else:
        with open(output_file, 'w') as f:
            f.write(shifted)

def main():
    try:
        shift_input(*parse_args(sys.argv))
    except Exception as e:
        print("Error:", e, file=stderr)
        print_command_template()

if __name__ == "__main__":
    main()
