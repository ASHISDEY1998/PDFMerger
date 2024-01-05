from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ['agreement.pdf','sql.pdf']:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

