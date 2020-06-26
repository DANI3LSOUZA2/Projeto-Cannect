def insert_file(objeto, name_file):

    import simplejson

    # Reading file
    try:
        f = open(name_file, 'r')

        filecontents = simplejson.load(f)
    except:
        filecontents = []
    finally:
        # Close file
        f.close()

    # Writing file
    try:
        f = open(name_file, 'w')
        filecontents.append(objeto)
        simplejson.dump(filecontents, f)

    except:
        print('Erro ao escrever arquivo, motivo: ', ValueError)


    finally:
        # Close file
        f.close()


def edit_file(find_column, pesq, edit_row, name_file):

    import simplejson

    # Reading file
    try:
        f = open(name_file, 'r')
        filecontents = simplejson.load(f)


        cont = 0
        for row in filecontents:

            if row[find_column] == pesq:
                filecontents[cont] = edit_row
                break

            cont += 1

    except:
        filecontents = []
    finally:
        # Close file
        f.close()


    # Writing file
    try:
        f = open(name_file, 'w')

        simplejson.dump(filecontents, f)

    except:
        print('Erro ao escrever arquivo, motivo: ', ValueError)
    finally:
        # Close file
        f.close()


def remover_file(find_column, pesq, name_file):

    import simplejson

    # Reading file
    try:
        f = open(name_file, 'r')
        filecontents = simplejson.load(f)


        cont = 0
        for row in filecontents:

            if row[find_column] == pesq:

                del filecontents[cont]

                break

            cont += 1

    except:
        filecontents = []
    finally:
        # Close file
        f.close()


    # Writing file
    try:
        f = open(name_file, 'w')

        if len(filecontents) == 0:
            filecontents = None

        simplejson.dump(filecontents, f)

    except:
        print('Erro ao escrever arquivo, motivo: ', ValueError)
    finally:
        # Close file
        f.close()



def find_file(name_column, pesq, name_file):

    import simplejson

    result = None

    # Reading file
    try:
        f = open(name_file, 'r')
        filecontents = simplejson.load(f)

        for row in filecontents:
            value = row[name_column]

            if value == pesq:
                # object found
                result = row

    except:
        print('Erro ao ler arquivo, motivo: ', ValueError)
    finally:
        # Close file
        f.close()


    return result


def show_file(name_file):

    import simplejson

    result = None

    # Reading file
    try:
        f = open(name_file, 'r')
        result = simplejson.load(f)


    except:
        print('Erro ao ler arquivo, motivo: ', ValueError)
    finally:
        # Close file
        f.close()

    return result
