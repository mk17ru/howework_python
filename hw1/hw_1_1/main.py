import sys

def nl(file_path=None):
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            process(file)
    else:
        process(sys.stdin)

def process(inp):
    line_number = 1
    for line in inp:
        print(f"\t{line_number}\t{line.strip()}")
        line_number += 1

if len(sys.argv) == 2:
    nl(sys.argv[1])
else:
    nl()