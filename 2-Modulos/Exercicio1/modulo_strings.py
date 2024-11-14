# modulo_strings.py

def inverter_string(texto):
    """
    Inverte a string de trás para frente.
    
    Parâmetros:
    texto (str): A string a ser invertida.
    
    Retorna:
    str: A string invertida.
    """
    return texto[::-1]

def letras_indices_pares(texto):
    """
    Retorna apenas as letras que estão em índices pares da string.
    
    Parâmetros:
    texto (str): A string a ser processada.
    
    Retorna:
    str: Uma string com as letras dos índices pares.
    """
    return texto[::2]

def letras_indices_impares(texto):
    """
    Retorna apenas as letras que estão em índices ímpares da string.
    
    Parâmetros:
    texto (str): A string a ser processada.
    
    Retorna:
    str: Uma string com as letras dos índices ímpares.
    """
    return texto[1::2]
