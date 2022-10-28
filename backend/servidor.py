from flask import Flask
from contextlib import closing
import sqlite3
from blueprint_continente import blueprint_continente
from blueprint_pais import blueprint_pais
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(blueprint_continente, url_prefix="/v1/continente")
app.register_blueprint(blueprint_pais, url_prefix="/v1/pais")

sql_create = """
CREATE TABLE IF NOT EXISTS CONTINENTE (
    CONTINENTE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS PAIS (
    PAIS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CONTINENTE_ID INTEGER NOT NULL,
    NOME VARCHAR(50) NOT NULL UNIQUE,
    CAPITAL VARCHAR(50) NOT NULL,
    BANDEIRA VARCHAR(200) NULL,
    LATITUDE VARCHAR(50) NULL,
    LONGITUDE VARCHAR(50) NULL,
    POPULACAO FLOAT NULL
);
"""

def conectar():
    return sqlite3.connect("geo.db")

def criar_bd():
    with closing(conectar()) as con:
        con.executescript(sql_create)
        con.commit()

if __name__ == "__main__":
    criar_bd()
    app.run(port = 9000)