import base_palabras
import plotly.express as px

import pandas as pd
bp = base_palabras

def entra_texto(texto):
    """
    Recibe como entrada un texto y retorna
        a) el texto en minúsculas
        b) texto sin puntuación (split)
        Esto último servirá para contar las palabras
    """
    # para introducir el texto, la línea siguiente:
    # texto = input("Texto:   ")

    texto_en_minusculas = texto.lower()

    texto_sin_puntuacion = texto_en_minusculas.replace(".", "").replace(",", "").replace(";", "").replace("...", ""). \
        replace("¡", "").replace("!", "").replace("¿", "").replace("?", "".replace("(", "").replace(")", ""))

    texto_sin_puntuacion_split = texto_sin_puntuacion.split()

    return texto_en_minusculas, texto_sin_puntuacion_split

def analisis_palabras(texto_sin_puntuacion_split):
    """
    lista palabras es la lista de palabras del texto
    pero con separación en dos palabras de aquellas que son
    palabras compuestas compo "ético-crítico",
     Pendiente los adverbios terminados en mente, como "sutilmente".
     Pendiente resumir para número de palabras
    """
    numero_de_palabras = len(texto_sin_puntuacion_split)
    lista_palabras = []

    for palabra in texto_sin_puntuacion_split:

        hasta_guion = palabra.find("-")

        if hasta_guion != -1:
            punto_del_guion = hasta_guion
            largo_palabra = len(palabra)
            item_1 = palabra[0:punto_del_guion]
            item_2 = palabra[punto_del_guion + 1:largo_palabra]
            lista_palabras.append(item_1)
            lista_palabras.append(item_2)
        else:
            lista_palabras.append(palabra)

    return lista_palabras, numero_de_palabras

def cambia_a_sin_diptongos(texto):
    texto_sin_diptongos = texto. \
        replace("au", "a").replace("ai", "a").replace("ia", "a").replace("ua", "a"). \
        replace("áu", "á").replace("ái", "á").replace("iá", "á").replace("uá", "á"). \
        replace("ui", "i").replace("iu", "u"). \
        replace("eu", "e").replace("ue", "e").replace("ei", "e").replace("ie", "e"). \
        replace(" éu", "é").replace("ué", "é").replace("éi", "é").replace("ié", "é"). \
        replace("ou", "o").replace("uo", "o").replace("io", "o").replace("oi", "o"). \
        replace("óu", "ó").replace("uó", "ó").replace("ió", "ó").replace("ói", "ó")
    return (texto_sin_diptongos)

def elimina_grafemas_consonantes(texto_sin_diptongo):
    texto = texto_sin_diptongo
    ultimo_caracter = texto[-1]

    texto_sin_grafemas_consonantes = texto.replace("b", "").replace("c", "").replace("d", ""). \
        replace("f", "").replace("gue", "e").replace("gui", "i"). \
        replace("gü", "u").replace("g", "").replace("h", "").replace("j", ""). \
        replace("k", "").replace("l", "").replace("m", "").replace("n", ""). \
        replace("ñ", "").replace("p", "").replace("q", "").replace("r", ""). \
        replace("s", "").replace("t", "").replace("v", "").replace("x", ""). \
        replace(" y ", "  ").replace("y, ", " ").replace("z", "")

    return texto_sin_grafemas_consonantes, ultimo_caracter

