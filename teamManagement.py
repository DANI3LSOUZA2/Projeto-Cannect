from simplejson_functions import *


def atualizar_placar():
    soma_time1 = 0
    soma_time2 = 0
    soma_usuario_time1 = 0
    soma_usuario_time2 = 0

    time = show_file('times.txt')
    usuario = show_file('usuarios.txt')

    time1 = find_file('id_time', '1', 'times.txt')
    time2 = find_file('id_time', '2', 'times.txt')

    time1_atual = find_file('id_time', "1", 'times.txt')
    time2_atual = find_file('id_time', '2', 'times.txt')


    # Soma time
    for pontuacao in time:

        if pontuacao['id_time'] == '1':
            soma_time1 = soma_time1 + pontuacao['pontuacao']
            time1_id = pontuacao['id_time']


        if pontuacao['id_time'] == '2':
            soma_time2 = soma_time2 + pontuacao['pontuacao']
            time2_id = pontuacao['id_time']

    # Soma ponto
    for ponto in usuario:
        if ponto['time'] == time1_id:
            soma_usuario_time1 = soma_usuario_time1 + ponto['pontuacao']
        if ponto['time'] == time2_id:
            soma_usuario_time2 = soma_usuario_time2 + ponto['pontuacao']

    if soma_time1 == soma_usuario_time1:
        print("Pontuação time 1 não houve alteração")
    else:
        soma_time1 = soma_usuario_time1
        time1['pontuacao'] = soma_time1
        edit_file('id_time', time1_id, time1, 'times.txt')

    if soma_time2 == soma_usuario_time2:
        print("Pontuação do time 2 não houve alteração")
    else:
        soma_time2 = soma_usuario_time2
        time2['pontuacao'] = soma_time2

        edit_file('id_time', time2_id, time2, 'times.txt')

    print("** Atualização feita com sucesso **\n")


while True:
    print("Gerenciamento de times")
    print("1 - Criar times")
    print("2 - Atualizar placar")
    print("3 - EndGame")
    print("4 - Zerar pontuação dos usuários")
    print("0 - Sair")
    escolha = int(input("Digite uma das opções acima: "))

    if escolha == 1:
        print(" ** Criar Time ** ")
        nome_time = input("Digite o nome do time: ")
        id_time = input("1 ou 2 ? ")
        pontuacao_inicial = 0

        time = {
            'nome_time': nome_time,
            'id_time': id_time,
            'pontuacao': pontuacao_inicial
        }

        insert_file(time, 'times.txt')

        print(" ** TIME CADASTRADO ** ")

    if escolha == 2:
        atualizar_placar()

    if escolha == 3:
        print("** Para iniciar um novo jogo digite o nome dos dois novos times **")
        nome_time_1 = input("Digite o nome do time 1: ")
        nome_time_2 = input("Digite o nome do time 2: ")

        time1 = find_file('id_time', '1', 'times.txt')
        time2 = find_file('id_time', '2', 'times.txt')

        remover_file('id_time', time1['id_time'], 'times.txt')
        novo_time1 = {
            'nome_time': nome_time_1,
            'id_time': '1',
            'pontuacao': 0
        }
        insert_file(novo_time1, 'times.txt')

        remover_file('id_time', time2['id_time'], 'times.txt')

        novo_time2 = {
            'nome_time': nome_time_2,
            'id_time': '2',
            'pontuacao': 0
        }

        insert_file(novo_time2, 'times.txt')

        usuarios = show_file('usuarios.txt')

        for usuario in usuarios:
            id_usuario = usuario['id']
            usuario['pontuacao'] = 0
            edit_file('id', id_usuario, 'pontuacao', 'usuarios.txt')

    if escolha == 4:
        print("*****")
        usuarios = show_file('usuarios.txt')

        for usuario in usuarios:
            id_usuario = usuario['id']
            usuario['pontuacao'] = 0
            edit_file('id', id_usuario, usuario, 'usuarios.txt')

    if escolha == 0:
        break
