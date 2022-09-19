#CRUD
#importando o sql lite
import sqlite3 as lite



#criando conexão
con = lite.connect('dados.db')

 #INSERT
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventorio(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


#UPDATE
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventorio SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


def deletar_form(i):
#DELETAR DADOS
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventorio WHERE id=?"
        cur.execute(query, i)


    #VER DADOS
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventorio"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)

    return ver_dados

#VER DADOS
def ver_item(id):
    ver_dados_individuais = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventorio WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individuais.append(row)