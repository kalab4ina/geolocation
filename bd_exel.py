import openpyxl
import csv
from geo_place import extract_lat_long_via_address


bd_open = openpyxl.load_workbook(filename = 'BD_main.xlsx',read_only=True)
bd_sheet = bd_open.sheetnames[0]
work_sheet =  bd_open[bd_sheet]

for i in range(3,6):
    data = [work_sheet['B'+str(i)].value]
    
    print(extract_lat_long_via_address(work_sheet['B'+str(i)].value))