def transcriptor(texto_en_minusculas):
    """
    Recibe como entrada texto_en_minusculas
        hace la transcripción fonológica en varios pasos
        vocales acentuadas gráficamente se representan en mayúsculas.
        Esta información será útil para la identificación de la sílaba tónica en las palabras.
    """

    # Primeras sustituciones
    ##  finales diptongos conserva tilde en las tónicas
    ##  consonantes

    # En estos remplazos, las vocales tildadas se transcriben con acento

    remplazos = [("oy ", "oi "), ("oy,", "oi,"), ("oy.", "oi."), ("oy;", "oi;"),
                 ("oy)", "oi)"), ("oy?", "oi?"), ("oy!", "oi!"),
                 ("ey ", "ei "), ("ey,", "ei,"), ("ey.", "ei."), ("ey;", "ei;"),
                 ("ey)", "ei)"), ("ey?", "ei?"), ("ey!", "ei!"),
                 ("uy ", "ui "), ("uy,", "ui,"), ("uy.", "ui."), ("uy;", "ui;"),
                 ("uy)", "ui)"), ("uy?", "ui?"), ("uy!", "ui!"),
                 ("ay ", "ai "), ("ay,", "ai,"), ("ay.", "ai."), ("ay;", "ai;"),
                 ("ay)", "ai)"), ("ay?", "ai?"), ("ay!", "ai!"),
                 ("óy ", "ói "), ("óy,", "ói,"), ("óy.", "ói."), ("óy;", "ói;"),
                 ("óy)", "ói)"), ("óy?", "ói?"), ("óy!", "ói!"),
                 ("éy ", "éi "), ("éy,", "éi,"), ("éy.", "éi."), ("éy;", "éi;"),
                 ("éy)", "éi)"), ("éy?", "éi?"), ("éy!", "éi!"),
                 ("úy ", "úi "), ("úy,", "úi,"), ("úy.", "úi."), ("úy;", "úi;"),
                 ("úy)", "úi)"), ("úy?", "úi?"), ("úy!", "úi!"),
                 ("áy ", "ái "), ("áy,", "ái,"), ("áy.", "ái."), ("áy;", "ái;"),
                 ("áy)", "ái)"), ("áy?", "ái?"), ("áy!", "ái!"),
                 ## consonantes
                 ("v", "b"),
                 ("ce", "se"), ("ci", "si"), ("cé", "sé"), ("cí", "sí"),
                 ("ca", "ka"), ("co", "ko"), ("cu", "ku"),
                 ("cá", "ká"), ("có", "kó"), ("cú", "kú"),
                 ("cr", "kɾ"),
                 ("ch", "∫"),
                 ("c", "k"),
                 (" x", "s"), ("x", "ks"), ("meksi", "mexi"),
                 ("j", "x"), ("ge", "xe"), ("gi", "xi"),
                 ("w", "g"),
                 ("ya", "ça"), ("ye", "çe"), ("yi", "çi"), ("yo", "ço"), ("yu", "çu"),
                 ("yá", "çA"), ("yé", "çE"), ("yí", "çI"), ("yó", "çO"), ("yú", "çU"),
                 ("ny", "nç"),
                 ("y", "i"), ("ll", "ç"), ("qu", "k"),
                 ("z", "s"), ("gue", "ge"), ("gui", "gi"), ("rr", "00"), ("ar", "aɾ"), ("er", "eɾ"), ("ir", "iɾ"),
                 ("or", "oɾ"), ("ur", "uɾ"),
                 ("gué", "gé"), ("guí", "gí"), ("ár", "áɾ"), ("ér", "éɾ"), ("ír", "íɾ"),
                 ("ór", "óɾ"), ("úr", "úɾ"),
                 ("gr", "gɾ"), ("br", "bɾ"), ("pr", "pɾ"), ("tr", "tɾ"), ("dr", "dɾ"),
                 ("fr", "fɾ"), ("cl", "kl"), ("00", "r"), ("h", ""), ("ü", "u")]

    transcripcion_1 = texto_en_minusculas

    for remplazoFonemas in remplazos:
        transcripcion_1 = transcripcion_1.replace(remplazoFonemas[0], remplazoFonemas[1])

    transcripcion_1a = transcripcion_1.replace(",", "|").replace(".", "‖ ").replace(";", "‖ ").replace(":",
                                                                                                       "| ").replace(
        "…", "| ").replace("...", "| ").replace("-", "| ").replace("¿", "").replace("?", "‖ ").replace("¡", "").replace(
        "!", "‖ ").replace("(", "| ").replace(")", "|").replace('"', '|').replace("'", "|")

    # Instala los archifonemas

    transcripcion_1b = transcripcion_1a.replace('n b', 'N b').replace('m b', 'N b').replace('m n', 'N n'). \
        replace('n d', 'N d').replace('n f', 'N f').replace('n g', 'N g').replace('n x', 'N x'). \
        replace('n k', 'N k').replace('n l', 'N l').replace('n m', 'N m').replace('n n', 'N n'). \
        replace('n ñ', 'N ñ').replace('n p', 'N p').replace('n r', 'N r').replace('n s', 'N s'). \
        replace('n t', 'N t').replace('n ç', 'N ç').replace('nb', 'Nb').replace('mb', 'Nb'). \
        replace('mn', 'Nm'). \
        replace('n∫', 'N∫').replace('nd', 'Nd').replace('nf', 'Nf').replace('ng', 'Ng'). \
        replace('nx', 'Nx').replace('nk', 'Nk').replace('nl', 'Nl').replace('nm', 'Nm'). \
        replace('nn', 'Nn').replace('np', 'Np').replace('nr', 'Nr').replace('ns', 'Ns'). \
        replace('nt', 'Nt').replace('n|', 'N|').replace('n‖', 'N‖').replace('m|', 'N|'). \
        replace('mp', 'Np').replace('mb', 'Nb').replace('m p', 'N p').replace('m b', 'N b'). \
        replace('m‖', 'N‖').replace('ɾ b', 'R b').replace('ɾ ∫', 'R ∫').replace('ɾ d', 'R d'). \
        replace('ɾ f', 'R f').replace('ɾ g', 'R g').replace('ɾ x', 'R x').replace('ɾ k', 'R k'). \
        replace('ɾ l', 'R l').replace('ɾ m', 'R m').replace('ɾ R', 'ɾ R').replace('ɾ ɲ', 'R ɲ'). \
        replace('ɾ p', 'R p').replace('ɾ r', 'R r').replace('ɾ s', 'R s').replace('ɾ t', 'R t'). \
        replace('ɾ y', 'R y').replace('ɾb', 'Rb').replace('ɾ∫', 'R∫').replace('ɾd', 'Rd'). \
        replace('ɾf', 'Rf').replace('ɾg', 'Rg').replace('ɾx', 'Rx').replace('ɾk', 'Rk'). \
        replace('ɾl', 'Rl').replace('ɾm', 'Rm').replace('ɾR', 'ɾR').replace('ɾñ', 'Rñ'). \
        replace('ɾp', 'Rp').replace('ɾr', 'Rr').replace('ɾs', 'Rs').replace('ɾt', 'Rt'). \
        replace('ɾç', 'Rç').replace('ɾ|', 'R|').replace('ɾ‖', 'R‖').replace('b b', 'B b'). \
        replace('b d', 'B d'). \
        replace('b f', 'B f').replace('b g', 'B g').replace('b x', 'B x').replace('b k', 'B k'). \
        replace('b l', 'B l').replace('b m', 'B m').replace('b r', 'B r').replace('b ɲ', 'B ñ'). \
        replace('b p', 'B p').replace('b s', 'B s').replace('b t', 'B t').replace('b y', 'B y'). \
        replace('bb', 'Bb').replace('b∫', 'B∫').replace('bd', 'Bd').replace('bf', 'Bf'). \
        replace('bg', 'Bg').replace('bx', 'Bx').replace('bk', 'Bk').replace('bm', 'Bm'). \
        replace('bñ', 'Bñ').replace('bp', 'Bp').replace('bs', 'Bs').replace('bt', 'Bt'). \
        replace('bʝ', 'Bʝ').replace('p b', 'p b').replace('p ∫', 'p ∫').replace('p d', 'p d'). \
        replace('p f', 'p f').replace('p g', 'p g').replace('p x', 'p x').replace('p k', 'p k'). \
        replace('p l', 'p l').replace('p m', 'p m').replace('p r', 'p r').replace('p ñ', 'p ñ'). \
        replace('p p', 'p p').replace('p s', 'p s').replace('p t', 'p t').replace('p ç', 'p ç'). \
        replace('pb', 'Bb').replace('p∫', 'B∫').replace('pd', 'Bd').replace('pf', 'Bf'). \
        replace('pg', 'Bg').replace('px', 'Bx').replace('pk', 'Bk').replace('pm', 'Bm'). \
        replace('pñ', 'Bñ').replace('pp', 'Bp').replace('ps', 'Bs').replace('pt', 'Bt'). \
        replace('pç', 'Bç').replace('p‖', 'B‖').replace('b|', 'B|').replace('b‖', 'B‖'). \
        replace('d b', 'D b').replace('d ∫', 'D ∫').replace('d d', 'D d').replace('d f', 'D f'). \
        replace('d g', 'D g').replace('d x', 'D x').replace('d k', 'D k').replace('d l', 'D l'). \
        replace('d m', 'D m').replace('d r', 'D r').replace('d ñ', 'D ñ'). \
        replace('d p', 'D p').replace('d r', 'D r').replace('d s', 'D s').replace('d t', 'D t'). \
        replace('d ç', 'D ç').replace('db', 'Db').replace('d∫', 'D∫').replace('df', 'Df'). \
        replace('dg', 'Dg').replace('dx', 'Dx').replace('dk', 'Dk'). \
        replace('dl', 'Dl').replace('dm', 'Dm').replace('dñ', 'Dñ').replace('dp', 'Dp'). \
        replace('ds', 'Ds').replace('dt', 'Dt').replace('dç', 'Dç').replace('d|', 'D|'). \
        replace('d‖', 'D‖').replace('t b', 'D b').replace('t c', 'D c').replace('t d', 'D d'). \
        replace('t f', 'D f').replace('t g', 'D g').replace('t x', 'D x').replace('t k', 'D k'). \
        replace('t l', 'D l').replace('t m', 'D m').replace('t r', 'D r').replace('t ñ', 'D ñ'). \
        replace('t p', 'D p').replace('t r', 'D r').replace('t s', 'D s').replace('t t', 'D t'). \
        replace('t ç', 'D ç').replace('tb', 'Db').replace('t∫', 'D∫').replace('td', 'Dd'). \
        replace('tf', 'Df').replace('tg', 'Dg').replace('tx', 'Dx').replace('tk', 'Dk'). \
        replace('tm', 'Dm').replace('tñ', 'Dñ').replace('tp', 'Dp').replace('ts', 'Ds'). \
        replace('tt', 'Dt').replace('tç', 'Dç').replace('t|', 'D|').replace('t‖', 'D‖'). \
        replace('g b', 'G b').replace('g d', 'G d').replace('g ∫', 'G ∫').replace('g d', 'G d'). \
        replace('g f', 'G f').replace('g g', 'G g').replace('g x', 'G x'). \
        replace('g k', 'G k').replace('g l', 'G l').replace('g m', 'G m').replace('g r', 'G r'). \
        replace('g ñ', 'G ñ').replace('g p', 'G p').replace('g r', 'G r').replace('g s', 'G s'). \
        replace('g t', 'G t').replace('g ç', 'G ç').replace('gb', 'Gb').replace('gd', 'Gd'). \
        replace('g∫', 'G∫').replace('gd', 'Gd').replace('gf', 'Gf').replace('gg', 'Gg'). \
        replace('gx', 'Gx').replace('gk', 'Gk').replace('gm', 'Gm').replace('gñ', 'Gñ'). \
        replace('gp', 'Gp').replace('gs', 'Gs').replace('gt', 'Gt').replace('gç', 'Gç'). \
        replace('g|', 'G|').replace('g‖', 'G‖').replace('k b', 'G b').replace('k d', 'G d'). \
        replace('k ∫', 'G ∫').replace('k d', 'G d').replace('k f', 'G f').replace('k g', 'G g'). \
        replace('k x', 'G x').replace('k k', 'G k').replace('k l', 'G l').replace('k m', 'G m'). \
        replace('k r', 'G r').replace('k ñ', 'G ñ').replace('k p', 'G p').replace('k r', 'G r'). \
        replace('k s', 'G s').replace('k t', 'G t').replace('k ç', 'G ç').replace('kb', 'Gb'). \
        replace('kd', 'Gd').replace('k∫', 'G∫').replace('kd', 'Gd').replace('kf', 'Gf'). \
        replace('kg', 'Gg').replace('kx', 'Gx').replace('kk', 'Gk').replace('km', 'Gm'). \
        replace('kñ', 'Gñ').replace('kp', 'Gp').replace('ks', 'Gs').replace('kt', 'Gt'). \
        replace('kç', 'Gç').replace('k|', 'G|').replace('k‖', 'G‖')

    transcripcion_1c = transcripcion_1b.replace('∫', 't͡∫').replace("ç", "ʝ").replace("ñ", "ɲ")

    return transcripcion_1c

