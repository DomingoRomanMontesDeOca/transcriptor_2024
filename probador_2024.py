import funciones_2024

fun = funciones_2024

texto = input("Texto:   ")

texto_en_minusculas, texto_sin_puntuacion_split = fun.entra_texto(texto)

lista_palabras, numero_de_palabras = fun.analisis_palabras(texto_sin_puntuacion_split)

transcripcion_1c = fun.transcriptor(texto_en_minusculas)

lista_compleja_palabras = fun.identificador_silaba_tonica(lista_palabras)

(contador_monosilabos, contador_monosilabos_tonicos, contador_monosilabos_atonos, contador_bisilabos_atonos, \
        contador_agudas, contador_graves, contador_esdrujulas, contador_otros_casos, letras_finales_palabras_graves,
            vocal_final_palabras_graves, ene_silabas_palabras_graves, contador_ene_sil_2, contador_ene_sil_3,
            contador_ene_sil_4, contador_ene_sil_5, contador_ene_sil_plus_5) \
    = fun.cuantificador_basico_tipos_de_palabras(lista_compleja_palabras)


fun.reporte_palabras(contador_monosilabos, contador_monosilabos_tonicos, contador_monosilabos_atonos,\
                    contador_bisilabos_atonos, contador_agudas, contador_graves, contador_esdrujulas)

contador_n_s_vocal, contador_otras_consonantes = fun.contar_letras_finales(letras_finales_palabras_graves)

categorias, valores = fun.reporte_palabras(contador_monosilabos, contador_monosilabos_tonicos,
                                           contador_monosilabos_atonos,contador_bisilabos_atonos, contador_agudas,
                                           contador_graves, contador_esdrujulas)

fun.graficos_para_ortografia_leyes_generales(categorias, valores, contador_n_s_vocal, contador_otras_consonantes)

fun.graficos_resultados_cuenta_tipos_palabras(contador_monosilabos, contador_monosilabos_tonicos,
                                              contador_monosilabos_atonos, contador_bisilabos_atonos,
                                              contador_agudas, contador_graves, contador_esdrujulas,
                                              contador_otros_casos, letras_finales_palabras_graves,
                                              vocal_final_palabras_graves, ene_silabas_palabras_graves)

fun.graficar_data_palabras_graves(contador_ene_sil_2, contador_ene_sil_3, contador_ene_sil_4, contador_ene_sil_5,
                                  contador_ene_sil_plus_5)