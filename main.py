import string
import sys

def print_command_template() -> None:
    """
    print out command usage
    """
    print("ROTN [n; how much rotation; default 1] {text to be translated or name of file} [flag]")
    print("\tflags:")
    print("\t\t-f - input is a filename to translate; next word is file name")
    print("\t\t-o - Use an output file; next word is file name")

def parse_args(args: list) -> [int, str, bool, str]:
    """
    turn sys.argv into more usable information
    :args: list of arguments passed from the system
    :returns: [the key or how many spaces shifted, text or name of file to be shifted, true/false if reading from file, output file name]
    """
    result = []
    output_file = ""
    read_from_file = False
    next_arg_is_output_file = False
    _ = args.pop(0)
    for arg in args:
        if arg == '-o':
            next_arg_is_output_file = True
        elif arg == '-f':
            read_from_file = True
        elif next_arg_is_output_file:
            output_file = arg
        else:
            result.append(arg)
    if len(result) == 1:
        result = [1] + result
    else:
        try:
            result[0] = int(result[0])
        except:
            raise SyntaxError("Not enough args")
    result += [read_from_file, output_file]
    if len(result) > 4:
        raise SyntaxError("Too many args")
    elif len(result) < 4:
        raise SyntaxError("Not enough args")
    return result

def shift_characters(n: int, inpt: str) -> str:
    """
    the alpha characters in the string n characters to the right in the alphabet
    :n: number of spaces shifted
    :inpt: text to be shifted
    """
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

def shift_input(n: int, inpt: str, read_from_file: bool, output_file: str) -> None:
    """
    shift text or input from file and print or put in file
    :n: number of spaces shifted
    :inpt: text to be shifted or path to file
    :read_from_file: true/false if reading from file
    :output_file: name of file to write to
    """
    if read_from_file:
        with open(inpt) as f:
            content = f.read()
    else:
        content = inpt
    shifted = shift_characters(n, content)
    if output_file == "":
        print(shifted)
    else:
        with open(output_file, 'w') as f:
            f.write(shifted)

def main():
    try:
        n, inpt, read_from_file, output_file = parse_args(sys.argv)
        shift_input(n, inpt, read_from_file, output_file)
    except Exception as e:
        print("Error:", e)
        print_command_template()

if __name__ == "__main__":
    main()
