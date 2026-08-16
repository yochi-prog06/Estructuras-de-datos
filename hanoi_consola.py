"""
Torres de Hanoi - Interfaz de CONSOLA (ASCII)
=============================================
Esta interfaz usa la lógica pura de hanoi.py y dibuja las torres
en la terminal con caracteres ASCII. También muestra una pequeña
gráfica de barras con el avance del juego.
"""

from typing import List

from hanoi import TorresDeHanoi


def pedir_entero(mensaje: str, minimo: int = 1, maximo: int = 10) -> int:
    """Pide un número entero al usuario dentro de un rango."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"✗ Ingresa un número entre {minimo} y {maximo}.")
        except ValueError:
            print("✗ Entrada inválida. Debes ingresar un número entero.")


def _render_torre(nombre: str, discos: List[int], num_discos: int,
                  ancho_max: int) -> List[str]:
    """
    Convierte una torre en una lista de líneas (strings) para dibujarla.
    Cada disco se dibuja como un bloque proporcional a su tamaño.
    """
    lineas: List[str] = []
    # Rellenamos desde la cima hacia abajo para alinear las torres.
    for nivel in range(num_discos - 1, -1, -1):
        if nivel < len(discos):
            tam = discos[nivel]
            bloque = "█" * (tam * 2 + 1)
            lineas.append(bloque.center(ancho_max))
        else:
            lineas.append("│".center(ancho_max))
    # Base de la torre
    lineas.append("█" * ancho_max)
    lineas.append(f"  {nombre}  ".center(ancho_max))
    return lineas


def mostrar(juego: TorresDeHanoi) -> None:
    """Dibuja las tres torres una al lado de la otra en la consola."""
    estado = juego.estado_torres()
    ancho_torre = juego.num_discos * 2 + 3
    columnas = [
        _render_torre(n, estado[n], juego.num_discos, ancho_torre)
        for n in ("A", "B", "C")
    ]
    alto = len(columnas[0])

    print("\n" + "=" * (ancho_torre * 3))
    for fila in range(alto):
        print("".join(col[fila] for col in columnas))
    print("=" * (ancho_torre * 3))
    print(
        f"Movimientos realizados: {juego.movimientos}  |  "
        f"Óptimo: {juego.movimientos_optimos()}"
    )


def grafica_avance(juego: TorresDeHanoi) -> None:
    """
    Gráfica de barras simple en consola: muestra cuántos discos hay
    en cada torre como barras horizontales.
    """
    estado = juego.estado_torres()
    print("\n  Gráfica de avance (discos por torre):")
    for nombre in ("A", "B", "C"):
        cantidad = len(estado[nombre])
        barra = "#" * cantidad + "-" * (juego.num_discos - cantidad)
        print(f"  Torre {nombre}: |{barra}| {cantidad}")


def menu_principal() -> None:
    """Menú principal del juego."""
    print("\n" + "═" * 50)
    print("   TORRES DE HANOI — CONSOLA (PILAS/Stacks)")
    print("═" * 50)
    print("1. Jugar manualmente")
    print("2. Ver solución automática (demostración)")
    print("3. Regresar al menú principal")
    print("═" * 50)


def jugar_manualmente() -> None:
    """Bucle de juego interactivo."""
    n = pedir_entero("¿Cuántos discos quieres? (1-8): ", 1, 8)
    juego = TorresDeHanoi(num_discos=n)
    print("\nObjetivo: mueve todos los discos de A hasta C.")
    print("Regla: nunca pongas un disco grande sobre uno más pequeño.\n")
    mostrar(juego)
    grafica_avance(juego)

    while not juego.ganado:
        print("\nEscribe 'salir' para abandonar.")
        cmd = input("Mover (origen destino), ej. 'A C': ").strip().lower()
        if cmd in ("salir", "exit", "quit"):
            print("Juego abandonado.")
            return
        partes = cmd.split()
        if len(partes) != 2:
            print("✗ Formato inválido. Ejemplo: A C")
            continue
        exito, mensaje = juego.mover(partes[0], partes[1])
        if exito:
            print(f"✓ {mensaje}")
        else:
            print(f"✗ {mensaje}")
        mostrar(juego)
        grafica_avance(juego)

    print("\n🎉 ¡Felicidades! Has resuelto las Torres de Hanoi.")
    print(f"Movimientos usados: {juego.movimientos}")
    print(f"Movimientos óptimos: {juego.movimientos_optimos()}")
    if juego.movimientos == juego.movimientos_optimos():
        print("⭐ ¡Lograste la solución ÓPTIMA!")
    else:
        print(f"💡 La solución óptima usa {juego.movimientos_optimos()} movimientos.")


def jugar_automatico() -> None:
    """Solución automática demostrando la recursión."""
    n = pedir_entero("¿Cuántos discos? (1-8): ", 1, 8)
    juego = TorresDeHanoi(num_discos=n)
    movimientos = juego.resolver()

    print(f"\nSolución óptima para {n} discos ({len(movimientos)} movimientos):\n")
    input("Presiona Enter para empezar la demostración paso a paso...")

    for i, mov in enumerate(movimientos, 1):
        origen, destino = mov.split(">")
        exito, mensaje = juego.mover(origen, destino)
        if not exito:
            print(f"✗ Error inesperado: {mensaje}")
            return
        print(f"\nPaso {i}/{len(movimientos)}: {mensaje}")
        mostrar(juego)
        grafica_avance(juego)
        if i < len(movimientos):
            input("Presiona Enter para continuar...")

    print("\n🎉 Solución completada de forma óptima.")
    print(f"Total de movimientos: {juego.movimientos}")


def main_consola() -> None:
    """Menú principal de la interfaz de consola."""
    while True:
        menu_principal()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            jugar_manualmente()
        elif opcion == "2":
            jugar_automatico()
        elif opcion == "3":
            print("Regresando al menú principal...")
            break
        else:
            print("✗ Opción no válida.")