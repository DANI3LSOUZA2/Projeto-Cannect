from simplejson_functions import *

print("** MUDULO FEITO PARA ADICIONAR CANECAS NO SISTEMA")
while True:
    manipulador = show_file('canecas.txt')
    num_canecas = len(manipulador)
    print("A última caneca é a: {}".format(num_canecas))

    mug_num = input("Digite o número da caneca ou -1 para finalizar: ")
    if mug_num == "-1":
        break
    print("1 - Clean")
    print("2 - Dirty")
    print("3 - Broken")
    print("4 - Lost")

    while True:
        mug_state = int(input("Digite o status da caneca: "))

        if mug_state == 1:
            mug_state = "Clean"
            break

        if mug_state == 2:
            mug_state = "Dirty"
            break

        if mug_state == 3:
            mug_state = "Broken"
            break

        if mug_state == 4:
            mug_state = "Lost"
            break

        else:
            print("** Código inválido **")
            continue

    while True:
        disp = int(input("Digite 1 para disponível ou 0 para indisponível: "))

        if disp == 1:
            disp = 'disponivel'
            break

        if disp == 0:
            disp = 'indisponivel'
            break

        else:
            print(" ** Código Inválido ** ")
            continue



    caneca = {
        'mug_num': mug_num,
        'mug_state': mug_state,
        'disp': disp
    }

    caneca = insert_file(caneca, 'canecas.txt')
    print("\n** Caneca Cadastrada ** \n")



