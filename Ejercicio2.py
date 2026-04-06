def resolver_fidelidad_manual():
    #leemos la primera línea para obtener N, M, S
    primera_linea = input().strip().split()
    if not primera_linea:
        return

    n = int(primera_linea[0])
    m = int(primera_linea[1])
    s = int(primera_linea[2])

    #mapeamos cada terminal a su respectivo socio
    terminal_a_socio = {}
    for _ in range(m):
        # aqui se lee exactamente M líneas
        datos = input().strip().split()
        id_socio = int(datos[0])
        id_terminal = int(datos[1])
        terminal_a_socio[id_terminal] = id_socio

    #preparamos el diccionario para contar
    conteo_por_socio = {i: {} for i in range(1, n + 1)}

    #se procesa exactamente las S líneas de transacciones
    for _ in range(s):
        datos = input().strip().split()
        id_cliente = int(datos[0])
        id_terminal_compra = int(datos[1])

        if id_terminal_compra in terminal_a_socio:
            socio_actual = terminal_a_socio[id_terminal_compra]
            if id_cliente not in conteo_por_socio[socio_actual]:
                conteo_por_socio[socio_actual][id_cliente] = 0
            conteo_por_socio[socio_actual][id_cliente] += 1

    #imprimimos los resultados
    for socio in range(1, n + 1):
        clientes_del_socio = conteo_por_socio[socio]

        if not clientes_del_socio:
            print(f"{socio} -1")
        else:
            cliente_mas_fiel = max(clientes_del_socio.keys(), key=lambda x: (clientes_del_socio[x], -x))
            print(f"{socio} {cliente_mas_fiel}")


if __name__ == "__main__":
    resolver_fidelidad_manual()