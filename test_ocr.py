from document_parser.ocr_engine import extract_text

file_path = r"c:\Users\user\Downloads\P.S.K. Engeineering Construction & Co-SEH022126-27-05 Jun 26.pdf"

ocr_results = extract_text(file_path)

print("=" * 80)
print("OCR RESULTS")
print("=" * 80)

for item in ocr_results:
    print(item)

print("=" * 80)