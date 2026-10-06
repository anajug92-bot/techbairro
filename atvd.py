import tkinter as tk
from tkinter import messagebox
import sqlite3


class Cliente:
    def __init__(self, nome, telefone, email, endereco, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return (
            (f"[{self.id}] " if self.id is not None else "")
            + f"Nome: {self.nome} | "
            + f"Telefone: {self.telefone} | "
            + f"E-mail: {self.email} | "
            + f"Endereço: {self.endereco}"
        )

# CLASSE GERENCIADORCLIENTES
class GerenciadorClientes:
    def __init__(self, caminho_banco="techbairro.db"):
        self.caminho_banco = caminho_banco
        self.clientes = []
        self.clientes_removidos = []

        try:
            self.criar_tabela()
        except sqlite3.Error as e:
            messagebox.showerror("Erro ao criar tabela", str(e))

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)

    def criar_tabela(self):
        sql = (
            "CREATE TABLE IF NOT EXISTS clientes ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "nome TEXT NOT NULL, "
            "telefone TEXT NOT NULL, "
            "email TEXT NOT NULL, "
            "endereco TEXT NOT NULL"
            ")"
        )

        with self.conectar() as conn:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()

    # CADASTRAR
    def adicionar(self, cliente):
        try:
            with self.conectar() as conn:
                cur = conn.cursor()

                cur.execute(
                    "INSERT INTO clientes "
                    "(nome, telefone, email, endereco) "
                    "VALUES (?, ?, ?, ?)",
                    (
                        cliente.nome,
                        cliente.telefone,
                        cliente.email,
                        cliente.endereco
                    )
                )

                conn.commit()
                cliente.id = cur.lastrowid

            return cliente

        except sqlite3.Error as e:
            messagebox.showerror(
                "Erro ao inserir cliente",
                str(e)
            )
            raise

    # LISTAR
    def listar(self):
        try:
            resultados = []

            with self.conectar() as conn:
                cur = conn.cursor()

                cur.execute(
                    "SELECT id, nome, telefone, email, endereco "
                    "FROM clientes ORDER BY id"
                )

                for row in cur.fetchall():
                    cid, nome, telefone, email, endereco = row

                    resultados.append(
                        Cliente(
                            nome,
                            telefone,
                            email,
                            endereco,
                            id=cid
                        )
                    )

            return resultados

        except sqlite3.Error as e:
            messagebox.showerror(
                "Erro ao listar clientes",
                str(e)
            )
            raise

    # ATUALIZAR
    def atualizar(self, cliente):
        if cliente.id is None:
            raise ValueError(
                "Cliente sem id não pode ser atualizado"
            )

        try:
            with self.conectar() as conn:
                cur = conn.cursor()

                cur.execute(
                    "UPDATE clientes "
                    "SET nome=?, telefone=?, email=?, endereco=? "
                    "WHERE id=?",
                    (
                        cliente.nome,
                        cliente.telefone,
                        cliente.email,
                        cliente.endereco,
                        cliente.id
                    )
                )

                conn.commit()

            return cliente

        except sqlite3.Error as e:
            messagebox.showerror(
                "Erro ao atualizar cliente",
                str(e)
            )
            raise

    # REMOVER
    def remover(self, id_cliente):
        try:
            with self.conectar() as conn:
                cur = conn.cursor()

                cur.execute(
                    "SELECT id, nome, telefone, email, endereco "
                    "FROM clientes WHERE id=?",
                    (id_cliente,)
                )

                row = cur.fetchone()

                if row:
                    cid, nome, telefone, email, endereco = row

                    cliente_removido = Cliente(
                        nome,
                        telefone,
                        email,
                        endereco,
                        id=cid
                    )
                else:
                    cliente_removido = None

                cur.execute(
                    "DELETE FROM clientes WHERE id=?",
                    (id_cliente,)
                )

                conn.commit()

            if cliente_removido:
                self.clientes_removidos.append(
                    cliente_removido
                )

            return cliente_removido

        except sqlite3.Error as e:
            messagebox.showerror(
                "Erro ao remover cliente",
                str(e)
            )
            raise

    # BUSCAR POR NOME
    def buscar_por_nome(self, texto):
        try:
            resultados = []
            like = f"%{texto}%"

            with self.conectar() as conn:
                cur = conn.cursor()

                cur.execute(
                    "SELECT id, nome, telefone, email, endereco "
                    "FROM clientes "
                    "WHERE nome LIKE ? COLLATE NOCASE "
                    "ORDER BY id",
                    (like,)
                )

                for row in cur.fetchall():
                    cid, nome, telefone, email, endereco = row

                    resultados.append(
                        Cliente(
                            nome,
                            telefone,
                            email,
                            endereco,
                            id=cid
                        )
                    )

            return resultados

        except sqlite3.Error as e:
            messagebox.showerror(
                "Erro na busca",
                str(e)
            )
            raise

