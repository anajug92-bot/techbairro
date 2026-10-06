# Importa a biblioteca Tkinter
import tkinter as tk

# Importa o messagebox para exibir mensagens e confirmações
from tkinter import messagebox

# NOVO NA AULA 14: importa o módulo do SQLite (já vem com o Python)
import sqlite3
import os


# ============================================================
# JANELA PRINCIPAL
# ============================================================

# Cria a janela principal da aplicação
janela = tk.Tk()

# Define o título da janela
janela.title("TechBairro — Cadastro de Cliente")

# Define o tamanho da janela
janela.geometry("480x460")

# Impede que a janela seja redimensionada
janela.resizable(False, False)


# ============================================================
# CLASSE CLIENTE
# ============================================================

# A classe Cliente representa um cliente dentro do sistema
class Cliente:

    # Método construtor
    #
    # NOVO NA AULA 14: o parâmetro id.
    # Ele fica None enquanto o cliente ainda não foi gravado no banco.
    def __init__(self, nome, telefone, email, endereco, id=None):

        # Armazena os dados do cliente
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    # Retorna os dados do cliente em uma única String
    def resumo(self):
        return f"{self.nome} | {self.telefone} | {self.email} | {self.endereco}"

    # Retorna as iniciais do nome
    #
    # Exemplo:
    # "João Victor Mendes" -> "JVM"
    def iniciais(self):

        # Divide o nome em partes
        partes = self.nome.split()

        # Pega a primeira letra de cada parte
        return "".join(
            parte[0].upper()
            for parte in partes
            if parte
        )


# ============================================================
# CLASSE GERENCIADOR DE CLIENTES
# ============================================================

