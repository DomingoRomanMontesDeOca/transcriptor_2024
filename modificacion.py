

transcripcion1c = "la niɲa ríe i kaNta kon alegɾía en el paRke‖  el sol bɾiʝa sobɾe su pelo rubio mieNtɾas kore detɾás de uN globo‖ "

lista_compleja = [['la', 1, False, '0', 'a'], ['niña', 2, True, '-2', 'a'], ['ríe', 2, True, '-2', 'e'], ['y', 1, False, '0', 'y'], ['canta', 2, True, '-2', 'a'], ['con', 1, False, '0', 'n'], ['alegría', 4, True, '-2', 'a'], ['en', 1, False, '0', 'n'], ['el', 1, False, '0', 'l'], ['parque', 2, True, '-2', 'e'], ['el', 1, False, '0', 'l'], ['sol', 1, True, '1', 'l'], ['brilla', 2, True, '-2', 'a'], ['sobre', 2, True, '-2', 'e'], ['su', 1, False, '0', 'u'], ['pelo', 2, True, '-2', 'o'], ['rubio', 2, True, '-2', 'o'], ['mientras', 2, True, '-2', 's'], ['corre', 2, True, '-2', 'e'], ['detrás', 2, True, '-1', 's'], ['de', 1, False, '0', 'e'], ['un', 1, False, '0', 'n'], ['globo', 2, True, '-2', 'o']]

#print(transcripcion1c)

#print(lista_compleja)

# poner acento

transcripcion1c_split = transcripcion1c.split()

#print(transcripcion1c_split)

#print(len(transcripcion1c_split))

largo1= len(transcripcion1c_split)

largo2 = len(lista_compleja)


if largo1 == largo2:

    print("Okis. Las longitudes coinciden")

    lista_compleja_2 = zip(transcripcion1c_split, lista_compleja)

    lista_compleja_2_b = (list(lista_compleja_2))
