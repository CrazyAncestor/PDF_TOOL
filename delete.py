from PyPDF2 import PdfWriter, PdfReader
import sys

#   Input filename
input_file = sys.argv[1]
infile = PdfReader(input_file, 'rb')
output = PdfWriter()

#   Delete page numbers
pages_to_delete = sys.argv[2:]
pages_delete_num = []
for i in range(len(pages_to_delete)):
    pages_delete_num.append(int(pages_to_delete[i])-1)
pages_to_keep = list(range(len(infile.pages)))
for i in pages_delete_num:
    pages_to_keep.remove(i)

#   Create new pdf
for i in pages_to_keep:
    p = infile.pages[i] 
    output.add_page(p)

with open('trimmed_file.pdf', 'wb') as f:
    output.write(f)