def identificador_silaba_tonica(lista_palabras):
    # La lista compleja de palabras tiene [palabra, palabra sin consonantes, tónica o átona y posición sílaba tónica]

    lista_compleja_palabras = []

    for palabra in lista_palabras:

        palabra_sin_diptongos = cambia_a_sin_diptongos(palabra)

        texto_sin_grafemas_consonantes, ultimo_caracter = elimina_grafemas_consonantes(palabra_sin_diptongos)

        ene_silabas = len(texto_sin_grafemas_consonantes)

        if ene_silabas == 1:
            if palabra in bp.monosilabos_atonos:
                pal_tonica = False
                posicion_tonica = "0"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter])

            elif palabra not in bp.monosilabos_atonos:
                pal_tonica = True
                posicion_tonica = "1"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter])

        elif ene_silabas == 2 and palabra in bp.bisilabos_atonos:
            pal_tonica = False
            posicion_tonica = "0"
            lista_compleja_palabras.append(
                [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter])

        elif ene_silabas >= 2:

            pal_tonica = True

            if ene_silabas > 3 and texto_sin_grafemas_consonantes[-4] in bp.vocales_acentuadas:
                posicion_tonica = "-4"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter])
            elif ene_silabas > 2 and texto_sin_grafemas_consonantes[-3] in bp.vocales_acentuadas:
                posicion_tonica = "-3"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter])
            # graves y agudas con acento escrito

            elif ene_silabas > 1 and texto_sin_grafemas_consonantes[-2] in bp.vocales_acentuadas:
                posicion_tonica = "-2"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter])

            elif ene_silabas > 1 and texto_sin_grafemas_consonantes[-1] in bp.vocales_acentuadas:
                posicion_tonica = "-1"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter])

            # graves y agudas sin acento escrito
            elif ene_silabas > 1 and ((texto_sin_grafemas_consonantes[-2] not in bp.vocales_acentuadas) and (
                    texto_sin_grafemas_consonantes[-1] not in bp.vocales_acentuadas)) and \
                    (ultimo_caracter not in bp.revision_grafema_final):
                posicion_tonica = "-1"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter])

            elif ene_silabas > 1 and ((texto_sin_grafemas_consonantes[-1] not in bp.vocales_acentuadas) and (
                    texto_sin_grafemas_consonantes[-2] not in bp.vocales_acentuadas)) and \
                    ultimo_caracter in bp.revision_grafema_final:
                posicion_tonica = "-2"
                lista_compleja_palabras.append(
                    [palabra, ene_silabas, pal_tonica, posicion_tonica, ultimo_caracter])

    return lista_compleja_palabras

