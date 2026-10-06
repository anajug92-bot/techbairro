# VERIFICAR BANCO (Aula 16) - lê o techbairro.db direto, sem passar pela TechBairro
import sqlite3
import os

PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")
print(f"Banco verificado: {CAMINHO_BANCO}")
print()

conexao = sqlite3.connect(CAMINHO_BANCO)
linhas = conexao.execute(
    "SELECT id, nome, telefone, email, endereco FROM clientes ORDER BY id"
).fetchall()
print("id | nome | telefone | email | endereco")
for linha in linhas:
    print(" | ".join(str(valor) for valor in linha))
print()

auditorias = {
    "A1 Total de clientes":
        "SELECT COUNT(*) FROM clientes",
    "A2 Campos vazios":
        """SELECT id, nome FROM clientes
           WHERE TRIM(nome) = '' OR TRIM(telefone) = ''
           OR TRIM(email) = '' OR TRIM(endereco) = ''""",
    "A3 Telefone com letras ou símbolos":
        "SELECT id, nome, telefone FROM clientes WHERE telefone GLOB '*[^0-9]*'",
    # A4: >=1 caractere, @, >=1 caractere, ponto, >=1 caractere
    "A4 E-mail fora do formato":
        "SELECT id, nome, email FROM clientes WHERE email NOT LIKE '%_@_%._%'",
    # A5: agrupa por telefone e mostra só grupos com mais de 1 cliente
    "A5 Telefone repetido":
        """SELECT telefone, COUNT(*) FROM clientes
           GROUP BY telefone HAVING COUNT(*) > 1""",
}
for titulo, sql in auditorias.items():
    resultado = conexao.execute(sql).fetchall()
    print(titulo)
    if not resultado:
        print("  nenhum problema encontrado")
    for linha in resultado:
        print("  ", linha)
    print()
conexao.close()