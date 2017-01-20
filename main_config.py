from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
import random
from datetime import datetime, date, time

database = "westworld.db"


def convert_time(unix_time):
    return datetime.fromtimestamp(unix_time).strftime('%d.%m.%Y')