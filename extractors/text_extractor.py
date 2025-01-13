import fitz  

def extract_text(file_path, keyword=None):
    text_data = []
    doc = fitz.open(file_path)
    for page in doc:
        text = page.get_text()
        if keyword:
            if keyword in text:
                text_data.append(text)
        else:
            text_data.append(text)
    return text_data

