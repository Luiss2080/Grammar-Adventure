import pygame
import random
import sys
import os

# Inicializar pygame
pygame.init()
pygame.mixer.init()

# Configurar pantalla
ANCHO, ALTO = 800, 600
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
AZUL = (27, 19, 66)
TAMAÑO_FUENTE = 35
TIPO = "Grammar Adventure\Font\Pixellettersfull-BnJ5.ttf"
FUENTE = pygame.font.Font(TIPO, TAMAÑO_FUENTE)
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Grammar Adventure")
posiciones_corazones = [(ANCHO - 60 - i * 60, 0)
                        for i in range(3)]  # 3 corazones espaciados por 60 píxeles
 
# Cargar archivos de sonido e imágenes
directorio_material = os.path.join(os.getcwd(), "Grammar Adventure\Material")

sonidos = {
    "Stage1.wav": pygame.mixer.Sound(os.path.join(directorio_material, "Stage1.wav")),
    "Correcta.wav": pygame.mixer.Sound(os.path.join(directorio_material, "Correcta.wav")),
    "ganador.wav": pygame.mixer.Sound(os.path.join(directorio_material, "ganador.wav")),
    "equivocado.wav": pygame.mixer.Sound(os.path.join(directorio_material, "equivocado.wav")),
    "Stage2.wav": pygame.mixer.Sound(os.path.join(directorio_material, "Stage2.wav")),
    "Title.wav": pygame.mixer.Sound(os.path.join(directorio_material, "Title.wav")),
    "GameOver.wav": pygame.mixer.Sound(os.path.join(directorio_material, "GameOver.wav")),
    "Stage4.wav": pygame.mixer.Sound(os.path.join(directorio_material, "Stage4.wav")),
    "Stage3.wav": pygame.mixer.Sound(os.path.join(directorio_material, "Stage3.wav"))
}

imagenes = {
    "Will.jpg": os.path.join(directorio_material, "Will.jpg"),
    "Comparativos.jpg": os.path.join(directorio_material, "Comparativos.jpg"),
    "PresentPerfect.png": os.path.join(directorio_material, "PresentPerfect.png"),
    "PastSimple.png": os.path.join(directorio_material, "PastSimple.jpg"),
    "corazon.png": os.path.join(directorio_material, "corazon.png"),
    "logo.png": os.path.join(directorio_material, "Logo.jpg"),
    "Signo.png": os.path.join(directorio_material, "Signo.png"),
    "Boton.png": os.path.join(directorio_material, "Boton.png"),
    "rule1.png": os.path.join(directorio_material, "rule1.png"),
    "rule2.png": os.path.join(directorio_material, "rule2.png"),
    "stage1_mascota.gif": os.path.join(directorio_material, "rule1.png"),
    "rule1.png": os.path.join(directorio_material, "rule1.png"),
    "rule1.png": os.path.join(directorio_material, "rule1.png"),
    "rule1.png": os.path.join(directorio_material, "rule1.png"),
}

