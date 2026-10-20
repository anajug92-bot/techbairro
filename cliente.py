class Cliente:
    def __init__(self, nome, telefone, email, endereco, id=None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.id = id