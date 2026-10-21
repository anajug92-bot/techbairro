# CHANGELOG.md

## Em desenvolvimento
### Adicionado
- Código publicado no GitHub, com histórico de versões.

## v3.2.1 (Aula 18)
### Alterado
- O número da versão passou a ficar definido em um único lugar no arquivo techbairro.py.

### Adicionado
- Script scripts/gerar_pacote.py para gerar o pacote da versão.
- Arquivo COMO_EXECUTAR.txt com as instruções para executar o sistema.

# Changelog da TechBairro

## v3.2 (Aula 16)

### Alterado

* O banco agora é aberto pelo caminho completo (`os.path` + `__file__`), sempre na pasta do projeto, não importa de onde o programa seja executado.
* O sistema passou a exibir a mensagem "Banco em uso" no terminal, mostrando qual arquivo de banco está sendo utilizado.

### Adicionado

* Foi criado o script `verificar_banco.py` para consultar e auditar diretamente o banco de dados.
* Foram adicionadas verificações A1 até A5 para conferir quantidade de clientes, campos vazios, telefones inválidos, e-mails fora do formato e telefones repetidos.

## v3.1 (Aula 15)

### Corrigido

* Corrigida a validação para que o campo Endereço também seja obrigatório.
* Corrigida a validação de e-mail para impedir e-mails sem usuário antes do `@`.
* Corrigida a validação de e-mail para impedir e-mails sem domínio.
* Corrigida a ordenação dos clientes para que sejam apresentados em ordem alfabética pelo nome.
* Corrigida a confirmação da exclusão para que o cadastro só seja removido quando o usuário confirmar.
* Corrigida a atualização dos clientes adicionando o `commit`, garantindo que as alterações sejam salvas no banco.

## v3.0 (Aula 14)

### Alterado

* O GerenciadorClientes deixou de guardar os clientes somente em uma lista em memória e passou a gravar os dados no banco SQLite `techbairro.db`.
* As operações de edição e exclusão passaram a utilizar o ID do cliente em vez do índice da lista.
* A quantidade de clientes passou a ser obtida diretamente do banco de dados.

### Adicionado

* Foi adicionada a integração com SQLite para armazenamento permanente dos clientes.

## v2.0 (Aulas 11 e 12)

### Adicionado

* Foram criadas as classes `Cliente` e `GerenciadorClientes`.
* Foi adicionada a tela de Consulta para visualizar os clientes cadastrados.
* Foram adicionadas as funções de cadastro e listagem dos clientes.
* Foram adicionados os métodos `atualizar()` e `remover()` ao gerenciador, inicialmente preparados para futuras implementações.

## Antes da v2.0 (Aulas 5 a 10)

* Foram desenvolvidas as telas da aplicação utilizando Tkinter, juntamente com os campos de cadastro e os eventos dos botões.
* Foram adicionadas validações básicas para os dados preenchidos pelo usuário.

# Changelog da TechBairro

## v3.3.0 (Aula 20)

### Adicionado
- Indicação visual do modo de edição: o botão muda para “Salvar edição” e volta para “Salvar” ao sair da edição.
- Duplo clique em uma linha da Consulta para editar o cliente.
- Atalho Delete na Consulta para excluir com confirmação.
- Telefone e e-mail na confirmação de exclusão para ajudar na conferência.

### Corrigido
- Editar e excluir usam o cliente associado à linha que está visível na Consulta, evitando divergências quando outra janela altera o banco.
- Linhas informativas, como “Nenhum cliente cadastrado”, não podem ser tratadas como clientes.
- O sistema verifica o retorno de atualizar() e informa quando o cliente não existe mais.
- O sistema verifica o retorno de remover() e atualiza a Consulta quando o cliente já foi excluído em outra janela.
- Cancelar informa se uma edição foi cancelada ou se apenas limpou o formulário.

# 5.2
VERSAO = "3.3.1"

## v3.3.1 (Aula 21)

- Separação da classe Cliente no arquivo cliente.py.
- Separação da classe GerenciadorClientes no arquivo banco.py.
- Criação do ValidadorCliente no arquivo validacao.py.
- Criação de testes automatizados das regras de validação.
- Organização do código em módulos com responsabilidades separadas.
- Preservação do comportamento da versão anterior.

# Por que a versão é PATCH, mesmo com quatro arquivos novos?
A versão é PATCH porque as mudanças reorganizam a estrutura interna do código e adicionam testes, sem alterar as funcionalidades nem o comportamento esperado para o usuário.

# 5.3 — Geração do pacote
Todos os arquivos novos entraram no pacote sem o __pycache__