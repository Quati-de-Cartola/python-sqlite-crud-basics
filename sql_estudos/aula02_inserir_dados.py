# importando biblioteca
import sqlite3

# conectando ao banco
conexao = sqlite3.connect('banco_dados/banco_dados.db')

# criando cursor
cursor = conexao.cursor()

# inserindo alunos
cursor.execute("INSERT INTO aluno (nome, idade) VALUES(?, ?)", ("Ana", 20))
cursor.execute("INSERT INTO aluno (nome, idade) VALUES(?, ?)", ("Carlos", 22))
cursor.execute("INSERT INTO aluno (nome, idade) VALUES(?, ?)", ("Marina", 19))

# salvando
conexao.commit()

# fechando
cursor.close()
conexao.close()