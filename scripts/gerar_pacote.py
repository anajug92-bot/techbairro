from pathlib import Path
import zipfile

PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_DIST = PASTA_PROJETO / "dist"

# Lê a versão diretamente do techbairro.py.
texto = (PASTA_PROJETO / "techbairro.py").read_text(encoding="utf-8")
prefixo = 'VERSAO = "'
inicio = texto.find(prefixo)
if inicio == -1:
    raise RuntimeError("VERSAO não encontrada no techbairro.py")
inicio += len(prefixo)
fim = texto.find('"', inicio)
VERSAO = texto[inicio:fim]

PASTA_DIST.mkdir(exist_ok=True)
saida = PASTA_DIST / f"TechBairro-{VERSAO}.zip"

IGNORAR_PASTAS = {"__pycache__", "dist"}
IGNORAR_EXTENSOES = {".db", ".pyc"}

with zipfile.ZipFile(saida, "w", zipfile.ZIP_DEFLATED) as pacote:
    for caminho in PASTA_PROJETO.rglob("*"):
        if not caminho.is_file():
            continue
        relativo = caminho.relative_to(PASTA_PROJETO)
        if any(parte in IGNORAR_PASTAS for parte in relativo.parts):
            continue
        if caminho.suffix in IGNORAR_EXTENSOES:
            continue
        pacote.write(caminho, relativo)

print(f"Pacote criado: {saida}")
