from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import magenta, red

import random
number = random.randint(1, 99)
number = str(number)
c = canvas.Canvas('PDFs/WestWorld%s.pdf' % number)

c.drawImage('pics/WW.jpg', 200, 700, 211, 131)
c.translate(cm, cm)
# define a large font
c.setFont("Helvetica", 14)
# choose some colors
# c.setStrokeColorRGB(0, 0, 0)
c.setFillColorRGB(1, 0, 1)

# draw some lines
# c.line(0, 0, 0, 1.7*inch)
# c.line(0, 0, 1*inch, 0)

# draw a ractangle
#c.rect(0.2*inch, 0.2*inch, 1*inch, 1.5*inch, fill=1)

# make text go straight up
# c.rotate(90)

# change color
c.setFillColorRGB(0, 0, 0)

# say hello wolrd! (note after rotate the y coord needs to be negative)
c.drawString(0, 20*cm, "Project: ")
c.drawString(0, 19*cm, "Project Manager: ")
c.drawString(0, 18*cm, "Begin: ")
c.drawString(0, 17*cm, "Deadline: ")
c.drawString(0, 16*cm, "Over(fact): ")
c.drawString(0, 15*cm, "Commentary: ")

c.showPage()
c.save()