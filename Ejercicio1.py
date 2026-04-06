def resolver_enrutamiento():
    #aqui leemos el número de rutas (N)
    n = int(input().strip())

    rutas = []
    for _ in range(n):
        linea = input().strip().split()
        ruta = linea[0]
        #tomamos el contenido principal
        contenido = linea[1]
        #aqui guardamos la ruta dividida por "/"
        rutas.append((ruta.split('/'), contenido))

    #leemos el número de transiciones (M)
    m = int(input().strip())

    #procesamos cada transición
    for _ in range(m):
        transicion = input().strip()
        partes_trans = transicion.split('/')

        encontrado = False

        #buscamos la ruta que coincida con la transición actual
        for partes_ruta, contenido in rutas:
            if len(partes_ruta) == len(partes_trans):
                coincide = True
                parametro = None

                #comparacion de segmento a segmento
                for pr, pt in zip(partes_ruta, partes_trans):
                    if pr.startswith(':'):
                        parametro = pt
                    elif pr != pt:
                        coincide = False
                        break

                if coincide:
                    if parametro:
                        print(f"{contenido} {parametro}")
                    else:
                        print(contenido)
                    encontrado = True
                    break

        #si ninguna ruta coincidió
        if not encontrado:
            print("404 Not Found")


if __name__ == "__main__":
    resolver_enrutamiento()