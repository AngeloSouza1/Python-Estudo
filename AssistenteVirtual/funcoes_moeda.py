from requests import get

def cotacao_moeda(moeda):
    if moeda == "Dólar":
        requisicao = get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
        cotacao = requisicao.json()
        nome = cotacao['USDBRL']['name']
        data = cotacao['USDBRL']['create_date']
        valor = cotacao['USDBRL']['bid']
        mensagem = f'Cotação do {nome} em {data} é {valor} reais'
    elif moeda == "Euro":
        requisicao = get('https://economia.awesomeapi.com.br/json/last/EUR-BRL')
        cotacao = requisicao.json()
        nome = cotacao['EURBRL']['name']
        data = cotacao['EURBRL']['create_date']
        valor = cotacao['EURBRL']['bid']
        mensagem = f'Cotação do {nome} em {data} é {valor} reais'
    elif moeda == "Bitcoin":
        requisicao = get('https://economia.awesomeapi.com.br/json/last/BTC-BRL')
        cotacao = requisicao.json()
        nome = cotacao['BTCBRL']['name']
        data = cotacao['BTCBRL']['create_date']
        valor = cotacao['BTCBRL']['bid']
        mensagem = f'Cotação do {nome} em {data} é {valor} reais'
        
    return mensagem

# print(cotacao_moeda("Dólar"))