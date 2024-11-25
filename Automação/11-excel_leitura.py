from openpyxl import load_workbook

wb = load_workbook(filename='files/test.xlsx')

planilha = wb['Planilha 1']

print(planilha['A2'].value)

for i in range(2, 5):
    #print(f"{planilha['A{i}'].value}")
    ano = planilha['A%s' %i].value
    lucro = planilha['B%s' %i].value
    custo = planilha['C%s' %i].value
    print("{0} teve {1} de lucro e {2} de custo".format(ano, lucro, custo))
    #msg = f"Ano {planilha['A{i}'].value} teve {planilha['B{i}'].value} de lucro e {planilha['C{i}'].value} de custo"
    #print(msg)