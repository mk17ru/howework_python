def read_table_from_file(file_path):
    table_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            row = line.strip().split(' ')
            table_data.append(row)
    return table_data

def generate_latex_table(data):
    latex_code = "\\begin{document}\n"

    latex_code += "\\begin{tabular}{|" + "c|" * len(data[0]) + "}\n"
    latex_code += "\\hline\n"

    for row in data:
        row_str = " & ".join(map(str, row)) + " \\\\"
        latex_code += row_str + "\n"

    latex_code += "\\hline\n\\end{tabular}\n"

    latex_code += "\\end{document}\n"

    return latex_code

if __name__ == "__main__":
    input_file_path = "../artifacts/input.txt"
    output_file_path = "../artifacts/output.tex"

    table_data = read_table_from_file(input_file_path)
    latex_table = generate_latex_table(table_data)

    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(latex_table)
