from openpyxl import Workbook

print("Lendo dados do arquivo de texto")

file_txt = open("files/gastos.txt", "r", encoding="utf-8")
file = file_txt.read()
# print(file)
list_data = file.splitlines()
# print(list_data)
for i in range(0, len(list_data)):
    list_data[i] = list_data[i].split(",")
# print(list_data)

wb = Workbook()
ws = wb.active

for row in list_data:
    ws.append(row)
    
wb.save('files/gastos.xlsx')
