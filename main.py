import string
import sys

def print_command_template() -> None:
    print("ROTN {n; how much rotation} {text to be translated or name of file} [flag]")
    print("\tflags:")
    print("\t\t-f - input is a filename to translate; next word is file name")
    print("\t\t-o - Use an output file; next word is file name")

def parse_args(args: list) -> (int, bool, str):
    try:
        if read_from_file := '-f' in args:
            args.remove('-f')
        _ = args.pop(0)
        print(_)
        if len(args) > 2:
        return int(args[0]), read_from_file, args[1],
    except Exception as e:
        print("Error: " + e)

def main():
    print(parse_args(sys.argv))

if __name__ == "__main__":
    main()
