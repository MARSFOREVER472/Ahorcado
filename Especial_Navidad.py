import random # VARIABLE ALEATORIA.

def reach_random_word(): # DEFINIMOS PALABRAS ALEATORIAS.
    words = ["adorno", "arbol", "bola", "bota", "claus", "copo", "estrella", "grinch", "muñeco", "navidad", "nieve", "nochebuena", "noel", "papa", "pascua", "santa"] # MEDIANTE UN DICCIONARIO DE PALABRAS, SE DEFINEN MANUALMENTE AL MOMENTO DE DELETREAR CUALQUIER PALABRA AL AZAR.
    random_word = random.choice(words) # PALABRAS ALEATORIAS INGRESADAS AL DICCIONARIO DE PALABRAS.
    return random_word # RETORNA UNA PALABRA ALEATORIA.

def show_board(secret_word, guessing_letters): # EN EL TABLERO SE MUESTRAN TODAS LAS PALABRAS ADIVINADAS YA DEFINIDAS POR LETRAS EN EL JUEGO.
    board="" # TABLERO DE PALABRAS ADIVINADAS.

    # LAS PALABRAS ADIVINADAS SE DEFINEN POR CARACTERES DISCRETAMENTE:

    for letter in secret_word: # POR CADA LETRA EN UNA PALABRA SECRETA.
        if letter in guessing_letters: # SI UNA LETRA DE UNA O MÁS ADIVINADAS, ACIERTA AL CAMPO VACÍO DE UNA LETRA.
            board += letter # SUMA 1 ACIERTO POR LETRA.

        else: # EN CASO CONTRARIO...
            board += "_" # NO ACIERTA NADA.
    print(board) # IMPRIME EL TABLERO DE PALABRAS.

def hanged_game(): # AHORA SE PROCEDE A JUGAR AL AHORCADO.
    secret_word = reach_random_word() # LA PALABRA SECRETA SERÁ ACERTADA CUANDO ELIGE UNA LETRA AL AZAR.
    guessing_letters = [] # LAS LETRAS ADIVINADAS SE DEFINEN MEDIANTE CAMPOS VACÍOS POR DEFECTO.
    times_remaining = 6 # LA CANTIDAD DE INTENTOS RESTANTES COMIENZA EN 6 INTENTOS SI ES QUE FALLA VA RESTANDO 1 INTENTO MENOS.

    while times_remaining > 0: # MIENTRAS QUE CANTIDAD DE INTENTOS RESTANTES SON MAYORES QUE 0.
        show_board(secret_word, guessing_letters) # EL TABLERO MUESTRA LAS PALABRAS ACERTADAS.
        letter = input("ENTER ANOTHER LETTER: ").lower() # LA LETRA INGRESADA SERÁ MINÚSCULA.

        if letter in guessing_letters: # SI UNA LETRA ES LA MISMA QUE INGRESÓ ANTERIORMENTE.
            print("YA INGRESASTE UNA LETRA,\nINTÉNTALO NUEVAMENTE CON OTRA LETRA!") # ELIGE OTRA LETRA QUE NO SEA LA MISMA.
            continue # PUEDE CONTINUAR EL JUEGO SIN FINALIZARLO.

        if letter in secret_word: # SI UNA LETRA HACE ALUSIÓN A UNA PALABRA SECRETA.
            guessing_letters.append(letter) # REFIÉRASE A UNA LETRA ADIVINADA EN EL SISTEMA.
            if set(guessing_letters) == set(secret_word): # SI LOGRA ACERTAR UNA LETRA A LA PALABRA SECRETA.
                print("FELICIDADES, HAS ACERTADO LA PALABRA!!!!!")
                break

        else: # EN CASO CONTRARIO CUANDO FALLA UNA LETRA EN UNA PALABRA SECRETA.
            times_remaining -= 1 # EL NÚMERO DE INTENTOS REDUCIRÁ EN 1.
            print(f"LETRA INCORRECTA\nTE QUEDAN {times_remaining}")
    
    if times_remaining == 0: # SI NO QUEDAN NINGÚN INTENTO.
        print(f"HAS PERDIDO.\nLA PALABRA SECRETA ERA: {secret_word}")

hanged_game()