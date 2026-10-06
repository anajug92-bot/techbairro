import os
import tempfile

from techbairro_logica import (
    Cliente,
    GerenciadorClientes,
    email_parece_valido
)


def teste_email_valido():
    assert email_parece_valido("ana@email.com") is True


def teste_email_sem_ponto():
    assert email_parece_valido("ana@email") is False


def teste_email_sem_usuario():
    assert email_parece_valido("@email.com") is False


def teste_cadastrar_cliente():
    with tempfile.NamedTemporaryFile(delete=False) as arquivo:
        banco = arquivo.name

    try:
        gerenciador = GerenciadorClientes(banco)

        cliente = Cliente(
            "Ana Souza",
            "61999990001",
            "ana@email.com",
            "Rua 10"
        )

        gerenciador.adicionar(cliente)

        clientes = gerenciador.listar()

        assert len(clientes) == 1
        assert clientes[0].nome == "Ana Souza"
        assert clientes[0].telefone == "61999990001"

    finally:
        if os.path.exists(banco):
            os.remove(banco)


def teste_ordenacao_alfabetica():
    with tempfile.NamedTemporaryFile(delete=False) as arquivo:
        banco = arquivo.name

    try:
        gerenciador = GerenciadorClientes(banco)

        gerenciador.adicionar(
            Cliente(
                "Carlos",
                "61999990001",
                "carlos@email.com",
                "Rua 1"
            )
        )

        gerenciador.adicionar(
            Cliente(
                "Ana",
                "61999990002",
                "ana@email.com",
                "Rua 2"
            )
        )

        gerenciador.adicionar(
            Cliente(
                "Bruno",
                "61999990003",
                "bruno@email.com",
                "Rua 3"
            )
        )

        clientes = gerenciador.listar()

        nomes = [cliente.nome for cliente in clientes]

        assert nomes == ["Ana", "Bruno", "Carlos"]

    finally:
        if os.path.exists(banco):
            os.remove(banco)


def teste_edicao_persistente():
    with tempfile.NamedTemporaryFile(delete=False) as arquivo:
        banco = arquivo.name

    try:
        gerenciador = GerenciadorClientes(banco)

        cliente = Cliente(
            "Joao",
            "61999990004",
            "joao@email.com",
            "Rua 4"
        )

        gerenciador.adicionar(cliente)

        cliente_editado = Cliente(
            "Joao Silva",
            "61999991111",
            "joao@email.com",
            "Rua 5"
        )

        resultado = gerenciador.atualizar(
            cliente.id,
            cliente_editado
        )

        assert resultado is True

        # Cria outro gerenciador usando o mesmo banco,
        # simulando fechar e abrir a aplicação.
        novo_gerenciador = GerenciadorClientes(banco)

        clientes = novo_gerenciador.listar()

        assert len(clientes) == 1
        assert clientes[0].nome == "Joao Silva"
        assert clientes[0].telefone == "61999991111"
        assert clientes[0].endereco == "Rua 5"

    finally:
        if os.path.exists(banco):
            os.remove(banco)


def teste_exclusao():
    with tempfile.NamedTemporaryFile(delete=False) as arquivo:
        banco = arquivo.name

    try:
        gerenciador = GerenciadorClientes(banco)

        cliente = Cliente(
            "Pedro",
            "61999990005",
            "pedro@email.com",
            "Rua 6"
        )

        gerenciador.adicionar(cliente)

        assert gerenciador.total() == 1

        resultado = gerenciador.remover(cliente.id)

        assert resultado is True
        assert gerenciador.total() == 0

    finally:
        if os.path.exists(banco):
            os.remove(banco)


if __name__ == "__main__":
    teste_email_valido()
    teste_email_sem_ponto()
    teste_email_sem_usuario()
    teste_cadastrar_cliente()
    teste_ordenacao_alfabetica()
    teste_edicao_persistente()
    teste_exclusao()

    print("Todos os testes automatizados passaram!")