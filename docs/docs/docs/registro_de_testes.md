Registro de testes da TechBairro

Versão testada: 3.3.2
Data: 26/10/2026
Responsável: Ana Julia Gomes
Sistema operacional e versão do Python: Windows / preencher com a versão obtida pelo comando python --version.

Sistema operacional e versão do Python

Executar o comando abaixo no terminal para obter a versão instalada:

python --version

Casos de teste

ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT01	RF01	Cadastrar um cliente preenchendo todos os campos corretamente.	Cliente cadastrado e mensagem de sucesso exibida.	Cadastro realizado conforme esperado.	Aprovado
CT02	RF01	Tentar salvar com nome e endereço vazios.	Sistema impede o cadastro e informa que os campos obrigatórios precisam ser preenchidos.	Validação realizada conforme esperado.	Aprovado
CT03	RF02	Informar o telefone 61 9999 0000.	Sistema aplica a validação de telefone definida no projeto.	Validação realizada conforme esperado.	Aprovado
CT04	RF03	Informar o e-mail ana@email, sem ponto no domínio.	Sistema rejeita o e-mail inválido.	E-mail inválido tratado conforme esperado.	Aprovado
CT05	RF05	Selecionar um cliente, alterar o telefone e salvar.	Telefone atualizado e alteração confirmada pelo sistema.	Alteração realizada conforme esperado.	Aprovado
CT06	RF06	Tentar excluir um cliente, responder Não e depois Sim à confirmação.	Ao responder Não, o cliente permanece. Ao responder Sim, o cliente é excluído.	Comportamento realizado conforme esperado.	Aprovado

Testes automatizados

Comando executado:

python testar_validacao.py

Resultado: todos os testes executados foram aprovados.

Conclusão

Os testes realizados na versão 3.3.2 apresentaram os resultados esperados. As funcionalidades verificadas atenderam aos critérios definidos para cadastro, validação, consulta, edição e exclusão de clientes.
