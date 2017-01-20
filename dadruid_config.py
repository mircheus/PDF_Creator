import dadruid_example
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait
from io import StringIO

def writeString():
    fpath = "C:/Users/Mircheus/PycharmProjects/PDF_Creator/temp.pdf"
    packet = StringIO()
    letter = StringIO()
    cv = canvas.Canvas(packet, pagesize=letter)

    # create a string
    cv.drawString(0, 500, "hello World")
    # a circle. Do not add another string. This draws on a new page.
    cv.circle(50, 250, 20, stroke=1, fill=0)

    # save to string
    cv.save()

    #get back to 0
    packet.seek(0)

    # write to a file
    with open(fpath, 'wb') as fp:
        fp.write(packet.getvalue())