from tkinter import Tk, filedialog
import os
import zipfile
import tempfile
import shutil

from document_parser.ocr_engine import extract_text
from document_parser.document_detector import detect_document
from document_parser.invoice_parser import extract_invoice
from document_parser.table_parser import extract_table
from excel_export import export_to_excel


# ==========================================
# GLOBAL LISTS
# ==========================================

completed_files = []
pending_files = []


# ==========================================
# SELECT ZIP FILE
# ==========================================

def select_zip():

    root = Tk()
    root.withdraw()

    zip_file = filedialog.askopenfilename(
        title="Select ZIP File",
        filetypes=[("ZIP Files", "*.zip")]
    )

    root.destroy()

    return zip_file


# ==========================================
# PROCESS SINGLE FILE
# ==========================================

def process_file(file_path):

    global completed_files
    global pending_files

    print("\n" + "=" * 70)
    print("Processing :", os.path.basename(file_path))
    print("=" * 70)

    try:

        ocr_results = extract_text(file_path)

        doc_type = detect_document(ocr_results)

        print("Detected :", doc_type)

        if doc_type != "Invoice":

            print("Skipped (Not an Invoice)")
            pending_files.append(os.path.basename(file_path))
            return

        # --------------------------------
        # Extract Header
        # --------------------------------

        header = extract_invoice(ocr_results)

        header["File Name"] = os.path.basename(file_path)

        # --------------------------------
        # Extract Items
        # --------------------------------

        items = extract_table(ocr_results)

        # --------------------------------
        # Header Details
        # --------------------------------

        print("\n")
        print("=" * 70)
        print("HEADER DETAILS")
        print("=" * 70)

        for k, v in header.items():

            print(f"{k} : {v}")

        # --------------------------------
        # Item Details
        # --------------------------------

        print("\n")
        print("=" * 70)
        print("ITEM DETAILS")
        print("=" * 70)

        if len(items) == 0:

            print("No Items Extracted")

        else:

            for i, item in enumerate(items, start=1):

                print(f"\nItem {i}")

                print(f"Description : {item.get('Description','')}")
                print(f"HSN         : {item.get('HSN','')}")
                print(f"Quantity    : {item.get('Quantity','')}")
                print(f"Unit        : {item.get('Per','')}")
                print(f"Rate        : {item.get('Rate','')}")
                print(f"Amount      : {item.get('Amount','')}")

        # --------------------------------
        # Export Excel
        # --------------------------------

        output_folder = "output"

        os.makedirs(output_folder, exist_ok=True)

        excel_name = os.path.splitext(
            os.path.basename(file_path)
        )[0] + ".xlsx"

        output_file = os.path.join(
            output_folder,
            excel_name
        )

        export_to_excel(
            header,
            items,
            output_file
        )

        print("\nExcel Saved :", output_file)

        completed_files.append(os.path.basename(file_path))

    except Exception as e:

        print("Error :", e)

        pending_files.append(os.path.basename(file_path))


# ==========================================
# MAIN
# ==========================================

def main():

    print("=" * 70)
    print("              MAKER CHECKER OCR")
    print("=" * 70)

    zip_path = select_zip()

    if not zip_path:

        print("No ZIP File Selected.")
        return

    temp_folder = tempfile.mkdtemp()

    try:

        print("\nExtracting ZIP...")

        with zipfile.ZipFile(zip_path, "r") as zip_ref:

            zip_ref.extractall(temp_folder)

        print("ZIP Extracted Successfully.")

        supported = (
            ".pdf",
            ".jpg",
            ".jpeg",
            ".png",
            ".bmp",
            ".tif",
            ".tiff"
        )

        for root, dirs, files in os.walk(temp_folder):

            for file in files:

                if file.lower().endswith(supported):

                    full_path = os.path.join(root, file)

                    process_file(full_path)

        # =====================================
        # FINAL SUMMARY
        # =====================================

        print("\n")
        print("=" * 70)
        print("PROCESS SUMMARY")
        print("=" * 70)

        print("\nCompleted Files")

        if len(completed_files) == 0:

            print("None")

        else:

            for file in completed_files:

                print("✔", file)

        print("\nPending Files")

        if len(pending_files) == 0:

            print("None")

        else:

            for file in pending_files:

                print("✖", file)

        print("\n")
        print("Total Files :", len(completed_files) + len(pending_files))
        print("Completed  :", len(completed_files))
        print("Pending    :", len(pending_files))

    finally:

        shutil.rmtree(temp_folder)

        print("\nTemporary Files Deleted.")


if __name__ == "__main__":

    main()