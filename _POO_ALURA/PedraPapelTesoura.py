import random

def jogar():
    user = input("'pe', 'pa' ou 't'").lower()
    pc = random.choice(['pe', 'pa','t'])
    if user == pc:
        return "empatou"
    if ganho(user,pc):
        return "GANHOU DAS MAQUINAS HHAHAHAHAHAHA"
    return  "Comecou a revolucao das maquinas"
    # pedra > tes, tes> papel, papel > pedra
def ganho(j1,j2):
    if (j1 =='pe' and j2 =='t') or (j1 =='t' and j2=='pa') or (j1 == 'pa' and j2 == 'pe'):
        return True

print(jogar())
