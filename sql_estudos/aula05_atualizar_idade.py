import sqlite3

# conexão
conexao = sqlite3.connect('banco_dados/banco_dados.db')
cursor = conexao.cursor()

# verificando nome do aluno
nome = input('Digite o nome do Aluno: ')
cursor.execute('SELECT * FROM aluno WHERE nome = ?', (nome,))
dados = cursor.fetchall()

# verificando nova idade
if dados:
    nova_idade = input(f'Digite a idade nova de {nome}: ')

    cursor.execute('UPDATE aluno SET idade = ? WHERE nome = ?', (int(nova_idade), nome))

    print(f'Aluno {nome} atualizado com sucesso!')
    conexao.commit()
else:
    print('Nenhum aluno foi encontrado.')

cursor.close()
conexao.close()