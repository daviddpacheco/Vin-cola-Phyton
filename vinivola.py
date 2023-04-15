#David de Medeiros Pacheco Junior rm:551462

print("Boas-vindas a Vinheria Agnello")
print("Para prosseguirmos com o atendimento, infome os dados")

nome = input("Digite seu nome-")
idade = int(input("Digite sua idade-"))
if idade < 18:
    print("Desculpe, você não tem idade suficiente para se cadastrar.")
    raise SystemExit  # Encerra o programa caso o usuário seja menor de idade

endereço = input("Digite seu endereço-")
envio = input("Digite seu endereço de envio-")

# Criando o catálogo de vinhos com seus respectivos preços
catalogo_vinhos = {'Cabernet Sauvignon': 50.0, 'Merlot': 45.0, 'Pinot Noir': 60.0, 'Chardonnay': 35.0, 'Sauvignon Blanc': 40.0}

# Solicitando a quantidade de cada tipo de vinho a ser comprado
qtd_cabernet = int(input("Quantidade de Cabernet Sauvignon: "))
qtd_merlot = int(input("Quantidade de Merlot: "))
qtd_pinot_noir = int(input("Quantidade de Pinot Noir: "))
qtd_chardonnay = int(input("Quantidade de Chardonnay: "))
qtd_sauvignon_blanc = int(input("Quantidade de Sauvignon Blanc: "))

# Calculando o valor do pedido
valor_pedido = (qtd_cabernet * catalogo_vinhos['Cabernet Sauvignon']) + (qtd_merlot * catalogo_vinhos['Merlot']) + (qtd_pinot_noir * catalogo_vinhos['Pinot Noir']) + (qtd_chardonnay * catalogo_vinhos['Chardonnay']) + (qtd_sauvignon_blanc * catalogo_vinhos['Sauvignon Blanc'])

# Verificando o valor do pedido e aplicando a lógica de frete
if valor_pedido >= 200.0:
    frete = 0.0
    mensagem_frete = "Frete grátis!"
else:
    frete = 50.0
    mensagem_frete = f"Frete: R$ {frete:.2f}"

# Verificando se o valor do pedido é maior ou igual a R$100,00
if valor_pedido >= 100.0:
    # Pedindo confirmação de compra
    confirmacao = input(f"O valor total do pedido é R$ {valor_pedido:.2f}. {mensagem_frete} Deseja confirmar a compra? (sim/não) ")
    
    # Verificando a resposta de confirmação
    if confirmacao.lower() in ['sim', 's']:
        # Emitindo nota fiscal
        print("\n====== NOTA FISCAL ======")
        print("Produtos comprados:")
        if qtd_cabernet > 0:
            print(f"{qtd_cabernet} x Cabernet Sauvignon - R$ {qtd_cabernet * catalogo_vinhos['Cabernet Sauvignon']:.2f}")
        if qtd_merlot > 0:
            print(f"{qtd_merlot} x Merlot - R$ {qtd_merlot * catalogo_vinhos['Merlot']:.2f}")
        if qtd_pinot_noir > 0:
            print(f"{qtd_pinot_noir} x Pinot Noir - R$ {qtd_pinot_noir * catalogo_vinhos['Pinot Noir']:.2f}")
        if qtd_chardonnay > 0:
            print(f"{qtd_chardonnay} x Chardonnay - R$ {qtd_chardonnay * catalogo_vinhos['Chardonnay']:.2f}")
        if qtd_sauvignon_blanc > 0:
            print(f"{qtd_sauvignon_blanc} x Sauvignon Blanc - R$ {qtd_sauvignon_blanc * catalogo_vinhos['Sauvignon Blanc']:.2f}")


