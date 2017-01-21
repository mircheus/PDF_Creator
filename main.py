from main_config import database, convert_time
from database import SQLighter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm
from functions import pdf_gen
from main_config import convert_time

db = SQLighter(database) # создаем объект БД(подключаемся к БД)
b = True
while b != False: # Цикл для "бесконечного" меню
    bigdata = db.select_all_projects() # Выбираем весь список записей
    for i in range(0,9): # Цикл для вывода списка
        print(bigdata[i][0], '---', bigdata[i][1], '---', bigdata[i][2], '--- Project started: ', convert_time(bigdata[i][3]))
    report_num = input('\n Введите номер проект для формирования отчёта - ')
    data = db.select_project(report_num) # запрос к выбранной записи
    pdf_gen(data) # Генерация PDF в папку Reports
    print('\nОтчёт сформирован и находится в папке Reports.\n')


