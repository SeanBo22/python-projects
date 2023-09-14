from pdf2docx import Converter

def convert_pdf_to_docx(pdf_path, docx_path):
    # Convert pdf to docx
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

input_pdf = "/path/to/pdf.file"
output_docx = "/desired/path/for/docxfile"

convert_pdf_to_docx(input_pdf, output_docx)
