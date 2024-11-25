from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference

# Criação da planilha e inserção de dados
wb = Workbook()
ws = wb.active

# Dados para o gráfico
rows = [
    ['Ano', 'Lucro', 'Custos'],
    [2017, 40, 30],
    [2018, 35, 25],
    [2019, 30, 20],
    [2020, 10, 5],
    [2021, 15, 10],
    [2022, 25, 15]
]

for row in rows:
    ws.append(row)

# Configuração do gráfico de área
chart = AreaChart()
chart.title = 'Lucros x Custos'
chart.style = 13  # Estilo do gráfico
chart.x_axis.title = "Ano"
chart.y_axis.title = "Valores (%)"

# Definição das categorias (Eixo X) e dos dados (Séries)
categorias = Reference(ws, min_col=1, min_row=2, max_row=7)  # Anos (Linha 2 a 7)
dados = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=7)  # Lucro e Custos

# Adicionar os dados e configurar os rótulos
chart.add_data(dados, titles_from_data=True)
chart.set_categories(categorias)

# Configurar cores personalizadas
for series in chart.series:
    if series.title == "Lucro":
        series.graphicalProperties.solidFill = "008000"  # Verde escuro para Lucro
    elif series.title == "Custos":
        series.graphicalProperties.solidFill = "FF6347"  # Vermelho claro para Custos

# Ajustar ordem das séries: colocar "Custos" acima de "Lucros"
chart.series = chart.series[::-1]  # Inverte a ordem das séries

# Adicionar o gráfico à planilha
ws.add_chart(chart, "A10")

# Salvar a planilha com o gráfico
wb.save('files/chart.xlsx')
