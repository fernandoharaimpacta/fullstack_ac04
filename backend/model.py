from flask import Blueprint, request, jsonify
from contextlib import closing
import sqlite3

def conectar():
    return sqlite3.connect("geo.db")

class Model ():
    def listar_continente():
        try:
            with closing(conectar()) as con, closing(con.cursor()) as cursor:
                sql = "SELECT continente_id, nome FROM CONTINENTE"
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