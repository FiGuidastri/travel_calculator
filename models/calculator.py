from datetime import datetime, timedelta

def calcular_tempo_de_viagem(distancia, velocidade, num_paradas=0, tempo_parada=0, horario_partida=None, consumo_medio=None, preco_combustivel=None):
    # Calcula o tempo total de viagem em horas sem paradas
    tempo_viagem = distancia / velocidade
    # Calcula o tempo total das paradas em horas e soma ao tempo de viagem
    tempo_total_com_paradas = tempo_viagem + (num_paradas * (tempo_parada / 60))
    
    # Extrai horas e minutos
    horas = int(tempo_total_com_paradas)
    minutos = int((tempo_total_com_paradas - horas) * 60)
    tempo_formatado = f"{horas} horas e {minutos} minutos"
    
    # Calcula o horário de chegada se horário de partida for fornecido
    horario_chegada = None
    if horario_partida:
        horario_partida = datetime.strptime(horario_partida, "%H:%M")
        horario_chegada = horario_partida + timedelta(hours=horas, minutes=minutos)
        horario_chegada = horario_chegada.strftime("%H:%M")
    
    # Calcula o custo estimado de combustível
    custo_combustivel = None
    if consumo_medio and preco_combustivel:
        litros_necessarios = distancia / consumo_medio
        custo_combustivel = (litros_necessarios * preco_combustivel) * 2  # calculando ida e volta
        custo_combustivel = float(custo_combustivel)  # Garantindo que seja um número para cálculos
    
    valor_pedagios = custo_combustivel * 0.30 if custo_combustivel is not None else 0
    
    custo = custo_combustivel + valor_pedagios if custo_combustivel is not None else 0
    
    lucro = custo * 0.70
    
    valor_final = custo + lucro
    
    return tempo_formatado, horario_chegada, f'R$ {valor_final:.2f}'
