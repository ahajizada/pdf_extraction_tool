from extractors.text_extractor import extract_text
from extractors.table_extractor import extract_tables

def test_text_extraction():
    text = extract_text("tests/sample.pdf")
    assert len(text) > 0
    print("Text extraction test passed!")

def test_table_extraction():
    tables = extract_tables("tests/sample.pdf")
    assert len(tables) > 0
    print("Table extraction test passed!")

if __name__ == "__main__":
    test_text_extraction()
    test_table_extraction()

