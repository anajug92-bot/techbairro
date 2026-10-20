from cliente import Cliente
from validacao import ValidadorCliente

validador = ValidadorCliente()


def cliente_valido():
    return Cliente(
        "Ana Souza",
        "61999990001",
        "ana@email.com",
        "Rua 1 Casa 2"
    )


# T1: cliente com todos os dados corretos
def teste_cliente_valido():
    assert validador.validar(cliente_valido()) is None


# T2: endereço vazio
def teste_endereco_vazio():
    cliente = cliente_valido()
    cliente.endereco = ""

    assert validador.validar(cliente) == (
        "Preencha o(s) campo(s): Endereço"
    )


# T3: telefone com letras
def teste_telefone_com_letras():
    cliente = cliente_valido()
    cliente.telefone = "6199ABC0001"

    assert validador.validar(cliente) == (
        "Telefone inválido: use somente números."
    )


# T4: e-mail sem ponto no domínio
def teste_email_sem_ponto():
    cliente = cliente_valido()
    cliente.email = "ana@email"

    assert validador.validar(cliente) == "E-mail inválido."


# T5: nome e telefone vazios
def teste_nome_e_telefone_vazios():
    cliente = cliente_valido()
    cliente.nome = ""
    cliente.telefone = ""

    assert validador.validar(cliente) == (
        "Preencha o(s) campo(s): Nome, Telefone"
    )


# T6: e-mail sem nome antes do @
def teste_email_sem_nome():
    assert validador.email_parece_valido("@email.com") is False


if __name__ == "__main__":
    for nome, funcao in list(globals().items()):
        if nome.startswith("teste_"):
            funcao()
            print("OK", nome)

    print("Todos os testes passaram.")