# Estructura de temas
temas = {
    "Simple Past": {
        "fondo": sonidos["Stage1.wav"],
        "clic": sonidos["Correcta.wav"],
        "exito": sonidos["ganador.wav"],
        "fracaso": sonidos["equivocado.wav"],
        "imagen_fondo": imagenes["PastSimple.png"],
        "imagen_corazon": imagenes["corazon.png"],
        "frases": [
            ("She _ the tree (climb)", "climbed"),
            ("They _ for two hours (wait)", "waited"),
            ("The train _ at the station (stop)", "stopped"),
            ("We _ the suitcases from the airport (carry)", "carried"),
            ("Everybody _. It was a funny joke (laugh)", "laughed"),
            ("I did not _ home after work (walk)", "walk"),
            ("I did not _ the party last night (like)", "like"),
            ("We _ Seville University on the bus (pass)", "passed"),
            ("No one _ at the end of the song (clap)", "clapped"),
            ("Did mary _ yesterday? (walk)", "walk"),
            ("Did you _ your homework? (finish)", "finish"),
            ("Tom _ _ _ his grandmother (not/visit)", "did not visit"),
            ("Did you _ to your mother? (listen)", "listen"),
            ("Mary _ off the tree (fall)", "fell"),
            ("Did you _ your breakfast? (eat)", "eat"),
            ("Sarah _ her new car (wash)", "washed"),
            ("Did you _ the movie? (enjoy)", "enjoy"),
            ("Jack _ his phone (lose)", "lost"),
            ("Did you _ to the doctor? (go)", "go"),
            ("The children _ in the park (play)", "played"),
            ("You _ your keys (find)", "found"),
            ("Did you _ the news? (hear)", "hear"),
            ("Tim _ the train (miss)", "missed"),
            ("She _ her ankle (twist)", "twisted"),
            ("Did you _ the test? (take)", "take"),
            ("He _ the vase (break)", "broke"),
            ("Ben _ the game (watch)", "watched"),
            ("The children _ in the park (run)", "ran"),
            ("Shakira _ in the concert (sing)", "sang"),
            ("Pedro _ his shoes (wear)", "wore"),
            ("Did you _ your room? (clean)", "clean")
        ]
    },
    "Comparatives and Superlatives": {
        "fondo": sonidos["Stage2.wav"],
        "clic": sonidos["Correcta.wav"],
        "exito": sonidos["ganador.wav"],
        "fracaso": sonidos["equivocado.wav"],
        "imagen_fondo": imagenes["Comparativos.jpg"],
        "imagen_corazon": imagenes["corazon.png"],
        # Agregar oraciones aquí
        "frases": [("La Paz is _ _ Santa Cruz (cold)", "colder than"),
                   ("Bugatti is _ _ Ferrari (fast)", "faster than"),
                   ("Susan is _ _ Maria (old)", "older than"),
                   ("Health is _ _ than money (important)", "more important"),
                   ("My sister is _ _ than Gina (lazy)", "lazier than"),
                   ("He is _ _ in his class (young)", "the youngest"),
                   ("Sarah is _ _ Emily (tall)", "taller than"),
                   ("Coca cola is the _ _ drink ever (popular)", "most popular"),
                   ("Patience is _ _ virtue (great)", "the greatest"),
                   ("The sun is _ _ the Earth (hot)", "hotter than"),
                   ("I am _ _ student in class (good)", "the best"),
                   ("She is the _ _ in her family (intelligent)", "most intelligent"),
                   ("My hair is _ _ yours (long)", "longer than"),
                   ("Lago Titicaca is _ _ lake in Sudamerica (large)", "the largest"),
                   ("Mike is _ _ Josh (fat)", "fatter than"),
                   ("Oruro is _ _ city in Bolivia (coldest)","the coldest"),
                   ("Jim Carrey is _ _ Eugenio Derbez (funny)","funnier than"),
                   ("His score was _ _ in the competition (high)","the highest"),
                   ("A car is _ _ a motorcycle (heavy)", "heavier than"),
                   ("My job is the _ _ stresful one (stresful)","most stresful"),
                   ("My house is _ _ yours (small)","smaller than"),
                   ("Chinese is the _ _ language (difficult)","most difficult"),
                   ("My dog is _ _ yours (friendly)","friendlier than"),
                   ("Mt. Everest is _ _ mountain in the world (tall)","the tallest"),
                   ("iPhone is _ _ than Samsung (expensive)","more expensive"),
                   ("Coffee is _ _ than tea (addictive)","more addictive"),
                   ("Steel is _ _ iron (hard)","harder than"),
                   ("This computer is _ _ I have used (fast)","the fastest"),
                   ("Jill is _ _ Gina (pretty)","prettier than")
                   ]
    },
    "Present Perfect": {
        "fondo": sonidos["Stage3.wav"],
        "clic": sonidos["Correcta.wav"],
        "exito": sonidos["ganador.wav"],
        "fracaso": sonidos["equivocado.wav"],
        "imagen_fondo": imagenes["PresentPerfect.png"],
        "imagen_corazon": imagenes["corazon.png"],
        # Agregar oraciones aquí
        "frases": [("She _ _ to the movies (go)", "has gone"),
                   ("I _ _ living in Bolivia this year(be)", "have been"),
                   ("They _ _ bananas this morning (eat)", "have eaten"),
                   ("Have you _ the letter? (write)", "written"),
                   ("I _ _ dinner for us (cook)", "have cooked"),
                   ("He _ _ that movie before (see)","has seen"),
                   ("We _ _ for the test (study)","have studied"),
                   ("It _ _ all day (rain)","has rained"),
                   ("Maria _ _ that book twice (read)","has read"),
                   ("Pedro _ _ the house (clean)","has cleaned" ),
                   ("Oriente _ _ the championship (win)","have won"),
                   ("Miguel _ _ to the beach (go)","has gone"),
                   ("We _ _ the museum (visit)","have visited"),
                   ("Jeff _ _ the dog for a walk (take)","has taken"),
                   ("I _ _ the assignment (complete)","have completed"),
                   ("He _ _ to many countries (travel)","has traveled"),
                   ("I _ _ my degree (finish)","have finished"),
                   ("He _ _ his arm (break)","has broken"),
                   ("Has he _ to ski? (learn)","learned"),
                   ("Has she _ a new job? (find)","found"),
                   ("I _ _ your brother (meet)","have met"),
                   ("Has she _ a song? (sing)","sung"),
                   ("They _ _ the kitchen (renovate)","have renovated"),
                   ("Has he _ the driving test? (pass)","passed"),
                   ("Have they a_ a puppy? (adopt)","adopted"),
                   ("Has Luis _ spanish for two years? (study)","studied"),
                   ("I _ _ a mistake (make)","have made"),
                   ("Pedro _ _ Maria (kiss)","has kissed")]
    },
    "Future with will / going to": {
        "fondo": sonidos["Stage4.wav"],
        "clic": sonidos["Correcta.wav"],
        "exito": sonidos["ganador.wav"],
        "fracaso": sonidos["equivocado.wav"],
        "imagen_fondo": imagenes["Will.jpg"],
        "imagen_corazon": imagenes["corazon.png"],
        # Agregar oraciones aquí, si faltan el programa se va a colgar
        "frases": [("I _ _ _ to Bolivia next year (won't/go)", "will not go"),
                    ("I _ _ to the movies tonight (be/go)", "am going"),
                    ("Pepe _ _ call you later (won't)", "will not"),
                    ("She is _ _ _ a new business (go/start)", "going to start"),
                    ("It _ _ tomorrow (will/rain)", "will rain"),
                    ("Sasha _ _ a doctor (will/be)", "will be"),
                    ("Pedro _ _ a car next month (will/buy)", "will buy"),
                    ("She _ _ going to make dinner tonight (be/not)", "is not"),
                    ("Will she _ to play the guitar? (learn)", "learn"),
                    ("I _ _ you with your homework (will/help)", "will help"),
                    ("She is _ _ _ a dance class (go/join)", "going to join"),
                    ("I _ _ money for vacations (will/save)", "will save"),
                    ("I _ _ _ my project next week (won't/finish)", "will not finish"),
                    ("We are _ _ _ the project by tomorrow (go/complete)","going to complete"),
                    ("John _ _ _ the report by the deadline (won't/complete)","will not complete"),
                    ("She _ _ _ to me by tomorrow (won't/speak)", "will not speak"),
                    (" _ she run the marathon next week? (will)", "will"),
                    ("I am _ _ _ the walls right now (go/paint)", "going to paint"),
                    ("I _ _ _ to call you on your birthday (won't/forget)","will not forget"),
                    ("I _ _ my birthday this year (will/celebrate)","will celebrate"),
                    ("Liam _ _ _ learn french this month (be/go)","is going to"),
                    ("I _ _ _ my birthday this year (won't/celebrate)","will not celebrate"),
                    ("She is _ _ _ to Europe tomorrow (go/travel)","going to travel"),
                    ("James is going to _ his kitchen next month (renovate)","renovate"),
                    ("Pedro _ _ with me for this (will/fight)","will fight"),
                    ("I am _ _ _ Game of Thrones (go/watch)","going to watch"),
                    ("This kid is _ _ _ very loud (go/scream)","going to scream"),
                    ("Carlos _ _ a lot of money (will/pay)","will pay")

                   ]
    }
}

