import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='eletric_shop'
)

cursor = conn.cursor()

# Executar uma consulta
cursor.execute("SELECT * FROM sua_tabela")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

# Fechar a conexão
cursor.close()
conn.close()
