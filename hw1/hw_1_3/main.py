import sys

def wc(file_paths=None):
    total_lines = 0
    total_words = 0
    total_bytes = 0

    if file_paths:
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines, words, bytes_count = process(file)
                print(f"\t{lines}\t{words}\t{bytes_count} {file_path}")
                total_lines += lines
                total_words += words
                total_bytes += bytes_count

        if len(file_paths) > 1:
            print(f"\t{total_lines}\t{total_words}\t{total_bytes} total")
    else:
        lines, words, bytes_count = process(sys.stdin)
        print(f"\t{lines}\t{words}\t{bytes_count}")


def process(inp):
    lines, words, bytes_count = 0, 0, 0

    for line in inp:
        lines += 1
        words += len(line.split())
        bytes_count += len(line.encode('utf-8'))

    return lines, words, bytes_count

if len(sys.argv) >= 2:
    wc(sys.argv[1:])
else:
    wc()