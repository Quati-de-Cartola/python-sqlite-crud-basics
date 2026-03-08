import sqlite3

# abrindo conexão
conexao = sqlite3.connect('banco_dados/banco_dados.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM aluno')
dados = cursor.fetchall()

for d in dados:
    print(d)

cursor.close()
conexao.close()