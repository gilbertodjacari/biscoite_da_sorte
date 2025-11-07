import random
from flask import Flask

# 1. Cria a aplicação Flask
app = Flask(__name__)

# 2. Lista de "sortes"
sortes = [
    "A sorte favorece os audazes.",
    "Hoje é um ótimo dia para aprender algo novo.",
    "A paciência é a chave para a vitória.",
    "Um sorriso seu pode mudar o dia de alguém.",
    "Acredite em si mesmo e tudo será possível.",
    "O melhor momento para plantar uma árvore foi há 20 anos. O segundo melhor é agora.",
    "Você encontrará uma nova oportunidade em breve."
]


# 3. Define a rota principal (a "homepage")
@app.route('/')
def pagina_inicial():
    # 4. Escolhe uma sorte aleatoriamente
    frase_da_sorte = random.choice(sortes)

    # 5. Retorna o HTML diretamente para o navegador
    #    (Com um pouco de estilo e um link para recarregar!)
    return f"""
    <html>
        <head>
            <title>Biscoito da Sorte</title>
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #f4f4f4;">

            <h1>Seu Biscoito da Sorte Virtual 🥠</h1>

            <blockquote style="font-size: 1.5em; font-style: italic; margin: 30px; padding: 20px; background-color: #fff; border-left: 5px solid #007BFF; border-radius: 5px;">
                "{frase_da_sorte}"
            </blockquote>

            <a href="/" style="text-decoration: none; padding: 10px 15px; background-color: #007BFF; color: white; border-radius: 5px;">
                Pegar outro biscoito!
            </a>

        </body>
    </html>
    """


# 6. Roda o servidor de desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)