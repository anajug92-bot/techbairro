# Registro de testes da TechBairro

**Versão testada:** 3.3.2  
**Data:** 26/10/2026  
**Responsável:** Ana Julia Gomes  
**Sistema operacional e versão do Python:** Windows / preencher com a versão obtida pelo comando `python --version`.

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar um cliente preenchendo todos os campos corretamente. | Cliente cadastrado e mensagem de sucesso exibida. | Preencher após executar o teste. | Pendente |
| CT02 | RF01 | Tentar salvar com Nome e Endereço vazios. | Sistema impede o cadastro e informa que os campos obrigatórios precisam ser preenchidos. | Preencher após executar o teste. | Pendente |
| CT03 | RF02 | Informar o telefone `61 9999 0000`. | Sistema aplica a validação de telefone definida no projeto. | Preencher após executar o teste. | Pendente |
| CT04 | RF03 | Informar o e-mail `ana@email`, sem ponto no domínio. | Sistema rejeita o e-mail inválido. | Preencher após executar o teste. | Pendente |
| CT05 | RF05 | Selecionar um cliente, alterar o telefone e salvar. | Telefone atualizado e alteração confirmada pelo sistema. | Preencher após executar o teste. | Pendente |
| CT06 | RF06 | Tentar excluir um cliente, responder Não e depois Sim. | Ao responder Não, o cliente permanece. Ao responder Sim, o cliente é excluído. | Preencher após executar o teste. | Pendente |

## Testes automáticos

**Comando executado:**

```bash
python testar_validacao.py
```

**Resultado obtido:** preencher com a saída real do terminal.

**Status:** pendente de execução.

## Defeitos encontrados

Preencher após executar os testes. Registrar os defeitos identificados, como foram corrigidos e o commit correspondente.

Caso nenhum defeito seja encontrado, escrever: "Nenhum defeito encontrado nos testes executados".