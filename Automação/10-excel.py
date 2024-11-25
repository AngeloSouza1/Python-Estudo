from openpyxl import Workbook

#1 - Criando Workbook
wb = Workbook()
name = "files/test.xlsx"

#2 - Criando Worksheet
ws1 = wb.active
ws1.title = "Planilha 1"

data = [
    ['Ano', 'Lucro', 'Custos'],
    [2023, '25%', '45%'],
    [2023, '45%', '55%'],
    [2023, '70%', '40%'],   
]

for line in data:
    ws1.append(line)
    
ws2 = wb.create_sheet(title="Pi")
ws2['D2'] = 3.14
    
wb.save(filename=name)