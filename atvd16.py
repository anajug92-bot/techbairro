import tkinter as tk
from tkinter import messagebox

# Classe que representa a estrutura de dados de um Cliente
class Cliente:
    def __init__(self, nome, telefone, email, endereco):
        # Inicializa os atributos básicos do cliente
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def resumo(self):
        # Retorna uma string formatada com todas as informações principais do cliente
        return f"Nome: {self.nome} | Tel: {self.telefone} | E-mail: {self.email} | Endereço: {self.endereco}"


# Classe responsável por gerenciar a lista de clientes cadastrados (operações de dados)
class GerenciadorClientes:
    def __init__(self):
        # Inicializa a lista vazia onde os objetos Cliente serão armazenados
        self.clientes = []

    def adicionar(self, cliente):
        # Adiciona um novo objeto cliente à lista interna
        self.clientes.append(cliente)

    def listar(self):
        # Retorna a lista completa de clientes cadastrados
        return self.clientes

    def atualizar(self, indice, novo_cliente):
        # Método reservado para futuras implementações de atualização de dados
        print("atualizar cliente: sem funcionalidades no momento")
        return

    def remover(self, indice):
        # Método reservado para futuras implementações de remoção de clientes
        print("remover cliente: sem funcionalidades no momento")
        return


# Classe principal que controla a interface gráfica (GUI) usando Tkinter
class TechBairroApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("TechBairro - Cadastro de Clientes")
        self.janela.geometry("400x320")
        
        # Instancia o gerenciador para controlar os dados dos clientes
        self.gerenciador = GerenciadorClientes()
        
        # Dicionário para armazenar as referências das caixas de texto (Entry)
        self.entradas = {}

        # Cria dinamicamente os campos de entrada para o cadastro
        campos = ["Nome", "Telefone", "E-mail", "Endereço"]
        for campo in campos:
            frame = tk.Frame(self.janela, pady=5)
            frame.pack(fill=tk.X, padx=10)
            
            lbl = tk.Label(frame, text=campo + ":", width=10, anchor="w")
            lbl.pack(side=tk.LEFT)
            
            ent = tk.Entry(frame)
            ent.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            self.entradas[campo] = ent


        # Botão para salvar as informações digitadas nos campos
        tk.Button(janela, text="salvar", command=self.salvar, bg="#FAFAD2", fg="#D8BFD8").pack(pady=5, fill=tk.X, padx=5)
        
        # Botão para abrir a janela secundária que exibe a lista de clientes cadastrados
        tk.Button(janela, text="Lista de Clientes", command=self.abrir_consulta, bg="#FAFAD2", fg="#D8BFD8").pack(pady=5, fill=tk.X, padx=5)

    def salvar(self):
        # Captura os valores inseridos nos campos de texto da interface
        nome = self.entradas["Nome"].get()
        telefone = self.entradas["Telefone"].get()
        email = self.entradas["E-mail"].get()
        endereco = self.entradas["Endereço"].get()

        # Valida se os campos obrigatórios (Nome e Telefone) foram preenchidos
        if not nome.strip() or not telefone.strip():
            print("Erro de Validação: Os campos 'Nome' e 'Telefone' são obrigatórios!")
            return

        # Cria a instância do cliente e a adiciona através do gerenciador
        novo_cliente = Cliente(nome, telefone, email, endereco)
        self.gerenciador.adicionar(novo_cliente)

        print("Cliente cadastrado com sucesso!")
        # Limpa os campos após salvar com sucesso
        self.limpar_campos()

    def abrir_consulta(self):
        # Cria uma nova janela secundária para exibir os registros
        janela_consulta = tk.Toplevel(self.janela)
        janela_consulta.title("TechBairro - Lista de Clientes")
        janela_consulta.geometry("450x350")
        tk.Label(janela_consulta, text="Clientes Cadastrados", font=("Arial", 12, "bold")).pack(pady=10)

        # Caixa de texto para exibir os dados dos clientes na segunda janela
        txt_resultado = tk.Text(janela_consulta, height=12, width=50)
        txt_resultado.pack(pady=5, padx=15, fill=tk.BOTH, expand=True)

        # Busca os dados atuais usando o método do gerenciador
        lista_clientes = self.gerenciador.listar()
        
        # Insere os dados na caixa de texto ou exibe aviso caso esteja vazia
        if not lista_clientes:
            txt_resultado.insert(tk.END, "Nenhum cliente cadastrado até o momento.")
        else:
            for i, cliente in enumerate(lista_clientes):
                txt_resultado.insert(tk.END, f"{i+1}. {cliente.resumo()}\n" + "-"*45 + "\n")
        
        txt_resultado.config(state=tk.DISABLED)

        # Botão para fechar a janela de consulta
        tk.Button(janela_consulta, text="Fechar", command=janela_consulta.destroy, bg="#FAFAD2", fg="#D8BFD8").pack(pady=10)

    def limpar_campos(self):
        # Limpa o conteúdo digitado
        for campo in self.entradas:
            self.entradas[campo].delete(0, tk.END)

# execução do programa
if __name__ == "__main__":
    # Inicializa a janela principal do aplicativo Tkinter
    janela = tk.Tk()
    # Instancia a classe principal da aplicação passando a janela
    app = TechBairroApp(janela)
    # Inicia o loop de eventos da interface gráfica
    janela.mainloop()