import re


def validate(header, items):

    results = []

    # Invoice Number
    results.append((
        "Invoice Number",
        "PASS" if header.get("Invoice Number") else "FAIL"
    ))

    # Supplier Name
    results.append((
        "Supplier Name",
        "PASS" if header.get("Supplier Name") else "FAIL"
    ))

    # Invoice Date
    results.append((
        "Invoice Date",
        "PASS" if header.get("Invoice Date") else "FAIL"
    ))

    # GSTIN
    gst = header.get("GSTIN", "")

    pattern = r"^\d{2}[A-Z]{5}\d{4}[A-Z][A-Z0-9]Z[A-Z0-9]$"

    results.append((
        "GSTIN",
        "PASS" if re.match(pattern, gst) else "FAIL"
    ))

    # Items
    results.append((
        "Items",
        "PASS" if len(items) > 0 else "FAIL"
    ))

    return results