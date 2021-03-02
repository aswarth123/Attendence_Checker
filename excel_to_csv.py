import openpyxl
import csv
import pandas as pd
file_name = input()
excel = openpyxl.load_workbook("classListExcel/"+file_name)
sheet = excel.active

col = csv.writer(open("classList/names.csv", 'w',  newline=""))

for r in sheet.rows:
    col.writerow([cell.value for cell in r])
