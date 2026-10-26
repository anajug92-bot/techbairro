# Manual de uso da TechBairro

## A tela principal

A tela principal permite cadastrar, consultar, alterar e excluir clientes. Ela possui campos para preencher os dados, botões para realizar as operações e uma área para visualizar os clientes cadastrados.

## Cadastrar um cliente

1. Abra o programa `techbairro.py`.
2. Preencha os campos com os dados do cliente.
3. Confira se as informações estão corretas.
4. Clique no botão de cadastro ou salvamento.
5. Verifique a mensagem apresentada para confirmar se o cadastro foi realizado.

## Consultar os clientes cadastrados

1. Abra a área de consulta.
2. Procure o cliente desejado na lista de cadastrados.
3. Selecione o cliente para visualizar suas informações.

## Alterar os dados de um cliente

1. Consulte os clientes cadastrados.
2. Selecione o cliente que deseja alterar.
3. Clique no botão de alteração ou edição.
4. Modifique os campos necessários.
5. Salve as alterações e confira a mensagem apresentada.

## Excluir um cliente

1. Consulte os clientes cadastrados.
2. Selecione o cliente que deseja excluir.
3. Clique no botão de exclusão.
4. Confira os dados do cliente selecionado.
5. Confirme a exclusão somente se tiver certeza de que selecionou o cliente correto.

## Regras de preenchimento

| Campo | Obrigatório? | Regra |
|---|---|---|
| Nome | Conforme o sistema | Informe o nome do cliente. |
| Telefone | Conforme o sistema | Digite um telefone válido. |
| E-mail | Conforme o sistema | Informe um e-mail válido. |
| Endereço | Conforme o sistema | Informe o endereço do cliente. |

## Mensagens do sistema

| Mensagem | O que significa | O que fazer |
|---|---|---|
| Cadastro realizado com sucesso | O cliente foi cadastrado. | Confira se ele aparece na consulta. |
| Preencha os campos obrigatórios | Existem campos que precisam ser preenchidos. | Complete os campos solicitados. |
| Cliente não encontrado | O sistema não localizou o cliente. | Confira as informações e tente novamente. |
| Selecione um cliente | Nenhum cliente foi selecionado. | Selecione um registro antes de continuar. |
| Confirma a exclusão? | O sistema solicita autorização para excluir. | Confira os dados antes de confirmar. |
| Erro ao salvar os dados | O sistema não conseguiu salvar as informações. | Confira os dados e tente novamente. |

**Importante:** confira os textos dessa tabela com as mensagens reais do seu programa antes de entregar.

## Dúvidas frequentes

**Como sei se o cadastro deu certo?**

Confira a mensagem apresentada pelo sistema e procure o cliente na consulta.

**O que faço se preencher algum dado errado?**

Consulte o cliente, selecione-o e utilize a opção de alteração, caso esteja disponível.

**Posso excluir um cliente por engano?**

Para evitar isso, confira os dados do cliente antes de confirmar a exclusão.

**O que faço se o programa não abrir?**

Confira se o Python está instalado e se você seguiu as instruções do README.