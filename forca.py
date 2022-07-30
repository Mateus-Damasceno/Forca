import os.path
import random

cont = 6
filename = "data.csv"
if os.path.isfile(filename):
    with open(filename, "r") as file:
        content = file.readlines()
        content = [x.rstrip('\n') for x in content]
        # print(content)


else:
    print(f'file{filename} nao existe')

# existe um jeito melhor
random = random.randint(0, (len(content) - 1))
palavra = content[random]

lenforca = (len(palavra))

digitadas = []
for i in range(lenforca):
    print('_', end="")

print('')

while True:
    chute = input()
    passe = chute

    if len(chute) > 1:
        print("só uma letra")
        continue
    if chute in digitadas:
        print("letra repetida")
        continue
    digitadas.append(chute)
    temp = ''
    for chute in palavra:
        if chute in digitadas:
            temp += chute

        else:

            temp += '_'

    print(f'as letras digitadas foram: {digitadas}')

    if temp == palavra:
        print("você venceu!!")
        break
    else:
        print(f'a palavra esta assim: {temp}')

        if passe not in palavra:
            print(cont)
            cont -= 1
        else:
            pass
        if cont <= 0:
            print("FORCA!! ")
            break
        print()
        print(f'chances: {cont}')