def cuantificador_basico_tipos_de_palabras(lista_compleja_palabras):
    contador_monosilabos = 0
    contador_monosilabos_tonicos = 0
    contador_monosilabos_atonos = 0
    contador_bisilabos_atonos = 0
    contador_agudas = 0
    contador_graves = 0
    contador_esdrujulas = 0
    contador_otros_casos = 0

    letras_finales_palabras_graves = []

    for item_complejo in lista_compleja_palabras:
        ene_silabas_del_item = item_complejo[1]
        tonicidad_del_item = item_complejo[2]
        posicion_del_acento = item_complejo[3]
        letra_final_del_item = item_complejo[4]

        if ene_silabas_del_item == 1:
            contador_monosilabos = contador_monosilabos + 1
            if tonicidad_del_item == 1:
                contador_monosilabos_tonicos = contador_monosilabos_tonicos + 1
            else:
                contador_monosilabos_atonos = contador_monosilabos_atonos + 1
        elif ene_silabas_del_item == 2:
            if tonicidad_del_item == False:
                contador_bisilabos_atonos = contador_bisilabos_atonos + 1

        if posicion_del_acento == '-1':
            contador_agudas = contador_agudas + 1
        elif posicion_del_acento == '-2':
            contador_graves = contador_graves + 1
            letras_finales_palabras_graves.append(letra_final_del_item)
        elif posicion_del_acento == '-3':
            contador_esdrujulas = contador_esdrujulas + 1
        else:
            contador_otros_casos = contador_otros_casos + 1

    return contador_monosilabos, contador_monosilabos_tonicos, contador_monosilabos_atonos, contador_bisilabos_atonos, \
        contador_agudas, contador_graves, contador_esdrujulas, contador_otros_casos, letras_finales_palabras_graves

