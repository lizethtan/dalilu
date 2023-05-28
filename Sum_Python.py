def mostrar_cancion(letra):
    canciones_gidle = {
        'l': 'LATATA',
        'h': 'Hann (Alone)',
        's': 'Senorita',
        'o': 'Oh my god'
    }

    canciones_bts = {
        'd': 'Dope',
        'f': 'Fake Love',
        'i': 'IDOL',
        'b': 'Blood Sweat & Tears'
    }

    letra = letra.lower()

    if letra in canciones_gidle:
        print(f"La canción de (G)I-DLE que comienza con la letra '{letra}' es '{canciones_gidle[letra]}'")
    elif letra in canciones_bts:
        print(f"La canción de BTS que comienza con la letra '{letra}' es '{canciones_bts[letra]}'")
    else:
        print("No se encontró una canción que empiece con esa letra para (G)I-DLE o BTS.")

letra_ingresada = input("Ingresa una letra: ")
mostrar_cancion(letra_ingresada)
#Dana_Lozada
#Canciones
#IEM_ESCUELA_NORMAL_PASTO
#11-1
