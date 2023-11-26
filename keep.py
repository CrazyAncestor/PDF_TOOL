from PyPDF2 import PdfWriter, PdfReader
import sys

#   Input filename
input_file = sys.argv[1]
infile = PdfReader(input_file, 'rb')
output = PdfWriter()

#   Keep page numbers
pages_to_keep = sys.argv[2:]
pages_keep_num = []
for i in pages_to_keep:
    pages_keep_num.append(int(i)-1)

#   Create new pdf
for i in pages_keep_num:
    p = infile.pages[i] 
    output.add_page(p)

with open('trimmed_file.pdf', 'wb') as f:
    output.write(f)