def contar_letras_finales(letras_finales_palabras_graves):

    vocales_al_final = (letras_finales_palabras_graves.count("a")) + (letras_finales_palabras_graves.count("e")) + (
        letras_finales_palabras_graves.count("i")) + (letras_finales_palabras_graves.count("o")) + (
                           letras_finales_palabras_graves.count("u"))

    consonantes_n_s_al_final = (letras_finales_palabras_graves.count("n")) + (letras_finales_palabras_graves.count("s"))
    otras_consonantes_finales =  (len(letras_finales_palabras_graves)) - (vocales_al_final + consonantes_n_s_al_final)

    print("Letras finales en las palabras graves:")
    print("      Graves terminadas en vocal: ", vocales_al_final)
    print("      Graves terminadas en n o s: ", consonantes_n_s_al_final)
    print("      Graves terminadas en otras consonantes : ", otras_consonantes_finales)

    return vocales_al_final, consonantes_n_s_al_final, otras_consonantes_finales

def reporte_palabras(contador_monosilabos, contador_monosilabos_tonicos, contador_monosilabos_atonos,\
                     contador_bisilabos_atonos, contador_agudas, contador_graves, contador_esdrujulas):

    print("Número total de palabras:", contador_monosilabos  + \
                     contador_bisilabos_atonos + contador_agudas + contador_graves + contador_esdrujulas)
    print("------")
    print("Número de monosílabos:", contador_monosilabos)
    print("------")
    print("Número de bisílabos átonos", contador_bisilabos_atonos)
    print("------")
    print("Número de palabras agudas, graves y esdrújulas:", contador_graves+contador_esdrujulas+contador_agudas)
    print("------")
    print("Monosílabos:")
    print("     Número de monosílabos tónicos:", contador_monosilabos_tonicos)
    print("     Número de monosílabos átonos:" , contador_monosilabos_atonos)
    print("------")
    print("Agudas, graves y esdrújulas:")
    print("     Número de palabras agudas:", contador_agudas)
    print("     Número de palabras graves:", contador_graves)
    print("     Número de palabras esdrújulas:", contador_esdrujulas)

