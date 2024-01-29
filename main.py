print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Seja bem-vindo(a) a ilha de tesouro.")
print("A sua missão é econtrar o tesouro.")
print("Você encontra uma estrada, e existe dois caminhos, você gostaria de ir para a esquerda ou direita ?\nDigite 'E' para Esquerda e 'D' para Direita")

caminho_1 = input("").lower()

if caminho_1 == "D":
    print("Você caiu em um buraco.\nGame Over")
else:
    print("Após caminhar, Você encontra um lago e nele tem uma ilha no meio, você quer nadar ou esperar um barco chegar até você ?\nDigite 'N' para nadar e 'E' para esperar")

caminho_2 = input("").lower()

if caminho_2 ==  "N":
    print("Você foi atacado por um jacaré\nGamer Over")
else:
    print("Após atravessar e chegar na ilha no lago, você encontra uma casa com 3 portas. Uma vermelha, uma amarela e uma azul.\nQual cor você escolhe")

caminho_3 = input("").lower()

if caminho_3 == "vermelha":
    print("Você caiu em uma armadilha\nGame Over")
elif caminho_3 == "azul":
    print("Você foi comido por bestas\nGame Over")
elif caminho_3 == "amarelo":
    print("Parabéns você ganhou !")
else:
    print("Game Over")
