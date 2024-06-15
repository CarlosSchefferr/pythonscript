# Sistema de Registro de Clientes

Este projeto é um sistema simples de registro de clientes desenvolvido em Python. Ele permite que os usuários insiram informações sobre clientes, como nome, CPF, acomodação e setor, e calcula o total a ser pago por cada cliente com base nas informações fornecidas.

## Funcionalidades

- Registro de clientes com nome, CPF, acomodação e setor.
- Cálculo do total a ser pago com base na acomodação e no setor escolhidos.
- Exibição do total a ser pago para cada cliente.

## Como Usar

1. Execute o script Python.
2. Insira o nome do cliente (ou 'Sair' para encerrar o programa).
3. Insira o CPF do cliente.
4. Escolha o tipo de acomodação:
   - `1` para quarto duplo.
   - `2` para quarto triplo.
5. Escolha o setor:
   - `A` ou `B`.
6. O sistema exibirá o total a ser pago pelo cliente.
7. O loop continuará até que você insira 'Sair' como nome do cliente.

## Exemplo de Uso

```bash
Qual o seu nome ('Sair' - encerra): João
Digite seu CPF: 123.456.789-00
Acomodação: 1- (quarto duplo) ou 2-(quarto triplo): 1
Qual setor você irá ficar, A ou B: A
João, total US$3,090.00
Qual o seu nome ('Sair' - encerra): Maria
Digite seu CPF: 987.654.321-00
Acomodação: 1- (quarto duplo) ou 2-(quarto triplo): 2
Qual setor você irá ficar, A ou B: B
Maria, total US$2,940.00
Qual o seu nome ('Sair' - encerra): Sair

