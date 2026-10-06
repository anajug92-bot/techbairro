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
