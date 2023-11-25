import base64
from decimal import Decimal
from io import BytesIO
from pathlib import Path

from borb.pdf import Document, Page, SingleColumnLayout, Paragraph, PDF
from borb.pdf.canvas.layout.image.barcode import Barcode, BarcodeType


class PdfBuilder(object):
    def __init__(self):
        self.pdf = Document()

    def add_page(self):
        page = Page()
        self.pdf.add_page(page)
        return page

    def add_single_column_layout(self, page):
        return SingleColumnLayout(page)

    def add_paragraph(self, layout, text):
        layout.add(Paragraph(text))

    def add_qr_code(self, layout, data, width, height):
        qr_code = Barcode(data=data, width=Decimal(width), height=Decimal(height), type=BarcodeType.QR)
        layout.add(qr_code)

    def add_qr_code_from_text(self, layout, text, width, height):
        qr_data = f"Text: {text}"
        self.add_qr_code(layout, qr_data, width, height)

    def save_pdf(self, output):
        if isinstance(output, str):
            output_path = Path(output)
            with open(output_path, "wb") as pdf_file_handle:
                PDF.dumps(pdf_file_handle, self.pdf)
        else:
            PDF.dumps(output, self.pdf)


def build_pdf(form):
    pdf_builder = PdfBuilder()
    page = pdf_builder.add_page()
    layout = pdf_builder.add_single_column_layout(page)
    pdf_builder.add_paragraph(layout, "Use the QR below and share your information quickly and easily!")
    pdf_builder.add_qr_code_from_text(layout,
                                      f"Name: {form.fullName.data}\nEmail: {form.email.data}\nPhone: {form.phone.data}",
                                      width=400, height=300)

    pdf_bytesio = BytesIO()
    pdf_builder.save_pdf(pdf_bytesio)
    pdf_bytesio.seek(0)
    pdf_binary = pdf_bytesio.read()

    return pdf_to_base64(pdf_binary)


def pdf_to_base64(pdf_binary_data):
    base64_pdf = base64.b64encode(pdf_binary_data).decode('utf-8')
    return base64_pdf