def diccionarios_con_valores_generales(contador_monosilabos_tonicos, contador_monosilabos_atonos,
                                       contador_bisilabos_atonos, contador_agudas, contador_graves,
                                       contador_esdrujulas, vocales_al_final, consonantes_n_s_al_final,
                                       otras_consonantes_finales):

# No crea diccionarios sino que crea dos objetos que se pueden coordinar con .pd

    categoria_letras_finales = ["Vocales N o S", "Otras consonantes"]
    valores_letras_finales = [vocales_al_final + consonantes_n_s_al_final, otras_consonantes_finales]

    categorias = ["Monosilabos tónicos", "Monosílabos átonos", "Bisílabos átonos","Palabras agudas","Palabras graves",
                  "Palabras esdrújulas" ]
    valores = [contador_monosilabos_tonicos, contador_monosilabos_atonos, contador_bisilabos_atonos, contador_agudas,
               contador_graves, contador_esdrujulas]
    return (categorias, valores, categoria_letras_finales, valores_letras_finales)

def graficos_para_ortografia_leyes_generales(categorias, valores, categoria_letras_finales, valores_letras_finales):

    df = pd.DataFrame(dict(
        grupo1=categorias,
        grupo2=valores
    ))
    fig = px.bar(df, x='grupo1', y='grupo2', color = 'grupo1', labels = {'grupo1': 'Categoría de palabras',
                                                                         'grupo2': 'Número de ocurrencias'})
    fig.show()


    fig = px.pie(df, values = 'grupo2', names = 'grupo1', title = "Distribución de palabras por tipo")
    fig.show()



    df2 = pd.DataFrame(dict(
        categ = categoria_letras_finales,
        valor = valores_letras_finales
    ))
    fig = px.bar(df2, x='categ', y='valor', color = 'categ', labels = {'categ': 'Letras finales',
                                                                       'valor': 'Número de ocurrencias'})
    fig.show()

def graficos_resultados_cuenta_tipos_palabras(contador_monosilabos, contador_monosilabos_tonicos,
                                              contador_monosilabos_atonos, contador_bisilabos_atonos,
                                              contador_agudas, contador_graves, contador_esdrujulas,
                                              contador_otros_casos, letras_finales_palabras_graves):

    categoria_de_palabras = ["Monosílabos", "Bisílabos átonos", "Agudas", "Graves", "Esdrújulas"]
    ene_por_categ_de_palabras = [contador_monosilabos, contador_bisilabos_atonos, contador_agudas, contador_graves,
                                 contador_esdrujulas]

    df3 = pd.DataFrame(dict(
        tipos = categoria_de_palabras,
        valores = ene_por_categ_de_palabras
    ))
    fig = px.bar(df3, x = 'tipos', y = 'valores', color = 'tipos', labels = {'tipos': 'Categoría de las palabras',
                                                                             'valores': 'Número de ocurrencias'})
    fig.show()


    # monosílabos y bisílabos átonos

    monos = ["Monosílabos tónicos", "Monosílabos átonos", "Bisílabos átonos"]
    val_mono = [contador_monosilabos_tonicos, contador_monosilabos_atonos, contador_bisilabos_atonos]

    df4 = pd.DataFrame(dict(
        tip = monos,
        valtip = val_mono
    ))
    fig = px.bar(df4, x = 'tip', y = 'valtip', title = "Palabras menores", labels = {'tip': "Tipos de palabras",
                                                                                     'valtip': "Número de ocurrencias"},
                 color = 'tip')

    fig.show()


