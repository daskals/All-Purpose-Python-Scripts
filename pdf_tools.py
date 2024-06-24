import os
import fitz  # PyMuPDF
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter
from datetime import datetime


def convert_pdf_to_images(pdf_path, image_format):
    """
    Converts each page of a PDF to high-resolution images and saves them in the same directory as the PDF.

    Args:
    pdf_path (str): Path to the PDF file.
    image_format (str): Format to save the images (jpg or png).
    """
    # Open the PDF document
    pdf_document = fitz.open(pdf_path)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = os.path.dirname(pdf_path)
    num_pages = pdf_document.page_count

    # Iterate through each page in the PDF
    for page_num in range(num_pages):
        page = pdf_document.load_page(page_num)
        zoom = 4  # Set zoom level for high resolution
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        # Set the output file name based on the number of pages
        if num_pages > 1:
            output_file = os.path.join(output_folder, f"{pdf_name}_page_{page_num + 1}.{image_format.lower()}")
        else:
            output_file = os.path.join(output_folder, f"{pdf_name}.{image_format.lower()}")

        # Convert pixmap to PIL image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        # Save the image in the specified format
        if image_format.lower() == 'jpg':
            img.save(output_file, 'JPEG')
        else:
            img.save(output_file, image_format.upper())
        print(f"Saved: {output_file}")


def process_folder(folder_path, image_format):
    """
    Processes a folder to find and convert all PDF files to images.

    Args:
    folder_path (str): Path to the folder to process.
    image_format (str): Format to save the images (jpg or png).
    """
    # Walk through the directory to find PDF files
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                print(f"Processing: {pdf_path}")
                convert_pdf_to_images(pdf_path, image_format)


def merge_pdfs(folder_path):
    """
    Merges all PDF files in a folder into a single PDF.

    Args:
    folder_path (str): Path to the folder containing the PDF files to merge.
    """
    pdf_writer = PdfFileWriter()

    # Walk through the directory to find and sort PDF files
    for root, _, files in os.walk(folder_path):
        for file in sorted(files):
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                pdf_reader = PdfFileReader(pdf_path)
                # Add each page of the PDF to the writer
                for page_num in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))

    # Generate a timestamped filename for the merged PDF
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(folder_path, f"merged_{timestamp}.pdf")

    # Write the merged PDF to a file
    with open(output_file, "wb") as out_file:
        pdf_writer.write(out_file)
    print(f"Merged PDF saved as: {output_file}")


def split_pdf(pdf_path):
    """
    Splits a PDF file into separate pages.

    Args:
    pdf_path (str): Path to the PDF file to split.
    """
    pdf_reader = PdfFileReader(pdf_path)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = os.path.dirname(pdf_path)

    # Iterate through each page in the PDF
    for page_num in range(pdf_reader.numPages):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page_num))
        output_file = os.path.join(output_folder, f"{pdf_name}_page_{page_num + 1}.pdf")

        # Write each page to a separate PDF file
        with open(output_file, "wb") as out_file:
            pdf_writer.write(out_file)
        print(f"Saved: {output_file}")


if __name__ == "__main__":
    # Set these variables to select the operation and provide necessary paths
    operation = "convert"  # Options: "convert", "merge", "split"
    folder_path = r'C:\Users\Greeniotsolutions\Dropbox\IOT_projects\Parkit_city\Parkit_city_Costs\Costs_2023\JLC_PCB'  # Path to the folder containing PDFs or single PDF file for splitting
    image_format = "jpg"  # Image format for conversion (jpg or png)
    pdf_path = "path/to/single/pdf/file.pdf"  # Path to a single PDF file for splitting (required for split operation)

    # Perform the selected operation
    if operation == "convert":
        process_folder(folder_path, image_format)
    elif operation == "merge":
        merge_pdfs(folder_path)
    elif operation == "split":
        if not pdf_path:
            print("Error: pdf_path is required for the split operation")
        else:
            split_pdf(pdf_path)