# Classe responsável por armazenar e manipular os clientes
#
# NOVO NA AULA 14: em vez de uma lista em memória,
# os clientes agora ficam gravados no arquivo techbairro.db
class GerenciadorClientes:

    def __init__(self, caminho_banco="techbairro.db"):

        # Guarda o nome do arquivo do banco
        self.caminho_banco = caminho_banco

        # Cria a tabela (se ela ainda não existir)
        self.criar_tabela()


    # Abre uma conexão com o banco
    def conectar(self):

        return sqlite3.connect(self.caminho_banco)


    # Cria a tabela clientes projetada na Aula 13.
    #
    # IF NOT EXISTS: na primeira vez cria a tabela,
    # nas próximas não faz nada e não apaga os dados.
    def criar_tabela(self):

        conexao = self.conectar()

        conexao.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                email TEXT,
                endereco TEXT
            )
        """)

        conexao.commit()
        conexao.close()


    # ========================================================
    # CREATE
    # ========================================================

    # Grava um novo cliente no banco
    def adicionar(self, cliente):

        conexao = self.conectar()

        # Cada ? é trocado, na ordem, por um valor da tupla.
        # Nunca monte o SQL juntando textos com f-string!
        cursor = conexao.execute(
            "INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)",
            (cliente.nome, cliente.telefone, cliente.email, cliente.endereco)
        )

        # Sem o commit, o cliente não fica salvo no arquivo
        conexao.commit()

        # Guarda o id que o banco gerou para este cliente
        cliente.id = cursor.lastrowid

        conexao.close()


    # ========================================================
    # READ
    # ========================================================

    # Retorna todos os clientes cadastrados no banco
    def listar(self):

        conexao = self.conectar()

        # fetchall() devolve uma lista de tuplas, uma por linha
        linhas = conexao.execute(
            "SELECT id, nome, telefone, email, endereco FROM clientes ORDER BY nome"  # CORRIGIDO (BUG 3): antes era ORDER BY id
        ).fetchall()

        conexao.close()

        # Transforma cada linha do banco num objeto Cliente
        return [
            Cliente(nome, telefone, email, endereco, id)
            for (id, nome, telefone, email, endereco) in linhas
        ]


    # ========================================================
    # UPDATE
    # ========================================================

    # Atualiza um cliente existente.
    #
    # MUDOU NA AULA 14: recebe o id do cliente, e não mais o índice da lista.
    def atualizar(self, id_cliente, novo_cliente):

        conexao = self.conectar()

        cursor = conexao.execute(
            "UPDATE clientes SET nome = ?, telefone = ?, email = ?, endereco = ? WHERE id = ?",
            (novo_cliente.nome, novo_cliente.telefone, novo_cliente.email,
             novo_cliente.endereco, id_cliente)
        )

        conexao.commit()   # CORRIGIDO (BUG 4): sem commit, o close() descartava a alteração
        conexao.close()

        # rowcount diz quantas linhas foram alteradas
        return cursor.rowcount == 1


    # ========================================================
    # DELETE
    # ========================================================

    # Remove um cliente existente.
    #
    # MUDOU NA AULA 14: recebe o id do cliente, e não mais o índice da lista.
    def remover(self, id_cliente):

        conexao = self.conectar()

        # Atenção à vírgula: (id_cliente,) é uma tupla de um elemento
        cursor = conexao.execute(
            "DELETE FROM clientes WHERE id = ?",
            (id_cliente,)
        )

        conexao.commit()
        conexao.close()

        return cursor.rowcount == 1


    # Retorna a quantidade de clientes cadastrados
    def total(self):

        conexao = self.conectar()

        quantidade = conexao.execute(
            "SELECT COUNT(*) FROM clientes"
        ).fetchone()[0]

        conexao.close()

        return quantidade


# ============================================================
# OBJETO GERENCIADOR
# ============================================================

# Cria o objeto responsável por gerenciar os clientes
# (e cria o arquivo techbairro.db, se ele ainda não existir)
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")
print(f"Banco em uso: {CAMINHO_BANCO}")

gerenciador = GerenciadorClientes(CAMINHO_BANCO)


# Guarda o id do cliente que está sendo editado.
#
# None significa que estamos cadastrando um cliente novo.
#
# MUDOU NA AULA 14: antes era indice_em_edicao.
id_em_edicao = None


# ============================================================
# CABEÇALHO DA INTERFACE
# ============================================================

# Cria um Frame para funcionar como cabeçalho
cabecalho = tk.Frame(
    janela,
    bg="#2c3e50"
)

cabecalho.pack(
    side="top",
    fill="x"
)


# Cria o título do sistema
tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    fg="white",
    bg="#2c3e50",
    font=("Arial", 14, "bold"),
    pady=12
).pack()


# ============================================================
# FORMULÁRIO
# ============================================================

# Cria um Frame para organizar os campos
form = tk.Frame(janela)

form.pack(
    pady=20
)


# Lista com os nomes dos campos
campos = [
    "Nome",
    "Telefone",
    "E-mail",
    "Endereço"
]


# Dicionário que armazenará os campos Entry
entradas = {}


# Percorre os campos para criar os Labels e Entrys
for i, campo in enumerate(campos):

    # Cria o Label
    tk.Label(
        form,
        text=f"{campo}:"
    ).grid(
        row=i,
        column=0,
        sticky="e",
        padx=5,
        pady=6
    )


    # Cria o campo de entrada
    entrada = tk.Entry(
        form,
        width=30
    )

    entrada.grid(
        row=i,
        column=1,
        padx=5,
        pady=6
    )


    # Guarda o Entry no dicionário
    entradas[campo] = entrada


# ============================================================
# STATUS
# ============================================================

# Label utilizada para mostrar mensagens ao usuário
status = tk.Label(
    janela,
    text="Nenhum cliente cadastrado ainda",
    fg="gray",
    wraplength=440,
    justify="left"
)

status.pack(
    pady=(0, 5)
)


# Mostra a quantidade de clientes cadastrados
#
# MUDOU NA AULA 14: o total já vem do banco ao abrir a aplicação
contador = tk.Label(
    janela,
    text=f"Clientes cadastrados: {gerenciador.total()}"
)

contador.pack()


# ============================================================
# LIMPAR CAMPOS
# ============================================================

def limpar_campos():

    global id_em_edicao

    # Percorre todos os campos
    for entrada in entradas.values():

        # Apaga o conteúdo do campo
        entrada.delete(
            0,
            tk.END
        )

    # Sai do modo de edição
    id_em_edicao = None


# ============================================================
# VALIDAÇÃO DE E-MAIL
# ============================================================

def email_parece_valido(email):

    # Verifica se existe @ no e-mail
    if "@" not in email:

        return False


    # Divide o e-mail em usuário e domínio
    usuario, _, dominio = email.partition("@")


    # Verifica se existe usuário e ponto no domínio
    if usuario == "" or "." not in dominio:   # CORRIGIDO (BUG 2): era and, precisa ser or

        return False


    return True


# ============================================================
# SALVAR
# ============================================================

def salvar():

    global id_em_edicao


    # Pega os valores digitados nos campos
    valores = {
        campo: entradas[campo].get().strip()
        for campo in campos
    }


    # Cria uma lista contendo os campos vazios
    vazios = [
        campo
        for campo in campos          # CORRIGIDO (BUG 1): antes era campos[:3], o Endereço ficava de fora
        if valores[campo] == ""
    ]


    # Se houver algum campo vazio
    if vazios:

        status.config(
            text=f"Preencha o(s) campo(s): {', '.join(vazios)}",
            fg="red"
        )

        return


    # Verifica se o telefone possui somente números
    if not valores["Telefone"].isdigit():

        status.config(
            text="Telefone inválido: use somente números.",
            fg="red"
        )

        return


    # Verifica se o e-mail parece válido
    if not email_parece_valido(
        valores["E-mail"]
    ):

        status.config(
            text="E-mail inválido: use o formato nome@dominio.com",
            fg="red"
        )

        return


    # Cria um novo objeto Cliente
    cliente = Cliente(
        valores["Nome"],
        valores["Telefone"],
        valores["E-mail"],
        valores["Endereço"]
    )


    # ========================================================
    # CADASTRAR OU ATUALIZAR?
    # ========================================================

    # NOVO NA AULA 14: try/except captura qualquer erro do banco
    try:

        # Se não existe um id em edição,
        # significa que estamos cadastrando um novo cliente.
        if id_em_edicao is None:

            gerenciador.adicionar(cliente)

            status.config(
                text=f"Cliente '{cliente.nome}' salvo com sucesso!",
                fg="green"
            )


        # Caso contrário, estamos editando um cliente existente.
        else:

            gerenciador.atualizar(
                id_em_edicao,
                cliente
            )

            status.config(
                text=f"Cliente '{cliente.nome}' atualizado com sucesso!",
                fg="green"
            )

    except sqlite3.Error as erro:

        status.config(
            text=f"Erro ao salvar no banco: {erro}",
            fg="red"
        )

        return


    # Atualiza o contador
    contador.config(
        text=f"Clientes cadastrados: {gerenciador.total()}"
    )


    # Limpa o formulário
    limpar_campos()


# ============================================================
# CANCELAR
# ============================================================

def cancelar():

    # Limpa os campos
    limpar_campos()

    # Atualiza a mensagem de status
    status.config(
        text="Formulário limpo",
        fg="gray"
    )


# ============================================================
# CONSULTA DE CLIENTES
# ============================================================

def abrir_consulta():

    # Cria uma nova janela
    consulta = tk.Toplevel(janela)

    consulta.title(
        "Consulta de Clientes"
    )

    # Define um tamanho fixo para que os botões
    # fiquem sempre visíveis
    consulta.geometry(
        "500x380"
    )

    # Impede o redimensionamento
    consulta.resizable(
        False,
        False
    )


    # ========================================================
    # LISTBOX
    # ========================================================

    # Cria a lista de clientes
    lista = tk.Listbox(
        consulta,
        width=65,
        height=12
    )

    # Não utilizamos expand=True ou fill="both".
    # Dessa forma, a Listbox não ocupa todo o espaço
    # e os botões permanecem visíveis.
    lista.pack(
        padx=10,
        pady=10
    )


    # ========================================================
    # BARRA DE ROLAGEM
    # ========================================================

    # Cria a barra de rolagem
    scrollbar = tk.Scrollbar(
        consulta
    )

    scrollbar.pack(
        side="right",
        fill="y",
        pady=10
    )


    # Liga a Listbox à barra de rolagem
    lista.config(
        yscrollcommand=scrollbar.set
    )

    scrollbar.config(
        command=lista.yview
    )


    # ========================================================
    # ATUALIZAR LISTA
    # ========================================================

    def atualizar_lista():

        # Remove todos os itens da Listbox
        lista.delete(
            0,
            tk.END
        )


        # Busca os clientes cadastrados no banco
        try:

            clientes_cadastrados = gerenciador.listar()

        except sqlite3.Error as erro:

            lista.insert(
                tk.END,
                f"Erro ao ler o banco: {erro}"
            )

            return


        # Verifica se existem clientes
        if not clientes_cadastrados:

            lista.insert(
                tk.END,
                "Nenhum cliente cadastrado"
            )

            return


        # Percorre os clientes
        for cliente in clientes_cadastrados:

            # Adiciona o resumo do cliente na Listbox
            lista.insert(
                tk.END,
                cliente.resumo()
            )


    # ========================================================
    # EDITAR CLIENTE
    # ========================================================

    def editar_cliente():

        global id_em_edicao


        # Descobre qual cliente foi selecionado
        selecionado = lista.curselection()


        # Verifica se algum cliente foi selecionado
        if not selecionado:

            messagebox.showwarning(
                "Atenção",
                "Selecione um cliente antes de editar."
            )

            return


        # Pega a posição selecionada na Listbox
        indice = selecionado[0]


        # Busca o cliente pela posição.
        #
        # A Listbox mostra os clientes na mesma ordem
        # em que gerenciador.listar() devolve.
        cliente = gerenciador.listar()[
            indice
        ]


        # MUDOU NA AULA 14: guardamos o id do cliente,
        # que é fixo, e não a posição dele na lista.
        id_em_edicao = cliente.id


        # ====================================================
        # COLOCA OS DADOS NO FORMULÁRIO
        # ====================================================

        # Nome
        entradas["Nome"].delete(
            0,
            tk.END
        )

        entradas["Nome"].insert(
            0,
            cliente.nome
        )


        # Telefone
        entradas["Telefone"].delete(
            0,
            tk.END
        )

        entradas["Telefone"].insert(
            0,
            cliente.telefone
        )


        # E-mail
        entradas["E-mail"].delete(
            0,
            tk.END
        )

        entradas["E-mail"].insert(
            0,
            cliente.email
        )


        # Endereço
        entradas["Endereço"].delete(
            0,
            tk.END
        )

        entradas["Endereço"].insert(
            0,
            cliente.endereco
        )


        # Informa que estamos editando
        status.config(
            text=f"Editando cliente: {cliente.nome}",
            fg="blue"
        )


        # Fecha a janela de consulta
        consulta.destroy()


    # ========================================================
    # EXCLUIR CLIENTE
    # ========================================================

    def excluir_cliente():

        # Descobre qual cliente foi selecionado
        selecionado = lista.curselection()


        # Verifica se algum cliente foi selecionado
        if not selecionado:

            messagebox.showwarning(
                "Atenção",
                "Selecione um cliente antes de excluir."
            )

            return


        # Pega a posição selecionada
        indice = selecionado[0]


        # Busca o cliente pela posição
        cliente = gerenciador.listar()[indice]


        # ====================================================
        # CONFIRMAÇÃO
        # ====================================================

        confirmar = messagebox.askyesno(      # CORRIGIDO (BUG 5): guardar a resposta
            "Confirmar exclusão",

            f"Tem certeza que deseja excluir o cadastro de "
            f"{cliente.nome}?\n\n"
            f"Essa ação não pode ser desfeita."
        )


        # CORRIGIDO (BUG 5): só remove se o usuário responder Sim
        if confirmar:

            # Remove pelo id do cliente
            try:

                gerenciador.remover(
                    cliente.id
                )

            except sqlite3.Error as erro:

                messagebox.showerror(
                    "Erro no banco",
                    f"Não foi possível excluir o cliente.\n{erro}"
                )

                return


            # Atualiza a lista
            atualizar_lista()


            # Atualiza o contador da janela principal
            contador.config(
                text=f"Clientes cadastrados: {gerenciador.total()}"
            )


            # Atualiza o status
            status.config(
                text=f"Cliente '{cliente.nome}' excluído com sucesso!",
                fg="green"
            )


    # ========================================================
    # BOTÕES DA CONSULTA
    # ========================================================

    # Frame para organizar os botões
    botoes_consulta = tk.Frame(
        consulta
    )

    botoes_consulta.pack(
        pady=10
    )


    # Botão Editar
    tk.Button(
        botoes_consulta,
        text="Editar selecionado",
        width=18,
        command=editar_cliente
    ).grid(
        row=0,
        column=0,
        padx=5
    )


    # Botão Excluir
    tk.Button(
        botoes_consulta,
        text="Excluir selecionado",
        width=18,
        command=excluir_cliente
    ).grid(
        row=0,
        column=1,
        padx=5
    )


    # Preenche a Listbox
    atualizar_lista()


# ============================================================
# BOTÕES DA JANELA PRINCIPAL
# ============================================================

botoes = tk.Frame(
    janela
)

botoes.pack(
    pady=10
)


# Botão Salvar
tk.Button(
    botoes,
    text="Salvar",
    width=12,
    command=salvar
).grid(
    row=0,
    column=0,
    padx=5
)


# Botão Cancelar
tk.Button(
    botoes,
    text="Cancelar",
    width=12,
    command=cancelar
).grid(
    row=0,
    column=1,
    padx=5
)


# Botão Consultar
#
# A edição e a exclusão ficam dentro
# da tela de consulta.
tk.Button(
    botoes,
    text="Consultar",
    width=12,
    command=abrir_consulta
).grid(
    row=0,
    column=2,
    padx=5
)


# ============================================================
# VERSÃO
# ============================================================

# Exibe a versão do sistema no canto inferior direito
#
# Versão 3.2 da Aula 16 com o caminho completo do banco
tk.Label(
    janela,
    text="v3.2",
    fg="gray"
).place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)


# ============================================================
# INICIALIZAÇÃO
# ============================================================

# Mantém a aplicação aberta
janela.mainloop()