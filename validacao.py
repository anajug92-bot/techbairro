class ValidadorCliente:

    def validar(self, cliente):
        # RF01: verifica os campos vazios
        vazios = []

        if cliente.nome == "":
            vazios.append("Nome")

        if cliente.telefone == "":
            vazios.append("Telefone")

        if cliente.email == "":
            vazios.append("E-mail")

        if cliente.endereco == "":
            vazios.append("Endereço")

        if vazios:
            return f"Preencha o(s) campo(s): {', '.join(vazios)}"

        # RF02: verifica se o telefone contém somente números
        if not cliente.telefone.isdigit():
            return "Telefone inválido: use somente números."

        # RF03: verifica o formato do e-mail
        if not self.email_parece_valido(cliente.email):
            return "E-mail inválido."

        return None

    def email_parece_valido(self, email):
        partes = email.split("@")

        if len(partes) != 2:
            return False

        nome, dominio = partes

        if not nome or not dominio:
            return False

        if "." not in dominio:
            return False

        if dominio.startswith(".") or dominio.endswith("."):
            return False

        return True