# GERENCIADOR
gerenciador = GerenciadorClientes()
cliente_em_edicao_indice = None

# FUNÇÕES DA INTERFACE
def limpar_campos():
    global cliente_em_edicao_indice

    entrada_nome.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)

    cliente_em_edicao_indice = None

    atualizar_titulo_botao_salvar()

    entrada_nome.focus()


def atualizar_titulo_botao_salvar():
    if cliente_em_edicao_indice is not None:
        botao_salvar.config(
            text="Salvar Alterações"
        )
    else:
        botao_salvar.config(
            text="Salvar"
        )

# SALVAR / ATUALIZAR
def salvar():
    global cliente_em_edicao_indice

    nome = entrada_nome.get().strip()
    telefone = entrada_telefone.get().strip()
    email = entrada_email.get().strip()
    endereco = entrada_endereco.get().strip()

    # VALIDAÇÕES
    if nome == "":
        messagebox.showwarning(
            "Campo obrigatório",
            "Informe o nome do cliente."
        )
        entrada_nome.focus()
        return

    if telefone == "":
        messagebox.showwarning(
            "Campo obrigatório",
            "Informe o telefone do cliente."
        )
        entrada_telefone.focus()
        return

    if email == "":
        messagebox.showwarning(
            "Campo obrigatório",
            "Informe o e-mail do cliente."
        )
        entrada_email.focus()
        return

    if endereco == "":
        messagebox.showwarning(
            "Campo obrigatório",
            "Informe o endereço do cliente."
        )
        entrada_endereco.focus()
        return

    # MODO EDIÇÃO
    if cliente_em_edicao_indice is not None:

        clientes = gerenciador.listar()

        cliente_existente = clientes[
            cliente_em_edicao_indice
        ]

        cliente = Cliente(
            nome,
            telefone,
            email,
            endereco,
            id=cliente_existente.id
        )

        gerenciador.atualizar(cliente)

        messagebox.showinfo(
            "Sucesso",
            "Cliente atualizado com sucesso!"
        )

    # MODO CADASTRO
    else:
        cliente = Cliente(
            nome,
            telefone,
            email,
            endereco
        )

        gerenciador.adicionar(cliente)

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

    limpar_campos()

