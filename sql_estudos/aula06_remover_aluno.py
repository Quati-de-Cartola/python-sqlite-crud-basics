import sqlite3

# estabelecendo conexão
conexao = sqlite3.connect('banco_dados/banco_dados.db')
cursor = conexao.cursor()

# pedindo nome do aluno
nome = input('Digite o Nome do Aluno: ')

# verificando se ele existe
cursor.execute('SELECT * FROM aluno WHERE nome = ?', (nome,))
dados = cursor.fetchall()

if dados:
    # executando
    cursor.execute('DELETE FROM aluno WHERE nome = ?', (nome,))
    conexao.commit()
    print(f'{nome} foi removido/a do Banco de Dados.')
else:
    print('Esse aluno não existe no banco de dados.')

# fechando
cursor.close()
conexao.close()