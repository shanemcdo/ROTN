import string
import sys

def print_command_template() -> None:
    print("ROTN {n; how much rotation} {text to be translated or name of file} [flag]")
    print("\tflags:")
    print("\t\t-f - input is a filename to translate; next word is file name")
    print("\t\t-o - Use an output file; next word is file name")

def parse_args(args: list) -> [int, str, bool, str]:
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
    result += [read_from_file, output_file]
    # if len(result) > 4:
    #     raise "Too many args"
    # elif len(result) < 4:
    #     raise "Not enough args"
    return result

def main():
    try:
        print(parse_args(sys.argv))
    except Exception as e:
        print("Error:", e)
        print_command_template()

if __name__ == "__main__":
    main()