# CONSULTA DE CLIENTES
def abrir_consulta():
    global cliente_em_edicao_indice

    janela_consulta = tk.Toplevel(janela)

    janela_consulta.title(
        "Lista de Clientes"
    )

    janela_consulta.geometry(
        "800x500"
    )

    janela_consulta.configure(
        bg="#FFF0F5"
    )

    titulo = tk.Label(
        janela_consulta,
        text="Clientes Cadastrados",
        font=("Sans Serif", 16, "bold"),
        bg="#FAFAD2",
        fg="#A9A9A9"
    )

    titulo.pack(
        fill="x",
        pady=(0, 15)
    )

    frame_lista = tk.Frame(
        janela_consulta,
        bg="#FFF0F5"
    )

    frame_lista.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    # LISTA
    lista = tk.Listbox(
        frame_lista,
        width=100,
        height=15,
        font=("Sans Serif", 10),
        bg="#FFF0F5",
        fg="#A9A9A9",
        selectbackground="#D8BFD8",
        selectforeground="#FFFFFF"
    )

    lista.pack(
        side="left",
        fill="both",
        expand=True
    )

    # BARRA DE ROLAGEM
    scrollbar = tk.Scrollbar(
        frame_lista
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    lista.config(
        yscrollcommand=scrollbar.set
    )

    scrollbar.config(
        command=lista.yview
    )

    # CARREGA CLIENTES
    clientes_cadastrados = gerenciador.listar()

    if len(clientes_cadastrados) == 0:

        lista.insert(
            tk.END,
            "Nenhum cliente cadastrado."
        )

    else:

        for cliente in clientes_cadastrados:
            lista.insert(
                tk.END,
                str(cliente)
            )

    # EDITAR
    def editar_selecionado():

        global cliente_em_edicao_indice

        selecao = lista.curselection()

        if len(selecao) == 0:

            messagebox.showwarning(
                "Nenhuma seleção",
                "Selecione um cliente para editar."
            )

            return

        indice = selecao[0]

        clientes = gerenciador.listar()

        cliente_selecionado = clientes[indice]

        entrada_nome.delete(
            0,
            tk.END
        )

        entrada_nome.insert(
            0,
            cliente_selecionado.nome
        )

        entrada_telefone.delete(
            0,
            tk.END
        )

        entrada_telefone.insert(
            0,
            cliente_selecionado.telefone
        )

        entrada_email.delete(
            0,
            tk.END
        )

        entrada_email.insert(
            0,
            cliente_selecionado.email
        )

        entrada_endereco.delete(
            0,
            tk.END
        )

        entrada_endereco.insert(
            0,
            cliente_selecionado.endereco
        )

        cliente_em_edicao_indice = indice

        atualizar_titulo_botao_salvar()

        janela_consulta.destroy()


    # EXCLUIR
    def excluir_selecionado():

        selecao = lista.curselection()

        if len(selecao) == 0:

            messagebox.showwarning(
                "Nenhuma seleção",
                "Selecione um cliente para excluir."
            )

            return

        indice = selecao[0]

        clientes = gerenciador.listar()

        cliente_selecionado = clientes[indice]

        confirmacao = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Deseja realmente excluir "
            f"{cliente_selecionado.nome}?"
        )

        if confirmacao:

            gerenciador.remover(
                cliente_selecionado.id
            )

            messagebox.showinfo(
                "Sucesso",
                "Cliente removido com sucesso!"
            )

            lista.delete(
                0,
                tk.END
            )

            clientes_atualizados = gerenciador.listar()

            if len(clientes_atualizados) == 0:

                lista.insert(
                    tk.END,
                    "Nenhum cliente cadastrado."
                )

            else:

                for cliente in clientes_atualizados:

                    lista.insert(
                        tk.END,
                        str(cliente)
                    )

    # BOTÕES
    frame_botoes = tk.Frame(
        janela_consulta,
        bg="#FFF0F5"
    )

    frame_botoes.pack(
        pady=15
    )

    botao_editar = tk.Button(
        frame_botoes,
        text="Editar selecionado",
        width=20,
        command=editar_selecionado,
        bg="#FAFAD2",
        fg="#D8BFD8",
        font=("Sans Serif", 10, "bold"),
        relief="flat"
    )

    botao_editar.grid(
        row=0,
        column=0,
        padx=5
    )

    botao_excluir = tk.Button(
        frame_botoes,
        text="Excluir selecionado",
        width=20,
        command=excluir_selecionado,
        bg="#FAFAD2",
        fg="#DB7093",
        font=("Sans Serif", 10, "bold"),
        relief="flat"
    )

    botao_excluir.grid(
        row=0,
        column=1,
        padx=5
    )


# JANELA PRINCIPAl
janela = tk.Tk()

janela.title(
    "TechBairro — Cadastro de Cliente"
)

janela.geometry(
    "600x500"
)

janela.resizable(
    False,
    False
)

janela.configure(
    bg="#FFF0F5"
)

cabecalho = tk.Frame(
    janela,
    bg="#FAFAD2"
)

cabecalho.pack(
    side="top",
    fill="x"
)

titulo = tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    font=("Sans Serif", 18, "bold"),
    bg="#FAFAD2",
    fg="#A9A9A9",
    pady=12
)

titulo.pack()

