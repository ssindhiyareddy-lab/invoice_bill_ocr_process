from document_parser.ocr_engine import extract_text
from document_parser.document_detector import detect_document

file_path = r"c:\Users\user\Downloads\P.S.K. Engeineering Construction & Co-SEH022126-27-05 Jun 26.pdf"

ocr = extract_text(file_path)

doc = detect_document(ocr)

print("=" * 50)
print("Detected Document :", doc)
print("=" * 50)