import sys

def tail(file_paths=None):
    if file_paths:
        for file_path in file_paths:
            print(f"==> {file_path} <==")
            with open(file_path, 'r', encoding='utf-8') as file:
                process(file, 10)
    else:
        process(sys.stdin, 17)

def process(inp, number_of_rows):
    lines = inp.readlines()
    if len(lines) <= number_of_rows:
        print("".join(lines), end="")
    else:
        for line in lines[-number_of_rows:]:
            print(line, end="")
    print()

if len(sys.argv) >= 2:
    tail(sys.argv[1:])
else:
    tail()