import sqlite3
import os

PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")

clientes_da_planilha = [
    ("Carlos Pereira", "61988887777", "carlos@email.com", "Quadra 3 Casa 10"),
    ("Beatriz Lima", "61977776666", "bia@email.com", "Rua 5 Casa 2"),
    ("Diego Martins", "61966665555", "diego@email", "Rua 8 Casa 1"),
    ("Eduarda Rocha", "61955554444", "eduarda@email.com", ""),
    ("Fábio Nunes", "6194444ABCD", "fabio@email.com", "Rua 9 Casa 4"),
    ("Gabriela Souza", "61988887777", "gabi@email.com", "Rua 2 Casa 7"),
    ("Helena Dias", "61933332222", "helena@email.com", "Rua 7 Casa 3"),
]

conexao = sqlite3.connect(CAMINHO_BANCO)

conexao.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    endereco TEXT
)
""")

conexao.executemany(
    """
    INSERT INTO clientes (nome, telefone, email, endereco)
    VALUES (?, ?, ?, ?)
    """,
    clientes_da_planilha
)

conexao.commit()
conexao.close()

print(f"{len(clientes_da_planilha)} clientes importados para {CAMINHO_BANCO}")