#CRUD
#importando o sql lite
import sqlite3 as lite



#criando conexão
con = lite.connect('dados.db')

dados = ['sofa', 'sala', 'marrom', 'kkkkkk', '19/09/2021', '100', '1234', 'c:/imagens']
'''#INSERT
with con:
    cur = con.cursor()
    query = "INSERT INTO inventorio(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
    cur.execute(query, dados)


atualizar_dados = ['sofa', 'Cozinha', 'marrom', 'kkkkkk', '19/09/2021', '100', '1234', 'c:/imagens', 1]
#UPDATE
with con:
    cur = con.cursor()
    query = "UPDATE inventorio SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
    cur.execute(query, atualizar_dados)'''


deletar_dados = str(1)
#DELETAR DADOS
with con:
    cur = con.cursor()
    query = "DELETE FROM inventorio WHERE id=?"
    cur.execute(query, deletar_dados)


ver_dados = []
#VER DADOS
with con:
    cur = con.cursor()
    query = "SELECT * FROM inventorio"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        ver_dados.append(row)

print(ver_dados)