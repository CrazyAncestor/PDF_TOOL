from PyPDF2 import PdfMerger
import sys

merger = PdfMerger()
pdfs = sys.argv[1:]

for pdf in pdfs:
    merger.append(pdf)

merger.write('merge_result.pdf')
print('pdf files merged successfully')
merger.close()