frases_recientes = []
# Otras variables del juego
reloj = pygame.time.Clock()
puntuacion = 0
vidas = 3
texto_ingresado = ""
frases_en_pantalla = []
tiempo_inicio = None
tema_actual = None
velocidad_palabra = 0.4
imagen_corazon = pygame.image.load(imagenes["corazon.png"])
# Ajusta el tamaño según sea necesario
imagen_corazon = pygame.transform.scale(imagen_corazon, (70, 70))

# Función para generar una nueva frase
sonidos["Title.wav"].play()


def nueva_frase(tema):
    global frases_recientes
    if not tema:
        return None

    # Obtener una nueva frase aleatoria que no esté en las frases recientes
    nueva_frase_data = None
    while nueva_frase_data is None:
        indice_frase = random.randint(0, len(temas[tema]["frases"]) - 1)
        frase, palabra_correcta = temas[tema]["frases"][indice_frase]
        if frase not in frases_recientes:
            nueva_frase_data = {
                "frase": frase,
                "indice_palabra_faltante": frase.index("_"),
                "palabra_correcta": palabra_correcta,
                "x": 0,
                "y": random.randint(50, 500),
                "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            }

    # Agregar la nueva frase a la lista de frases recientes
    frases_recientes.append(nueva_frase_data["frase"])

    # Limitar la lista de frases recientes para que no sea demasiado larga
    if len(frases_recientes) > 10:
        frases_recientes = frases_recientes[1:]

    return nueva_frase_data
# Ventana principal


def ventana_principal():
    PANTALLA.fill(AZUL)

    # Load and display the logo off-screen
    logo = pygame.image.load(imagenes["logo.png"])
    logo = pygame.transform.scale(logo, (400, 400))
    logo_rect = logo.get_rect(center=(-200, ALTO // 3))  # Start off-screen
    PANTALLA.blit(logo, logo_rect)

    # Define the target position for the logo (center of the screen)
    target_position = pygame.Rect(ANCHO // 2 - 200, ALTO // 3, 400, 400)

    # Slide the logo to the center of the screen
    while logo_rect.x < target_position.x:
        PANTALLA.fill(AZUL)
        logo_rect.x += 5  # Adjust the sliding speed as needed
        PANTALLA.blit(logo, logo_rect)
        pygame.display.flip()
        pygame.time.delay(20)

    # Load button images
    boton_reglas_img = pygame.image.load(imagenes["Boton.png"])
    boton_niveles_img = pygame.image.load(imagenes["Boton.png"])

    # Resize button images as needed
    boton_reglas_img = pygame.transform.scale(boton_reglas_img, (200, 50))
    boton_niveles_img = pygame.transform.scale(boton_niveles_img, (200, 50))

    # Button rects
    boton_reglas = boton_reglas_img.get_rect(
        topleft=(ANCHO // 4 - 100, ALTO // 2 + 100))
    boton_niveles = boton_niveles_img.get_rect(
        topleft=(ANCHO // 4 * 3 - 100, ALTO // 2 + 100))

    # Blit button images onto the screen
    PANTALLA.blit(boton_reglas_img, boton_reglas)
    PANTALLA.blit(boton_niveles_img, boton_niveles)

    # texto en los botones
    texto_reglas = FUENTE.render("Rules", True, NEGRO)
    PANTALLA.blit(texto_reglas, (boton_reglas.x + 60, boton_reglas.y + 10))

    texto_niveles = FUENTE.render("Play the Game", True, NEGRO)
    PANTALLA.blit(texto_niveles, (boton_niveles.x + 12, boton_niveles.y + 10))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_reglas.collidepoint(evento.pos):
                    mostrar_reglas()
                elif boton_niveles.collidepoint(evento.pos):
                    menu_niveles()

        pygame.display.flip()

# Ventana de reglas



#LUIS
def mostrar_reglas():
    PANTALLA.fill(AZUL)
    texto_reglas = FUENTE.render("RULES OF THE GAME:", True, BLANCO)
    PANTALLA.blit(texto_reglas, (20, 20))

    # imagen regla 1
    rule1 = pygame.image.load(imagenes["rule1.png"])
    rule1 = pygame.transform.scale(rule1, (490, 80))
    rule1_rect = rule1.get_rect(center=(300, 190))
    PANTALLA.blit(rule1, rule1_rect)

    # imagen regla 2
    rule2 = pygame.image.load(imagenes["rule2.png"])
    rule2 = pygame.transform.scale(rule2, (180, 70))
    rule2_rect = rule1.get_rect(center=(400, 340))
    PANTALLA.blit(rule2, rule2_rect)

    reglas = [
        "1. A phrase with a missing word will appear on the screen.",
        "",
        "",
        "2. Type the correct word to score points.",
        "",
        "",
        "3. As your score goes up, more phrases will appear on screen.",
        "5. No contractions allowed.",
        "6. You lose one life for every phrase missed.",
        "7. The game ends when you run out of lives."
    ]

    y = 100
    for regla in reglas:
        texto_regla = FUENTE.render(regla, True, BLANCO)
        PANTALLA.blit(texto_regla, (20, y))
        y += 50

    # Cargar imagen del botón
    boton_img = pygame.image.load(imagenes["Boton.png"])
    boton_img = pygame.transform.scale(
        boton_img, (150, 50))  # Escalar según sea necesario

    # Obtener el rectángulo del botón de volver y establecer su tamaño según la imagen
    boton_volver = boton_img.get_rect(bottomright=(ANCHO - 20, ALTO - 20))

    # Dibujar la imagen del botón en lugar del rectángulo rojo
    PANTALLA.blit(boton_img, boton_volver)

    # Renderizar texto en el botón
    texto_volver = FUENTE.render("Volver", True, NEGRO)
    PANTALLA.blit(texto_volver, (boton_volver.x + 35, boton_volver.y + 10))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.collidepoint(evento.pos):
                    ventana_principal()

        pygame.display.flip()

# Menu de niveles


def menu_niveles():
    global tema_actual
    PANTALLA.fill(AZUL)
    texto_menu = FUENTE.render("Select a Chapter:", True, BLANCO)
    PANTALLA.blit(texto_menu, (ANCHO // 2 - 100, 50))

    y = 100
    botones_niveles = []
    for tema in temas.keys():
        boton_nivel = pygame.Rect(
            ANCHO // 2 - 200, y, 400, 50)  # Adjust width here
        botones_niveles.append(boton_nivel)
        # Load button image
        boton_img = pygame.image.load(imagenes["Boton.png"])
        boton_img = pygame.transform.scale(
            boton_img, (400, 50))  # Adjust width here
        PANTALLA.blit(boton_img, boton_nivel)

        # Render the text
        texto_tema = FUENTE.render(tema, True, NEGRO)
        # Calculate the position to center the text within the button
        text_x = boton_nivel.x + \
            (boton_nivel.width - texto_tema.get_width()) // 2
        text_y = boton_nivel.y + \
            (boton_nivel.height - texto_tema.get_height()) // 2
        PANTALLA.blit(texto_tema, (text_x, text_y))

        y += 100

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                for i, boton in enumerate(botones_niveles):
                    if boton.collidepoint(evento.pos):
                        tema_actual = list(temas.keys())[i]
                        bucle_juego()

        pygame.display.flip()

# Bucle del juego


def bucle_juego():
    global puntuacion, vidas, texto_ingresado, frases_en_pantalla, tiempo_inicio

    jugando = True
    temporizador_puntuacion = 0
    duracion_puntuacion = 60  # Duración en frames (1 segundo a 60 FPS)
    posicion_puntuacion = None

    # Cargar fondo, signo y sonido del nivel
    fondo = pygame.image.load(temas[tema_actual]["imagen_fondo"])
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    signo = pygame.image.load(imagenes["Signo.png"])
    signo = pygame.transform.scale(signo, (350, 158))
    sonido_nivel = temas[tema_actual]["fondo"]
    sonido_nivel.play(-1)  # Reproducir sonido en bucle

    tiempo_inicio = pygame.time.get_ticks()  # Obtener el tiempo de inicio





#JEFER
    while jugando:

        while jugando:
            PANTALLA.blit(fondo, (0, 0))  # Dibujar fondo

            # Draw a rectangle around the text "Points: {puntuacion}"
            texto_puntuacion = FUENTE.render(
                f"Points: {puntuacion}", True, ROJO)
            rect_puntuacion = texto_puntuacion.get_rect(topleft=(10, 10))
            # Fill the rectangle with white color
            pygame.draw.rect(PANTALLA, BLANCO, rect_puntuacion)
            PANTALLA.blit(texto_puntuacion, (10, 10))
            # Dibujar corazones
            for i, (x, y) in enumerate(posiciones_corazones[:vidas]):
                PANTALLA.blit(imagen_corazon, (x, y))

            PANTALLA.blit(signo, (230, 518))  # Dibujar signo
            # Manejo de eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    jugando = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        jugando = False
                        sonido_nivel.stop()
                        game_over()
                    elif evento.key == pygame.K_BACKSPACE:
                        texto_ingresado = texto_ingresado[:-1]
                    else:
                        texto_ingresado += evento.unicode

            # Agregar más frases gradualmente según la puntuación
            while len(frases_en_pantalla) < (puntuacion // 8) + 1:
                nueva_frase_data = nueva_frase(tema_actual)
                if nueva_frase_data:
                    frases_en_pantalla.append(nueva_frase_data)
                else:
                    break  # No hay más frases en el tema actual

                # Update the velocidad_palabra based on puntuacion
            velocidad_palabra = 0.4 + (puntuacion/50)

            # Dibujar frases y verificar colisiones
            for frase in frases_en_pantalla[:]:
                # Renderizar texto con fondo blanco
                texto_con_fondo = FUENTE.render(
                    frase["frase"], True, NEGRO, BLANCO)
                rect_fondo = texto_con_fondo.get_rect(
                    topleft=(frase["x"], frase["y"]))
                PANTALLA.fill(BLANCO, rect_fondo)
                PANTALLA.blit(texto_con_fondo, rect_fondo)
                frase["x"] += velocidad_palabra

                if frase["x"] > ANCHO:
                    frases_en_pantalla.remove(frase)
                    vidas -= 1
                    temas[tema_actual]["fracaso"].play()
                    if vidas == 0:
                        jugando = False
                        pygame.time.delay(4000)
                        temas[tema_actual]["fondo"].stop()
                        game_over()

                if texto_ingresado.strip().lower() == frase["palabra_correcta"].lower():
                    puntuacion += 1
                    temas[tema_actual]["clic"].play()
                    # Encontrar la frase correcta y eliminarla
                    for p in frases_en_pantalla:
                        if p["palabra_correcta"].lower() == frase["palabra_correcta"].lower():
                            frases_en_pantalla.remove(p)
                            # Establecer la posición de la puntuación
                            if not posicion_puntuacion:
                                posicion_puntuacion = p["x"]
                            break  # Salir del bucle después de eliminar la frase correcta
                    texto_ingresado = ""  # Limpiar texto ingresado después de una palabra correcta
                    temporizador_puntuacion = duracion_puntuacion

            # Mostrar puntuación
            tiempo_transcurrido = (
                pygame.time.get_ticks() - tiempo_inicio) / 1000
            texto_puntuacion = FUENTE.render(
                f"Points: {puntuacion}", True, ROJO)
            PANTALLA.blit(texto_puntuacion, (10, 10))

            # Mostrar tiempo transcurrido
            texto_tiempo = FUENTE.render(f"Time: {int(tiempo_transcurrido)}s", True, ROJO)
            rect_tiempo = texto_tiempo.get_rect(midtop=(ANCHO // 2, 10))
            pygame.draw.rect(PANTALLA, BLANCO, rect_tiempo)  
            PANTALLA.blit(texto_tiempo, rect_tiempo)


            # Mostrar texto ingresado
            texto_ingresado_render = FUENTE.render(
                texto_ingresado, True, NEGRO)
            PANTALLA.blit(texto_ingresado_render, (ANCHO // 2 -
                          texto_ingresado_render.get_width() // 2, ALTO - 50))

            pygame.display.flip()
            reloj.tick(60)
    sonido_nivel.stop()  # Detener el sonido del nivel cuando el juego termina
    pygame.quit()
    sys.exit()


# Función para mostrar pantalla de game over

def game_over():
    global tema_actual, puntuacion, vidas, texto_ingresado, frases_en_pantalla, tiempo_inicio
    PANTALLA.fill(AZUL)
    sonidos["GameOver.wav"].play()
    texto_game_over = FUENTE.render("Game Over!", True, BLANCO)
    PANTALLA.blit(texto_game_over, (ANCHO // 2 -
                  texto_game_over.get_width() // 2, ALTO // 2))

    pygame.display.flip()
    pygame.time.delay(6000)  # Esperar 6 segundos

    # reiniciar stats
    puntuacion = 0
    vidas = 3
    texto_ingresado = ""
    frases_en_pantalla = []
    tiempo_inicio = None
    menu_niveles()

# Función principal


def main():
    ventana_principal()
    bucle_juego()


if __name__ == "__main__":
    main()
