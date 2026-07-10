from document_parser.ocr_engine import extract_text
from document_parser.layout_parser import build_layout

file_path = r"c:\Users\user\Downloads\P.S.K. Engeineering Construction & Co-SEH022126-27-05 Jun 26.pdf"

ocr = extract_text(file_path)

rows = build_layout(ocr)

print("=" * 80)
print("OCR LAYOUT")
print("=" * 80)

for row in rows:

    print("-" * 80)

    line = " | ".join([text for _, text in row])

    print(line)