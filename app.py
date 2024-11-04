from flask import Flask, render_template, request
from models.calculator import calcular_tempo_de_viagem

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    horario_partida = None
    horario_chegada = None
    valor_final = None
    
    if request.method == 'POST':
        # Coleta os dados do formulário
        distancia = float(request.form['distancia'])
        velocidade = float(request.form['velocidade'])
        num_paradas = int(request.form['num_paradas'])
        tempo_parada = float(request.form['tempo_parada'])
        horario_partida = request.form['horario_partida']
        consumo_medio = request.form.get('consumo_medio', type=float)
        preco_combustivel = request.form.get('preco_combustivel', type=float)
        
        # Chama a função para calcular
        resultado, horario_chegada, valor_final = calcular_tempo_de_viagem(
            distancia,
            velocidade,
            num_paradas,
            tempo_parada,
            horario_partida,
            consumo_medio,
            preco_combustivel
        )

        # Debug: Imprima os valores calculados
        #print(f"Resultado: {resultado}, Horário de Chegada: {horario_chegada}, Valor Final: {valor_final}")

    return render_template('index.html', resultado=resultado, horario_partida=horario_partida, horario_chegada=horario_chegada, valor_final=valor_final)


if __name__ == "__main__":
    app.run(debug=True)
