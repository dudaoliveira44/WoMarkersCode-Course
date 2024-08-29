# Nome: Eduarda do Carmo Oliveira / Squad: Jaqueline Goes

import sqlite3
import pandas as pd

conexao = sqlite3.connect('BancoAlunos') # Conexão com o arquivo Sqlite
cursor = conexao.cursor() # Nova variável para o banco de dados

# 1 - Criar tabela alunos
#cursor.execute(' CREATE TABLE alunos( id INT , nome VARCHAR(100), idade INT, curso VARCHAR(100));')

'''
# 2 - Inserir alunos
cursor.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Carolina", 22, "Engenharia")')
cursor.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Pedro", 20, "Medicina")')
cursor.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Laura", 18, "Biologia")')
cursor.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Kaio", 19, "Engenharia")')
cursor.execute(' INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Ana Clara", 27, "Letras")')
'''

# 3a - Selecionar todos os registros da tabela "Alunos"
# dados = cursor.execute(' SELECT * FROM alunos')

# 3b - Selecionar o nome e a idade dos alunos com mais de 20 anos
# dados = cursor.execute(' SELECT nome, idade FROM alunos WHERE idade>20')

# 3c - Selecionar os alunos do curso "Engenharia" em ordem alfabética
# dados = cursor.execute(' SELECT nome FROM alunos WHERE curso="Engenharia" ORDER BY nome')

'''
for selecao in dados:
    print(selecao)
'''

# 3d - Contar o número total de alunos na tabela
'''
lista_alunos = cursor.execute(' SELECT * FROM alunos')

total_alunos = 0
for n in lista_alunos:
    total_alunos+=1

print(f'A tabela possui {total_alunos} alunos registrados.')
'''

# 4a - Atualizar idade de um aluno
#cursor.execute('UPDATE alunos SET idade=23 WHERE nome="Carolina"')

# 4b - Remover aluno pelo ID
#cursor.execute('DELETE FROM alunos where id=5')

# 5 - Criar tabela Clientes
#cursor.execute(' CREATE TABLE clientes( id INT , nome VARCHAR(100), idade INT, saldo FLOAT);')

'''
# Inserir clientes
cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Carolina", 31, 22.75)')
cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Pedro", 35, 78.84)')
cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Laura", 62, 14.21)')
cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Kaio", 19, 37.40)')
cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Ana Clara", 27, 50.00)')
'''

# 6a - Selecionar o nome e a idade dos clientes com mais de 30 anos
# dados = cursor.execute(' SELECT nome, idade FROM clientes WHERE idade>30')

'''
for selecao2 in dados2:
    print(selecao2)
'''

# 6b - Calcular o saldo médio dos clientes
#cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
#saldo_medio = cursor.fetchone()[0]

#print(f'O saldo médio dos clientes é R$ {saldo_medio:.2f}')

# 6c - Encontrar cliente com saldo máximo
#cursor.execute('SELECT MAX(saldo),nome AS maxsaldo_cliente FROM clientes')
#maxsaldo_cliente = cursor.fetchone()[1]

#print(f'O cliente com saldo máximo é {maxsaldo_cliente}')

# 6d - Contar clientes com saldo acima de 1000

# inserindo mais clientes com saldo maior que 1000 para contabilizar
#cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo) VALUES (6, "Sara", 37, 450.56)')
#cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo) VALUES (7, "Julio", 49, 1567.99)')
#cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo) VALUES (8, "Fabio", 49, 2000)')
#cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo) VALUES (9, "Tamara", 37, 1059.92)')
#cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo) VALUES (10, "Maria", 49, 152.00)')

'''
lista_clientes = cursor.execute(' SELECT * FROM clientes WHERE saldo>1000')

total_clientes = 0
for n in lista_clientes:
    total_clientes+=1

print(f'A tabela possui {total_clientes} clientes com saldo acima de 1000.')
'''

# 7a - Atualizar saldo de cliente
#cursor.execute('UPDATE clientes SET saldo=300 WHERE nome="Sara"')

# 7b - Remover cliente pelo ID
#cursor.execute('DELETE FROM clientes where id=8')

# 8 - Juntar tabelas

# Criar tabela compras
#cursor.execute(' CREATE TABLE compras( id INTEGER PRIMARY KEY, cliente_id INT, produto TEXT, valor REAL, FOREIGN KEY(cliente_id) REFERENCES clientes(id) );')

# Inserir compras associadas a clientes existentes
#cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (1, "Notebook", 4500.00)')
#cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (2, "Smartphone", 1870.00)')
#cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (3, "Tablet", 750.00)')
#cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (4, "SmartTV", 2999.99)')
#cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (5, "SmartWatch", 499.90)')

# Consulta para exibir nome do cliente, produto e valor da compra
#cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id;')

# Exibir os resultados
''''
compras = cursor.fetchall()
for compra in compras:
    print(f'Cliente: {compra[0]}, Produto: {compra[1]}, Valor: R${compra[2]:.2f}')
'''

# Confirmar (commit) as transações
conexao.commit()

# Fechar a conexão com o banco de dados
conexao.close()

