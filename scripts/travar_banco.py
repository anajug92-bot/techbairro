import sqlite3
import os

PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")

conexao = sqlite3.connect(
    CAMINHO_BANCO,
    isolation_level=None
)

conexao.execute("BEGIN EXCLUSIVE")

input(
    "Banco TRAVADO. Teste a TechBairro agora "
    "e aperte Enter aqui para liberar..."
)

conexao.execute("ROLLBACK")
conexao.close()

print("Banco liberado.")