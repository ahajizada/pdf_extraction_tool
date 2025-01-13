import fitz  

def extract_text(file_path, keyword=None):
    text_data = []
    doc = fitz.open(file_path)
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        if keyword:
            if keyword.lower() in text.lower():
                text_data.append(f"Page {page_num}:\n{text}\n")
        else:
            text_data.append(f"Page {page_num}:\n{text}\n")
    return text_data
