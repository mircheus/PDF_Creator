from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm
from reportlab.pdfgen import canvas
from main_config import convert_time

def pdf_gen(data):
    code_date = str(convert_time(data[0][2]))
    code_project = str(data[0][0])
    # Создаём файл PDF
    c = canvas.Canvas("Reports/Report-%s-%s.pdf" % (code_date, code_project), pagesize=letter)
    # Вставляем лого
    c.drawImage('pics/WW.jpg', 200, 650, 211, 131)
    # Переводим единицы измерения в см
    c.translate(cm, cm)
    # Выбираем шрифт и его размер
    c.setFont("Helvetica", 14)
    # Выставляем черный цвет
    c.setFillColorRGB(0, 0, 0)
    # Вывод стандартной формы
    c.drawString(0, 20 * cm, "Project: ")
    c.drawString(0, 19 * cm, "Project Manager: ")
    c.drawString(0, 18 * cm, "Begin: ")
    c.drawString(0, 17 * cm, "Deadline: ")
    c.drawString(0, 16 * cm, "Over(fact): ")
    c.drawString(0, 15 * cm, "Commentary: ")
    # Вывод данных из БД
    c.drawString(5 * cm, 20 * cm, str(data[0][0]))  # Project name
    c.drawString(5 * cm, 19 * cm, data[0][1])  # Project man
    c.drawString(5 * cm, 18 * cm, convert_time(data[0][2]))  # Begin date
    c.drawString(5 * cm, 17 * cm, convert_time(data[0][3]))  # Deadline date
    c.drawString(5 * cm, 16 * cm, convert_time(data[0][4]))  # Over date
    c.drawString(5 * cm, 15 * cm, data[0][5])  # Comments
    c.showPage()
    c.save() # сохраняем страницу PDF
