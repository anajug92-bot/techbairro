# TechBairro

A TechBairro é um sistema desenvolvido em Python para cadastrar, consultar, alterar e excluir clientes, facilitando o gerenciamento das informações da associação de moradores.

**Versão atual:** 3.3.0 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md).

## Funcionalidades

- Cadastro, consulta, alteração e exclusão de clientes.
- Armazenamento dos dados em banco de dados SQLite.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows |
| Python | Python 3 instalado |
| Tkinter | Necessário para a interface gráfica |
| Bibliotecas externas | Nenhuma |
| Internet | Necessária para baixar o projeto |

## Instalação

1. Baixe o projeto pelo GitHub, clicando em **Code → Download ZIP**, e extraia os arquivos.
2. Abra o terminal na pasta do projeto e execute:

```bash
python -m pip install -r requirements.txt
```

3. Inicie o programa com:

```bash
python techbairro.py
```

A janela principal será aberta e o terminal mostrará a mensagem `Banco em uso`.

## Configuração do banco de dados

O banco de dados `techbairro.db` armazena os clientes e fica na pasta do projeto, conforme configurado no código. Ele é criado quando necessário. A mensagem `Banco em uso`, exibida no terminal, informa o caminho do banco utilizado.

O banco não deve ser enviado ao GitHub, pois pode conter dados pessoais. Para fazer uma cópia de segurança, feche o programa e copie o arquivo para um local seguro.

## Como usar

Consulte o [Manual de uso](docs/manual_de_uso.md) para aprender a cadastrar, consultar, alterar e excluir clientes.

## Estrutura do projeto

- `techbairro.py`: arquivo principal do sistema.
- `techbairro.db`: banco de dados dos clientes.
- `requirements.txt`: informações sobre as dependências.
- `CHANGELOG.md`: histórico de alterações.
- `docs/manual_de_uso.md`: instruções para utilizar o sistema.

## Autor

Ana Julia Gomes — SENAC DF.
