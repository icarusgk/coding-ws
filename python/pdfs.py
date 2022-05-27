from PyPDF4 import PdfFileReader, PdfFileWriter

with open(file='dummy.pdf', mode='rb') as file:
  pdf = PdfFileReader(file)
  information = pdf.getDocumentInfo()
  number_of_pages = pdf.getNumPages()


metadata = f"""
    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """


print(metadata)


new_pdf = PdfFileWriter()
original_pdf = PdfFileReader("dummy.pdf")

# Rotate page 90 degrees to the right
page_0 = original_pdf.getPage(0).rotateClockwise(90)
new_pdf.addPage(page_0)

pdf_reader = PdfFileReader("dummy.pdf")

# Rotate page 90 degrees to the left
page_1 = pdf_reader.getPage(0).rotateCounterClockwise(90)
new_pdf.addPage(page_1)

with open(file="rotate_page.pdf", mode="wb") as new_file:
    new_pdf.write(new_file)
