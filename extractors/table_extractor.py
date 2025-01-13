import pdfplumber

def extract_tables(file_path):
    tables = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.append(table)
    return tables

