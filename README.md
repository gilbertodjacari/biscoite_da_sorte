# 🥠 Biscoito da Sorte Virtual

Um mini-aplicativo web divertido feito com Flask que exibe uma frase de "sorte" ou inspiradora diferente cada vez que a página é carregada.

## 💡 Sobre o Projeto

Este é um projeto simples em Flask criado para demonstrar os conceitos básicos de:
* Criação de uma aplicação Flask.
* Definição de rotas (`@app.route('/')`).
* Retorno de HTML dinâmico diretamente de uma função Python.
* Uso da biblioteca `random` do Python para seleção aleatória.

## 🚀 Como Executar

Este projeto usa um ambiente virtual (`venv`) para gerenciar suas dependências.

1.  **Clone o repositório (ou baixe os arquivos):**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd biscoite_da_sorte
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    # Criar (apenas uma vez)
    python3 -m venv .venv
    
    # Ativar (sempre que for trabalhar no projeto)
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    (Certifique-se de que o venv está ativado)
    ```bash
    pip install Flask
    ```

4.  **Rode o aplicativo:**
    ```bash
    python app.py
    ```

5.  **Acesse no seu navegador:**
    Abra [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Flask** - O micro-framework web.
