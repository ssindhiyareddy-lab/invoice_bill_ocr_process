from document_parser.ocr_engine import extract_text
from document_parser.layout_parser import build_layout
from document_parser.coordinate_parser import *

file_path = r"c:\Users\user\Downloads\P.S.K. Engeineering Construction & Co-SEH022126-27-05 Jun 26.pdf"

ocr = extract_text(file_path)

rows = build_layout(ocr)

print("Invoice No :", get_below_value(rows, "Invoice No"))
print("GSTIN :", find_gstin(rows))
print("Dispatch :", get_below_value(rows, "Despatched through"))