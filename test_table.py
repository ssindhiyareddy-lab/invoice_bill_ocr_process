from document_parser.ocr_engine import extract_text
from document_parser.table_parser import extract_table

file_path = r"c:\Users\user\Downloads\P.S.K. Engeineering Construction & Co-SEH022126-27-05 Jun 26.pdf"

ocr = extract_text(file_path)

items = extract_table(ocr)

print("=" * 70)
print("LINE ITEMS")
print("=" * 70)

for i, item in enumerate(items, 1):

    print(f"\nItem {i}")

    for k, v in item.items():
        print(f"{k:12}: {v}")