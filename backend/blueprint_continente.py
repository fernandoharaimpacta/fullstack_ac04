from flask import Blueprint, request, jsonify
from contextlib import closing
import sqlite3
from flask_cors import CORS
from model_continente import ModelContinente

blueprint_continente = Blueprint('blueprint_continente', __name__)
CORS(blueprint_continente)

def conectar():
    return sqlite3.connect("geo.db")

@blueprint_continente.route("/adicionar_continente", methods = ["POST"])
def adicionar_continente():
    return ModelContinente.adicionar_continente()

@blueprint_continente.route("/atualizar_continente", methods = ["PUT"])
def atualizar_continente():
    return ModelContinente.atualizar_continente()

@blueprint_continente.route("/consultar_continente_id/<int:continente_id>", methods = ["GET"])
def consultar_continente_id(continente_id):
    return ModelContinente.consultar_continente_id(continente_id)

@blueprint_continente.route("/consultar_continente_nome/<string:nome>", methods = ["GET"])
def consultar_continente_nome(nome):
    return ModelContinente.consultar_continente_nome(nome)

@blueprint_continente.route("/listar_continentes", methods = ["GET"])
def listar_continentes():
    return ModelContinente.listar_continente()

@blueprint_continente.route("/excluir_continente_id/<int:continente_id>", methods = ["DELETE"])
def excluir_continente_id(continente_id):
    return ModelContinente.excluir_continente_id(continente_id)