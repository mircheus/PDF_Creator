import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait
import dadruid_config
from PyPDF2 import PdfFileWriter, PdfFileReader
from dadruid_config import writeString
from io import StringIO
writeString()
# a reader
reader = PdfFileReader(open("path", 'rb'))

# a writer
writer = PdfFileWriter()
outfp = open("outpath", 'wb')
writer.write(outfp)

