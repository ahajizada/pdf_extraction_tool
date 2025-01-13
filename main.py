import argparse
from extractors.text_extractor import extract_text
from extractors.table_extractor import extract_tables
import pandas as pd
import json

def main():
    parser = argparse.ArgumentParser(description="PDF Data Extraction Tool")
    parser.add_argument("file", help="Path to the PDF file")
    parser.add_argument("--keyword", help="Keyword for filtering text")
    parser.add_argument("--output", choices=["csv", "json"], default="csv", help="Output format")
    args = parser.parse_args()

    text_data = extract_text(args.file, args.keyword)
    tables = extract_tables(args.file)

    if args.output == "csv":
        if tables:
            df = pd.DataFrame(tables[0])
            df.to_csv("output/extracted_data.csv", index=False)
        else:
            with open("output/extracted_data.csv", "w") as f:
                f.writelines(text_data)
    elif args.output == "json":
        data = {"text": text_data, "tables": tables}
        with open("output/extracted_data.json", "w") as f:
            json.dump(data, f, indent=4)

    print(f"Data extracted and saved in output/extracted_data.{args.output}")

if __name__ == "__main__":
    main()

