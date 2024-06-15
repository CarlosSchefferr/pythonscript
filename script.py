clientes = {}
cod = 1

while True:
    nome = input("Qual o seu nome ('Sair' - encerra): ")
    if nome.title() == "Sair":
        break
    
    cpf = input("Digite seu CPF: ")
    acomodacao = input("Acomodação: 1- (quarto duplo) ou 2-(quarto triplo): ")
    setor = input("Qual setor você irá ficar, A ou B: ")

    dados = [nome.title(), cpf, acomodacao, setor]
    clientes[cod] = dados

    if acomodacao == '1':
        subtotal = 240 * 2
    elif acomodacao == '2':
        subtotal = 180 * 2
    else:
        print("Acomodação inválida, considerando como quarto duplo.")
        subtotal = 240 * 2

    if setor.upper() == "A":
        setor_valor = 800
    elif setor.upper() == "B":
        setor_valor = 650
    else:
        print("Setor inválido, considerando como setor B.")
        setor_valor = 650
        
    total_cliente = 1450 + subtotal + setor_valor
    print(f'{nome.title()}, total US${total_cliente:,.2f}')
    
    cod += 1
