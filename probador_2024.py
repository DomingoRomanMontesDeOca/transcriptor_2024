import funciones_2024

fun = funciones_2024


texto = "La niña ríe y canta con alegría en el parque. El sol brilla sobre su pelo rubio mientras corre detrás de un globo. \
Escucha el chirrido de los pájaros y el ruido de la fuente. Siente el suave viento y el frescor de la brisa marina. \
¡Qué bello día para disfrutar!"

texto_en_minusculas, texto_sin_puntuacion_split = fun.entra_texto(texto)

lista_palabras, numero_de_palabras = fun.analisis_palabras(texto_sin_puntuacion_split)

transcripcion_1c = fun.transcriptor(texto_en_minusculas)

lista_compleja_palabras = fun.identificador_silaba_tonica(lista_palabras)

contador_monosilabos, contador_monosilabos_tonicos, contador_monosilabos_atonos, contador_bisilabos_atonos, \
    contador_agudas, contador_graves, contador_esdrujulas, contador_otros_casos, letras_finales_palabras_graves \
    = fun.cuantificador_basico_tipos_de_palabras(lista_compleja_palabras)

fun.reporte_palabras(contador_monosilabos, contador_monosilabos_tonicos, contador_monosilabos_atonos,\
                     contador_bisilabos_atonos, contador_agudas, contador_graves, contador_esdrujulas)

vocales_al_final, consonantes_n_s_al_final, otras_consonantes_finales = fun.contar_letras_finales(letras_finales_palabras_graves)


categorias, valores, categoria_letras_finales, valores_letras_finales = fun.diccionarios_con_valores_generales(contador_monosilabos_tonicos, contador_monosilabos_atonos,
                                             contador_bisilabos_atonos, contador_agudas, contador_graves, contador_esdrujulas,
                                             vocales_al_final, consonantes_n_s_al_final,otras_consonantes_finales)



fun.graficos_para_ortografia_leyes_generales(categorias, valores, categoria_letras_finales, valores_letras_finales)

fun.graficos_resultados_cuenta_tipos_palabras(contador_monosilabos, contador_monosilabos_tonicos,
                                              contador_monosilabos_atonos, contador_bisilabos_atonos,
                                              contador_agudas, contador_graves, contador_esdrujulas,
                                              contador_otros_casos, letras_finales_palabras_graves)