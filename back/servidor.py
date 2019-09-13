from flask import Flask, jsonify
from modelo import Pessoa
from playhouse.shortcuts import model_to_dict, dict_to_model

app = Flask(__name__)

@app.route("/")
def inicio():
    return "backend do sistema de pessoas; <a href=/listar_pessoas>API listar pessoas</a>"

@app.route("/listar_pessoas")
def listar_pessoas():
    # forma alternativa rápida: usando map (lambda)
    pessoas = list(map(model_to_dict, Pessoa.select()))
    return jsonify({'lista':pessoas})
    # referência: 
    # https://www.geeksforgeeks.org/python-map-function/
    
app.run(debug=True,port=4999)