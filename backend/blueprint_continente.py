from flask import Blueprint, request, jsonify
from contextlib import closing
import sqlite3
from flask_cors import CORS
from model import Model

blueprint_continente = Blueprint('blueprint_continente', __name__)
CORS(blueprint_continente)

def conectar():
    return sqlite3.connect("geo.db")

@blueprint_continente.route("/adicionar_continente", methods = ["POST"])
def adicionar_continente():
    content_type = request.headers.get('Content-Type')
    json = ""
    if (content_type == 'application/json'):
        json = request.json
    if json == "":
        return {"sucesso": False, "mensagem": "Formato de dados incorretos"}, 400
    else:
        try:
            with closing(conectar()) as con, closing(con.cursor()) as cursor:
                sql = "INSERT INTO CONTINENTE (nome) VALUES (?)"
                cursor.execute(sql, [json["nome"]])
                continente_id = cursor.lastrowid
                con.commit()
                return {"sucesso": True, "continente": {"continente_id": continente_id, "nome": json["nome"]}}, 200
        except Exception:
            return {"sucesso": False, "mensagem": "O servidor não está se comportando bem"}, 500

@blueprint_continente.route("/atualizar_continente", methods = ["PUT"])
def atualizar_continente():
    content_type = request.headers.get('Content-Type')
    json = ""
    if (content_type == 'application/json'):
        json = request.json
    if json == "":
        return {"sucesso": False, "mensagem": "Formato de dados incorretos"}, 400
    else:
        try:
            with closing(conectar()) as con, closing(con.cursor()) as cursor:
                sql = "UPDATE CONTINENTE SET nome = ? WHERE continente_id = ?"
                cursor.execute(sql, [json["nome"], json["id"]])
                con.commit()
                return {"sucesso": True, "continente": json}, 200
        except Exception:
            return {"sucesso": False, "mensagem": "O servidor não está se comportando bem"}, 500

@blueprint_continente.route("/consultar_continente_id/<int:continente_id>", methods = ["GET"])
def consultar_continente_id(continente_id):
    if continente_id == None or continente_id <= 0:
        return {"sucesso": False, "mensagem": "Formato de dados incorretos"}, 400
    else:
        try:
            with closing(conectar()) as con, closing(con.cursor()) as cursor:
                sql = "SELECT continente_id, nome FROM CONTINENTE WHERE continente_id = ?"
                cursor.execute(sql, [continente_id])
                row = cursor.fetchone()
                if row == None:
                    return {"sucesso": False, "mensagem": "Não encontrado"}, 404
                return {"sucesso": True, "continente": {"id": row[0], "nome": row[1]}}, 200
        except Exception:
            return {"sucesso": False, "mensagem": "O servidor não está se comportando bem"}, 500

@blueprint_continente.route("/consultar_continente_nome/<string:nome>", methods = ["GET"])
def consultar_continente_nome(nome):
    if nome == None or nome == "":
        return {"sucesso": False, "mensagem": "Formato de dados incorretos"}, 400
    else:
        try:
            with closing(conectar()) as con, closing(con.cursor()) as cursor:
                sql = "SELECT continente_id, nome FROM CONTINENTE WHERE nome LIKE '%%%s%%'" % (nome)
                cursor.execute(sql)
                rows = cursor.fetchall()
                if len(rows) == 0:
                    return {"sucesso": False, "mensagem": "Não encontrado"}, 404
                continentes = []
                for row in rows:
                    continentes.append({"id": row[0], "nome": row[1]})
                return {"sucesso": True, "continentes": continentes}, 200
        except Exception:
            return {"sucesso": False, "mensagem": "O servidor não está se comportando bem"}, 500

@blueprint_continente.route("/listar_continentes", methods = ["GET"])
def listar_continentes():
    return Model.listar_continente()

@blueprint_continente.route("/excluir_continente_id/<int:continente_id>", methods = ["DELETE"])
def excluir_continente_id(continente_id):
    if continente_id == None or continente_id <= 0:
        return {"sucesso": False, "mensagem": "Formato de dados incorretos"}, 400
    else:
        try:
            with closing(conectar()) as con, closing(con.cursor()) as cursor:
                sql = "DELETE FROM CONTINENTE WHERE continente_id = ?"
                cursor.execute(sql, [continente_id])
                con.commit()
                return {"sucesso": True, "continente_id": continente_id}, 200
        except Exception:
            return {"sucesso": False, "mensagem": "O servidor não está se comportando bem"}, 500