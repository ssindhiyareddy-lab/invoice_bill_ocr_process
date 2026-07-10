from document_parser.ocr_engine import extract_text
from document_parser.invoice_parser import extract_invoice

file_path = r"c:\Users\user\Downloads\P.S.K. Engeineering Construction & Co-SEH022126-27-05 Jun 26.pdf"

ocr_results = extract_text(file_path)

header = extract_invoice(ocr_results)

print("=" * 60)
print("HEADER DETAILS")
print("=" * 60)

for key, value in header.items():
    print(f"{key} : {value}")