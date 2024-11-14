# agendamento_desligamento.py

import os

def agendar_desligamento_1_hora():
    """
    Agenda o desligamento do computador para 1 hora a partir de agora.
    """
    # 1 hora = 3600 segundos
    tempo_1_hora = 3600
    print("Desligamento agendado para 1 hora a partir de agora.")
    os.system(f"shutdown -h {tempo_1_hora // 60}")

def agendar_desligamento_30_minutos():
    """
    Agenda o desligamento do computador para 30 minutos a partir de agora.
    """
    # 30 minutos = 1800 segundos
    tempo_30_minutos = 1800
    print("Desligamento agendado para 30 minutos a partir de agora.")
    os.system(f"shutdown -h {tempo_30_minutos // 60}")

def agendar_desligamento_personalizado(tempo_em_minutos):
    """
    Agenda o desligamento do computador para um tempo personalizado em minutos.
    
    Parâmetros:
        tempo_em_minutos (int): Tempo em minutos até o desligamento.
    """
    if tempo_em_minutos <= 0:
        print("Por favor, insira um valor positivo de minutos para o agendamento.")
        return
    
    print(f"Desligamento agendado para {tempo_em_minutos} minutos a partir de agora.")
    os.system(f"shutdown -h {tempo_em_minutos}")
    
def reiniciar_computador():
    """
    Reinicia o computador imediatamente.
    """
    print("Reinicialização do computador agendada para agora.")
    os.system("shutdown -r now")    
    