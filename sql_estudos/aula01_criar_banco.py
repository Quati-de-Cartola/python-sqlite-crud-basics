import sqlite3

# função de fechar conexão
def fechando():
    cursor.close()
    conexao.close()

# criando uma conexão
conexao = sqlite3.connect('banco_dados/banco_dados.db')

# criando um cursor
cursor = conexao.cursor()

# criando tabela de alunos com tipos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aluno (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
''')

# salvando alterações
conexao.commit()

fechando()