# FORMULÁRIO
formulario = tk.Frame(
    janela,
    bg="#FFF0F5"
)

formulario.pack(
    padx=20,
    pady=20
)

# NOME
tk.Label(
    formulario,
    text="Nome:",
    width=12,
    anchor="e",
    font=("Sans Serif", 10),
    bg="#FFF0F5",
    fg="#A9A9A9"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=6
)

entrada_nome = tk.Entry(
    formulario,
    width=40,
    font=("Sans Serif", 10),
    bg="#FFFFFF",
    fg="#A9A9A9",
    insertbackground="#A9A9A9"
)

entrada_nome.grid(
    row=0,
    column=1,
    padx=5,
    pady=6
)

# TELEFONE
tk.Label(
    formulario,
    text="Telefone:",
    width=12,
    anchor="e",
    font=("Sans Serif", 10),
    bg="#FFF0F5",
    fg="#A9A9A9"
).grid(
    row=1,
    column=0,
    padx=5,
    pady=6
)

entrada_telefone = tk.Entry(
    formulario,
    width=40,
    font=("Sans Serif", 10),
    bg="#FFFFFF",
    fg="#A9A9A9",
    insertbackground="#A9A9A9"
)

entrada_telefone.grid(
    row=1,
    column=1,
    padx=5,
    pady=6
)

# E-MAIL
tk.Label(
    formulario,
    text="E-mail:",
    width=12,
    anchor="e",
    font=("Sans Serif", 10),
    bg="#FFF0F5",
    fg="#A9A9A9"
).grid(
    row=2,
    column=0,
    padx=5,
    pady=6
)

entrada_email = tk.Entry(
    formulario,
    width=40,
    font=("Sans Serif", 10),
    bg="#FFFFFF",
    fg="#A9A9A9",
    insertbackground="#A9A9A9"
)

entrada_email.grid(
    row=2,
    column=1,
    padx=5,
    pady=6
)

# ENDEREÇO
tk.Label(
    formulario,
    text="Endereço:",
    width=12,
    anchor="e",
    font=("Sans Serif", 10),
    bg="#FFF0F5",
    fg="#A9A9A9"
).grid(
    row=3,
    column=0,
    padx=5,
    pady=6
)

entrada_endereco = tk.Entry(
    formulario,
    width=40,
    font=("Sans Serif", 10),
    bg="#FFFFFF",
    fg="#A9A9A9",
    insertbackground="#A9A9A9"
)

entrada_endereco.grid(
    row=3,
    column=1,
    padx=5,
    pady=6
)

status = tk.Label(
    janela,
    text="Nenhum cliente cadastrado ainda",
    fg="#A9A9A9",
    bg="#FFF0F5",
    font=("Sans Serif", 9)
)

status.pack(
    pady=(0, 5)
)

# BOTÕES

botoes = tk.Frame(
    janela,
    bg="#FFF0F5"
)

botoes.pack(
    pady=10
)

# SALVAR
botao_salvar = tk.Button(
    botoes,
    text="Salvar",
    width=15,
    command=salvar,
    bg="#FAFAD2",
    fg="#D8BFD8",
    font=("Sans Serif", 10, "bold"),
    relief="flat"
)

botao_salvar.grid(
    row=0,
    column=0,
    padx=5
)

# CONSULTA
botao_consulta = tk.Button(
    botoes,
    text="Consultar",
    width=15,
    command=abrir_consulta,
    bg="#FAFAD2",
    fg="#D8BFD8",
    font=("Sans Serif", 10, "bold"),
    relief="flat"
)

botao_consulta.grid(
    row=0,
    column=1,
    padx=5
)

# LIMPAR
botao_limpar = tk.Button(
    botoes,
    text="Limpar",
    width=15,
    command=limpar_campos,
    bg="#FAFAD2",
    fg="#DB7093",
    font=("Sans Serif", 10, "bold"),
    relief="flat"
)

botao_limpar.grid(
    row=0,
    column=2,
    padx=5
)

tk.Label(
    janela,
    text="TechBairro • v1.0",
    fg="#A9A9A9",
    bg="#FFF0F5",
    font=("Sans Serif", 8)
).place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)

janela.mainloop()
