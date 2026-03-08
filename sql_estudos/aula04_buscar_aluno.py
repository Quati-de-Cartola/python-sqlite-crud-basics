import sqlite3

conexao = sqlite3.connect('banco_dados/banco_dados.db')
cursor = conexao.cursor()

# perguntando nome de usuário
nome = input('Digite o nome do Aluno a ser Encontrado:\n> ')

cursor.execute("SELECT * FROM aluno WHERE nome = ?", (nome,))
dados = cursor.fetchall() # pegando os dados obtidos

if dados:
    for d in dados:
        print('id, nome e idade')
        print(d)
else:
    print('Este aluno não existe no Banco de Dados.')

cursor.close()
conexao.close()