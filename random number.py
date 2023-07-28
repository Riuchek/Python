import random

def chuta(x):
    RN = random.randint(1,x)
    chuta = 0
    while chuta !=RN :
        chuta =int (input(f"Chute um numero entre 1 e {x}: "))
        print(chuta)
        if chuta < RN :
            print("muito baixo teu chute nego")
        elif chuta > RN:
            print("Muito alto nego abaixa ae ")

    print(f"acerto mizeravi o numero: {x}")


def pc_guess(x):
    baixo = 1
    alto = x
    feedback = ''
    while feedback != 'c':
        if baixo != alto:
            chuta = random.randint(baixo,alto)
        else :
            chuta = baixo
        feedback = input(f'O numero {chuta} ta alto (A), baixo (B) ou certo (C)'.lower())
        if feedback == 'a':
            alto = chuta -1
        elif feedback == 'b':
            baixo = chuta +1
    print(f'Aeee a maquina acertou o numero {chuta}')
chuta(10)
pc_guess(1000)
