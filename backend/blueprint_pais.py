from flask import Blueprint, request, jsonify
from contextlib import closing
import sqlite3
from flask_cors import CORS
from model_pais import ModelPais

blueprint_pais = Blueprint('blueprint_pais', __name__)
CORS(blueprint_pais)

def conectar():
    return sqlite3.connect("geo.db")

@blueprint_pais.route("/adicionar_pais", methods = ["POST"])
def adicionar_pais():
    return ModelPais.adicionar_pais()

@blueprint_pais.route("/atualizar_pais", methods = ["PUT"])
def atualizar_pais():
    return ModelPais.atualizar_pais()

@blueprint_pais.route("/consultar_pais_id/<int:pais_id>", methods = ["GET"])
def consultar_pais_id(pais_id):
    return ModelPais.consultar_pais_id(pais_id)

@blueprint_pais.route("/consultar_pais_nome/<string:nome>", methods = ["GET"])
def consultar_pais_nome(nome):
    return ModelPais.consultar_pais_nome(nome)

@blueprint_pais.route("/listar_paises", methods = ["GET"])
def listar_paises():
    return ModelPais.listar_paises()

@blueprint_pais.route("/excluir_pais_id/<int:pais_id>", methods = ["DELETE"])
def excluir_pais_id(pais_id):
    return ModelPais.excluir_pais_id(pais_id)