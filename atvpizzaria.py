print("PIZZARIA JJ")
print("Bem-vindo à Pizzaria JJ!")
print("")
print("CARDÁPIO - PREÇOS")
print("")

print ("///////PIZZAS - SABORES///////")
print(" CALABRESA, FRANGO, MUSSARELA")

print("////////PIZZAS - TAMANHO///////")
print(" PIZZA PEQUENA   R$ 20,00")
print(" PIZZA MÉDIA    R$ 30,00")
print(" PIZZA GRANDE   R$ 40,00")
print("")

print("/////////BEBIDAS - SABORES/////////")
print(" COCA-COLA LATA   R$ 8,00")
print(" SUCO LATA       R$ 5,00")
print(" AGUA MINERAL    R$ 3,00")
print("")

print("FAÇA SEU PEDIDO PARA A PIZZA")
print(" 1 - CALABREZA")
print(" 2 - FRANGO")
print(" 3 - MUSSARELA")
print("")

# Lê a escolha do sabor do usuário e converte para inteiro.
pedidopizza = int(input())


print("DIGITE O TAMANHO DA PIZZA:")
print(" P - PEQUENA")
print(" M - MÉDIA ")
print(" G - GRANDE ")

# Lê a escolha do tamanho da pizza do usupario e converte para maiúsculo.
tampizza = input().upper()



print("FAÇA SEU PEDIDO PARA REFRIGERANTE: ")
print(" 1 - COCA-COLA LATA")
print(" 2 - SUCO LATA ")
print(" 3 - AGUA MINERAL")
print("")

# Lê A ESCOLHA DO REFRIGERANTE DO USUÁRIO E CONVERTE PARA INTEIRO
pedidorefri = int(input())



# Calcula o prelo total e descreve o pedido utilizando elif com parênteses; PEQUENA

if (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 20.00 + 8.00
    pedidos = "CALABREZA, PEQUENA, COCA-COLA LATA"

elif (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 20.00 + 5.00
    pedidos = "CALABREZA, PEQUENA, SUCO LATA" 

elif (pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 20.00 + 3.00 
    pedidos = "CALABREZA, PEQUENA, AGUA MINERAL"

# // 


elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 20.00 + 5.00
    pedidos = "FRANGO, PEQUENA, SUCO LATA" 

elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 20.00 + 3.00 
    pedidos = "FRANGO, PEQUENA, AGUA MINERAL"

elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 20.00 + 5.00
    pedidos = "FRANGO, PEQUENA, SUCO LATA" 


# // 

elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 20.00 + 5.00
    pedidos = "MUSSARELA, PEQUENA, SUCO LATA" 

elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 20.00 + 3.00 
    pedidos = "MUSSARELA, PEQUENA, AGUA MINERAL"

elif (pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 20.00 + 5.00
    pedidos = "MUSSARELA, PEQUENA, SUCO LATA" 


# // MÉDIA

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 30.00 + 8.00
    pedidos = "CALABREZA, PEQUENA, COCA-COLA LATA"

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 30.00 + 5.00
    pedidos = "CALABREZA, PEQUENA, SUCO LATA" 

elif (pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 30.00 + 3.00 
    pedidos = "CALABREZA, PEQUENA, AGUA MINERAL"

#//

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 30.00 + 8.00
    pedidos = "FRANGO, PEQUENA, COCA-COLA LATA"

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 30.00 + 5.00
    pedidos = "FRANGO, PEQUENA, SUCO LATA" 

elif (pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 30.00 + 3.00 
    pedidos = "FRANGO, PEQUENA, AGUA MINERAL"


# // 

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 30.00 + 8.00
    pedidos = "MUSSARELA, PEQUENA, COCA-COLA LATA"

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 30.00 + 5.00
    pedidos = "MUSSARELA, PEQUENA, SUCO LATA" 

elif (pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 30.00 + 3.00 
    pedidos = "MUSSARELA, PEQUENA, AGUA MINERAL"

# // GRANDE

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 40.00 + 8.00
    pedidos = "CALABREZA, PEQUENA, COCA-COLA LATA"

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 40.00 + 5.00
    pedidos = "CALABREZA, PEQUENA, SUCO LATA" 

elif (pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 40.00 + 3.00 
    pedidos = "CALABREZA, PEQUENA, AGUA MINERAL"

# // 

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 40.00 + 8.00
    pedidos = "FRANGO, PEQUENA, COCA-COLA LATA"

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 40.00 + 5.00
    pedidos = "FRANGO, PEQUENA, SUCO LATA" 

elif (pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 40.00 + 3.00 
    pedidos = "FRANGO, PEQUENA, AGUA MINERAL"

#//

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 40.00 + 8.00
    pedidos = "MUSSARELA, PEQUENA, COCA-COLA LATA"

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 40.00 + 5.00
    pedidos = "MUSSARELA, PEQUENA, SUCO LATA" 

elif (pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 40.00 + 3.00 
    pedidos = "MUSSARELA, PEQUENA, AGUA MINERAL"

else:
    precopagar = 0.0
    pedidos = "INVÁLIDO"

print("////////////////////////////////")
print(f"O TOTAL A PAGAR É: R$ {precopagar:.2f}")
print("////////////////////////////////")
print(f"OS PEDIDOS FORAM {pedidos}")
print("////////////////////////////////")
print("BOM APETITE, AGRADECEMOS A PREFERENCIA.")
