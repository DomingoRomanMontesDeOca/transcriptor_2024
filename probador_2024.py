import funciones_2024

import base_palabras

bp = base_palabras

fun = funciones_2024


texto = "La niña ríe y canta con alegría en el parque. El sol brilla sobre su pelo rubio mientras corre detrás de un globo. \
Escucha el chirrido de los pájaros y el ruido de la fuente. Siente el suave viento y el frescor de la brisa marina. \
¡Qué bello día para disfrutar!"

texto_en_minusculas, texto_sin_puntuacion_split = fun.entra_texto(texto)

lista_palabras, numero_de_palabras = fun.analisis_palabras(texto_sin_puntuacion_split)

transcripcion_1c = fun.transcriptor(texto_en_minusculas)

lista_compleja_palabras = fun.identificador_silaba_tonica(lista_palabras)

contador_monosilabos, contador_monosilabos_tonicos, contador_monosilabos_atonos, contador_bisilabos_atonos, contador_agudas, contador_graves, contador_esdrujulas, contador_otros_casos, letras_finales_palabras_graves = fun.cuantificador_basico_tipos_de_palabras(lista_compleja_palabras)



print("Entrada: \n", texto)
print(".....................")
print(lista_palabras)
print(".....................")
print("En minúsculas: \n", texto_en_minusculas)
print(".....................")
print("Transcripción 1c :\n", transcripcion_1c)
print(".....................")
print(lista_compleja_palabras)
print(".....................")
print("El texto tiene ", numero_de_palabras, " palabras")
print("El texto tiene ", contador_monosilabos, " monosílabos")
print("El texto tiene ", contador_monosilabos_tonicos, " monosílabos tónicos")
print("El texto tiene ", contador_monosilabos_atonos, " monosílabos átonos")
print("El texto tiene ", contador_bisilabos_atonos, " bisílabos átonos")
print("El texto tiene ", contador_agudas, " palabras agudas")
print("El texto tiene ", contador_graves, " palabras graves")
print("El texto tiene ", contador_esdrujulas, " palabras esdrújulas")
print(letras_finales_palabras_graves)
print(len(letras_finales_palabras_graves))

print(contador_monosilabos + contador_bisilabos_atonos + contador_agudas + contador_graves + contador_esdrujulas)
print(numero_de_palabras)

fun.contar_letras_finales(letras_finales_palabras_graves)