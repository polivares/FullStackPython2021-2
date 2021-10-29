students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(lista):

    for l in lista:
        texto = ''
        '''
        for k in l.keys():
            texto += f'{k} - {l[k]},'
        '''
        for k, v in l.items():
            texto += f'{k} - {v},'

        print(texto[:-1])

iterateDictionary(students)

def iterateDictionary2(llave, lista):
    # Primero recorro la lista
    for i in lista:
        if llave in i.keys():
            print(i[llave])
        else:
            print("Llave no existente:", llave)
            break

iterateDictionary2('apellido', students)