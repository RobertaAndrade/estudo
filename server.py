from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello(): 
    return "<h1>Welcome to my first API!</h1>"

@app.route("/developer")
def roberta():
    return {
        "nome": "Roberta Andrade",
        "idade": 20
    }

@app.route("/address/<string:cep>")
def hello_world(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)