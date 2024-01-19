print("Obrigado por escolher Telas pizzaria, a melhor facada que voce vai levar\n")

Sabor = input("Qual o sabor que voce gostaria? Mussarela, Calabresa, Frango, Chocolate ou gostaria de pedir uma meio a meio?\n")
Tamanho = input("Qual o tamanho da pizza que voce gostaria? Broto, Medio ou Familia\n")

Conta = 0

if Sabor == "Meio a meio":
    Meio = input("E qual seriam esses sabores? Nós temos: Mussarela e Calabresa, Mussarela e Frango, Calabresa e Frango, Salgado com Doce\n")
    if Meio == "Mussarela e Calabresa":
        Conta += 10.99
    if Meio == "Mussarela e Frango":
        Conta += 10.49
    if Meio == "Calabresa + Frango":
        Conta += 11.49
    if Meio == "Salgado com doce":
        Meia = input("Qual sabor de salgado você gostaria? Mussarela, Frango ou Calabresa?\n")
        if Meia == "Mussarela":
            Conta += 15.99
        if Meia == "Frango":
            Conta += 15.99
        if Meia == "Calabresa":
            Conta += 15.99
if Sabor == "Mussarela":
    Conta += 9.99
if Sabor == "Calabresa":
    Conta += 11.99
if Sabor == "Frango":
    Conta += 10.99
if Sabor == "Chocolate":
    Conta += 12.99

if Tamanho == "Broto":
    Conta += 29.99
elif Tamanho == "Medio":
    Conta += 35.99
else:
    Conta += 49.99

Salami = input("Gostaria de adicionar salami? Sim ou Nao\n")
Queijo = input("Gostaria de queijo extra? Sim ou Nao\n") 
Borda = input("Gostaria de borda recheada? Sim ou Nao\n")

if Salami == "Sim":
    Conta += 8.99

if Queijo == "Sim":
    Conta += 4.99

if Borda == "Sim":
    Bordela = input("Qual borda voce gostaria? Chocolate, Requeijao, Catupiry, Cheddar, Doce de leite\n")
    if Bordela == "Chocolate":
        Conta += 3.99
    if Bordela == "Requeijao":
        Conta += 2.99
    if Bordela == "Catupiry":
        Conta += 3.49
    if Bordela == "Cheddar":
        Conta += 6.99
    if Bordela == "Doce de leite":
        Conta += 5.49

Frete = input("Vai ser para retirar no local ou para Entrega?\n")

if Frete == "Entrega":
    Conta += 4.99
    Endereço = input("Qual é o endereço da entrega?\n")
    Pagamento = input(f"O total da sua conta foi {round(Conta ,2)} reais. Como gostaria de pagar? Cartao ou Dinheiro\n")
    if Pagamento == "Cartao":
        print("Ok, a pizza ficara pronta em 45 minutos! Obrigado por pedir conosco!")
    if Pagamento == "Dinheiro":
        Troco = float(input("Sera necessario troco? Se sim, para quanto seria?\n"))
        if Troco < Conta:
            print("\nRefaça o pedido, valor do troco invalido")
        else:
            Troco -= Conta
            print(f"Ok, o motoboy saira em 45 minutos e levara o troco de {round(Troco ,2)} reais!")
else:
    print(f"Ok, o total da conta foi {round(Conta ,2)}, a pizza ficara pronta em 45 minutos!")

print(input("\nAperte ENTER para fechar o terminal"))