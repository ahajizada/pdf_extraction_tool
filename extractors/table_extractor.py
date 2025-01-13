import pdfplumber

def extract_tables(file_path):
    tables = []
    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            table = page.extract_table()
            if table:
                tables.append({"page": page_num, "table": table})
    return tables
