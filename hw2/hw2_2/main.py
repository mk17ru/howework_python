import subprocess
import pdflatex
import os

from table_generator.table_generator import *

def generate_pdf_from_latex(latex_code, output_file_path):
    # Run pdflatex to generate PDF
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(latex_code)
    subprocess.check_output(["pdflatex", os.path.abspath(output_file_path)])


if __name__ == "__main__":
    input_file_path = "artifacts/input.txt"
    output_file_path = "artifacts/output.tex"

    table_data = read_table_from_file(input_file_path)
    latex_table = generate_latex_table(table_data)

    generate_pdf_from_latex(latex_table, output_file_path)