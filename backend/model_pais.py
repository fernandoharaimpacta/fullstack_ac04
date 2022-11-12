from flask import Blueprint, request, jsonify
from contextlib import closing
import sqlite3

def conectar():
    return sqlite3.connect("geo.db")

class ModelPais ():
    def adicionar_pais():
        content_type = request.headers.get('Content-Type')
        json = ""
        if (content_type == 'application/json'):
            json = request.json
        if json == "":
            return {"sucesso": False, "mensagem": "Formato de dados incorretos"}, 400
        else:
            try:
                with closing(conectar()) as con, closing(con.cursor()) as cursor:
                    sql = "INSERT INTO PAIS (continente_id, nome, capital, bandeira, latitude, longitude, populacao) VALUES (?, ?, ?, ?, ?, ?, ?)"
                    cursor.execute(sql, [json["continente_id"], json["nome"], json["capital"], json["bandeira"], json["latitude"], json["longitude"], json["populacao"]])
                    pais_id = cursor.lastrowid
                    con.commit()
                    return {"sucesso": True, "pais": {"pais_id": pais_id, "continente_id": json["continente_id"], "nome": json["nome"], "capital": json["capital"], "bandeira": json["bandeira"], "latitude": json["latitude"], "longitude": json["longitude"], "populacao": json["populacao"]}}, 200
            except Exception as ex:
                return {"sucesso": False, "mensagem": str(ex)}, 500

    def atualizar_pais():
        content_type = request.headers.get('Content-Type')
        json = ""
        if (content_type == 'application/json'):
            json = request.json
        if json == "":
            return {"sucesso": False, "mensagem": "Formato de dados incorretos"}, 400
        else:
            try:
                with closing(conectar()) as con, closing(con.cursor()) as cursor:
                    sql = "UPDATE PAIS SET continente_id = ?, nome = ?, capital = ?, bandeira = ?, latitude = ?, longitude = ?, populacao = ? WHERE pais_id = ?"
                    cursor.execute(sql, [json["continente_id"], json["nome"], json["capital"], json["bandeira"], json["latitude"], json["longitude"], json["populacao"], json["pais_id"]])
                    con.commit()
                    return {"sucesso": True, "pais": json}, 200
            except Exception:
                return {"sucesso": False, "mensagem": "O servidor não está se comportando bem"}, 500

    def consultar_pais_id(pais_id):
        if pais_id == None or pais_id <= 0:
            return {"sucesso": False, "mensagem": "Formato de dados incorretos"}, 400
        else:
            try:
                with closing(conectar()) as con, closing(con.cursor()) as cursor:
                    sql = "SELECT pais_id, continente_id, nome, capital, bandeira, latitude, longitude, populacao FROM PAIS WHERE pais_id = ?"
                    cursor.execute(sql, [pais_id])
                    row = cursor.fetchone()
                    if row == None:
                        return {"sucesso": False, "mensagem": "Não encontrado"}, 404
                    return {"sucesso": True, "pais": {"pais_id": row[0], "continente_id": row[1], "nome": row[2], "capital": row[3], "bandeira": row[4], "latitude": row[5], "longitude": row[6], "populacao": row[7]}}, 200
            except Exception:
                return {"sucesso": False, "mensagem": "O servidor não está se comportando bem"}, 500

    def consultar_pais_nome(nome):
        if nome == None or nome == "":
            return {"sucesso": False, "mensagem": "Formato de dados incorretos"}, 400
        else:
            try:
                with closing(conectar()) as con, closing(con.cursor()) as cursor:
                    sql = "SELECT pais_id, continente_id, nome, capital, bandeira, latitude, longitude, populacao FROM PAIS WHERE nome LIKE '%%%s%%'" % (nome)
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    if len(rows) == 0:
                        return {"sucesso": False, "mensagem": "Não encontrado"}, 404
                    paises = []
                    for row in rows:
                        paises.append({"pais_id": row[0], "continente_id": row[1], "nome": row[2], "capital": row[3], "bandeira": row[4], "latitude": row[5], "longitude": row[6], "populacao": row[7]})
                    return {"sucesso": True, "paises": paises}, 200
            except Exception:
                return {"sucesso": False, "mensagem": "O servidor não está se comportando bem"}, 500

    def listar_paises():
        try:
            with closing(conectar()) as con, closing(con.cursor()) as cursor:
                sql = "SELECT pais_id, continente_id, nome, capital, bandeira, latitude, longitude, populacao FROM PAIS"
                cursor.execute(sql)
                rows = cursor.fetchall()
                if len(rows) == 0:
                    return {"sucesso": False, "mensagem": "Não encontrado"}, 404
                paises = []
                for row in rows:
                    paises.append({"pais_id": row[0], "continente_id": row[1], "nome": row[2], "capital": row[3], "bandeira": row[4], "latitude": row[5], "longitude": row[6], "populacao": row[7]})
                return {"sucesso": True, "paises": paises}, 200
        except Exception as ex:
            return {"sucesso": False, "mensagem": str(ex)}, 500

    def excluir_pais_id(pais_id):
        if pais_id == None or pais_id <= 0:
            return {"sucesso": False, "mensagem": "Formato de dados incorretos"}, 400
        else:
            try:
                with closing(conectar()) as con, closing(con.cursor()) as cursor:
                    sql = "DELETE FROM PAIS WHERE pais_id = ?"
                    cursor.execute(sql, [pais_id])
                    con.commit()
                    return {"sucesso": True, "pais_id": pais_id}, 200
            except Exception:
                return {"sucesso": False, "mensagem": "O servidor não está se comportando bem"}, 500