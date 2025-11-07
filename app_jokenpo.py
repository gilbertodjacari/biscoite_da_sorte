import random
from flask import Flask

app = Flask(__name__)


# --- Lógica do Jogo ---
def calcular_vencedor(escolha_usuario, escolha_computador):
    """Determina o vencedor do Pedra, Papel, Tesoura."""

    if escolha_usuario == escolha_computador:
        return "Empate! 😐"

    # Condições de vitória do usuário
    if (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
            (escolha_usuario == "papel" and escolha_computador == "pedra") or \
            (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        return "Você Ganhou! 🎉"

    # Se não empatou e não ganhou, perdeu
    return "Você Perdeu! 😢"


# --- Estilos (para deixar bonito) ---
# (Coloquei aqui para o HTML ficar mais limpo)
ESTILOS = """
<style>
    body { 
        font-family: Arial, sans-serif; 
        text-align: center; 
        margin-top: 50px; 
        background-color: #f0f2f5; 
    }
    h1, h2 { color: #333; }
    .escolhas { margin: 30px 0; }
    .escolha {
        font-size: 3em;
        text-decoration: none;
        margin: 0 20px;
        padding: 20px;
        border-radius: 10px;
        background-color: #fff;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .escolha:hover {
        transform: scale(1.1);
    }
    .resultado {
        font-size: 1.2em;
        margin: 20px;
    }
    .btn-voltar {
        display: inline-block;
        margin-top: 30px;
        text-decoration: none;
        padding: 10px 20px;
        background-color: #007BFF;
        color: white;
        border-radius: 5px;
        font-weight: bold;
    }
</style>
"""


# --- Rotas do Flask ---

# Rota 1: Página Inicial (para o usuário escolher)
@app.route('/')
def index():
    return f"""
    <html>
        <head>
            <title>Jokenpô</title>
            {ESTILOS}
        </head>
        <body>
            <h1>Pedra, Papel ou Tesoura?</h1>
            <h2>Faça sua jogada:</h2>
            <div class="escolhas">
                <a href="/jogar/pedra" class="escolha" title="Pedra">🪨</a>
                <a href="/jogar/papel" class="escolha" title="Papel">📄</a>
                <a href="/jogar/tesoura" class="escolha" title="Tesoura">✂️</a>
            </div>
        </body>
    </html>
    """


# Rota 2: A Rota Dinâmica (onde o jogo acontece)
# O <string:escolha_usuario> é a parte mágica!
# O Flask pega o que veio na URL e passa como argumento para a função.
@app.route('/jogar/<string:escolha_usuario>')
def jogar(escolha_usuario):
    # 1. Validação (para o caso de o usuário digitar algo errado na URL)
    opcoes_validas = ["pedra", "papel", "tesoura"]
    if escolha_usuario not in opcoes_validas:
        return f"""
            <html><head>{ESTILOS}</head><body>
                <h1>Escolha inválida!</h1>
                <p>Por favor, jogue usando um dos links da página inicial.</p>
                <a href="/" class="btn-voltar">Voltar</a>
            </body></html>
        """

    # 2. Computador faz a jogada
    escolha_computador = random.choice(opcoes_validas)

    # 3. Calcula o resultado
    resultado = calcular_vencedor(escolha_usuario, escolha_computador)

    # 4. Mostra o resultado
    return f"""
    <html>
        <head>
            <title>Resultado</title>
            {ESTILOS}
        </head>
        <body>
            <h1>Resultado da Rodada</h1>

            <div class="resultado">
                Você escolheu: <strong>{escolha_usuario.capitalize()}</strong>
            </div>
            <div class="resultado">
                O computador escolheu: <strong>{escolha_computador.capitalize()}</strong>
            </div>

            <h2>{resultado}</h2>

            <a href="/" class="btn-voltar">Jogar Novamente</a>
        </body>
    </html>
    """


# Roda o servidor
if __name__ == '__main__':
    app.run(debug=True)