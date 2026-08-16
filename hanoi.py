"""
<<<<<<< HEAD
Torres de Hanoi - Juego educativo para entender la estructura de PILAS (Stacks)
================================================================================
=======
Torres de Hanoi - Lógica del juego con PILAS (Stacks)
=====================================================
>>>>>>> 65115aee89f17bd00f473bd088888e3abc55e984

¿Qué es una Pila (Stack)?
-------------------------
Una pila es una estructura de datos lineal que sigue el principio LIFO
(Last In, First Out - Último en entrar, primero en salir). Imagina una pila
de platos: el último plato que pones encima es el primero que retiras.

Operaciones principales de una pila:
- push (apilar): agregar un elemento en la cima.
- pop (desapilar): retirar y devolver el elemento de la cima.
- peek (ver cima): consultar el elemento de la cima sin retirarlo.
- is_empty (¿vacía?): saber si la pila no tiene elementos.
- size (tamaño): cantidad de elementos apilados.

¿Por qué las Torres de Hanoi usan pilas?
----------------------------------------
Cada torre es literalmente una pila de discos. Solo puedes tocar el disco
de la cima (pop) y solo puedes colocar un disco encima de la cima (push).
Esto modela perfectamente el comportamiento LIFO.
<<<<<<< HEAD
"""

from typing import List, Optional
=======

Arquitectura (refactorizada):
- Este módulo contiene SOLO la lógica del juego (sin imprimir en pantalla).
- hanoi_consola.py  -> interfaz de consola (ASCII).
- hanoi_grafico.py  -> interfaz gráfica con tkinter (gráficas simples).
"""

from typing import Dict, List, Optional, Tuple
>>>>>>> 65115aee89f17bd00f473bd088888e3abc55e984


class Pila:
    """
    Implementación de una Pila (Stack) usando una lista interna.

    La cima de la pila es el FINAL de la lista interna, de modo que
    append() y pop() de Python operan en O(1).
    """

    def __init__(self) -> None:
        # La lista interna guarda los elementos. El final = cima de la pila.
        self._elementos: List[object] = []

    def push(self, elemento: object) -> None:
        """Apila un elemento en la cima (tope) de la pila."""
        self._elementos.append(elemento)

    def pop(self) -> object:
        """
        Retira y devuelve el elemento de la cima.
        Lanza ValueError si la pila está vacía.
        """
        if self.is_empty():
            raise ValueError("No se puede desapilar: la pila está vacía.")
        return self._elementos.pop()

    def peek(self) -> object:
        """
        Devuelve el elemento de la cima SIN retirarlo.
        Lanza ValueError si la pila está vacía.
        """
        if self.is_empty():
            raise ValueError("No se puede consultar la cima: la pila está vacía.")
        return self._elementos[-1]

    def is_empty(self) -> bool:
        """Devuelve True si la pila no tiene elementos."""
        return len(self._elementos) == 0

    def size(self) -> int:
        """Devuelve la cantidad de elementos apilados."""
        return len(self._elementos)

    def to_list(self) -> List[object]:
        """
        Devuelve una copia de los elementos desde la base hasta la cima.
        Útil para renderizar las torres visualmente.
        """
        return list(self._elementos)

    def __str__(self) -> str:
        return f"Pila(base -> cima): {self._elementos}"


class TorresDeHanoi:
    """
    Juego de las Torres de Hanoi usando 3 pilas como torres.
<<<<<<< HEAD
=======
    Lógica pura: no imprime ni dibuja; devuelve mensajes de texto
    para que cualquier interfaz (consola o gráfica) los muestre.
>>>>>>> 65115aee89f17bd00f473bd088888e3abc55e984

    Reglas clásicas:
    1. Solo se puede mover un disco a la vez (el de la cima de una torre).
    2. Un disco nunca puede quedar sobre uno más pequeño.
    3. Solo se puede usar la torre de destino (y la auxiliar) como apoyo.

    Objetivo: mover todos los discos desde la torre origen (A) hasta la
    torre destino (C), usando la torre auxiliar (B).
    """

    def __init__(self, num_discos: int = 4) -> None:
        if num_discos < 1:
            raise ValueError("Debe haber al menos 1 disco.")

        self.num_discos = num_discos
        # Tres pilas que representan las torres A, B y C.
<<<<<<< HEAD
        self.torres: dict = {
=======
        self.torres: Dict[str, Pila] = {
>>>>>>> 65115aee89f17bd00f473bd088888e3abc55e984
            "A": Pila(),
            "B": Pila(),
            "C": Pila(),
        }
        # Apilamos los discos del mayor (base) al menor (cima) en la torre A.
        # Usamos números: 1 = disco más pequeño, N = disco más grande.
        for disco in range(num_discos, 0, -1):
            self.torres["A"].push(disco)

        self.movimientos: int = 0
        self.ganado: bool = False
<<<<<<< HEAD

    # --- Lógica del juego -------------------------------------------------

    def mover(self, origen: str, destino: str) -> bool:
        """
        Intenta mover el disco de la cima de `origen` a `destino`.
        Devuelve True si el movimiento fue válido y se realizó.
        Devuelve False si el movimiento es inválido (sin lanzar excepciones
        para que el juego pueda continuar).
=======
        # (origen, destino, disco) del último movimiento válido.
        self.ultimo_movimiento: Optional[Tuple[str, str, int]] = None

    # --- Lógica del juego -------------------------------------------------

    def mover(self, origen: str, destino: str) -> Tuple[bool, str]:
        """
        Intenta mover el disco de la cima de `origen` a `destino`.

        Devuelve una tupla (éxito, mensaje):
        - éxito = True si el movimiento fue válido y se realizó.
        - mensaje describe el resultado (para que la UI lo muestre).
>>>>>>> 65115aee89f17bd00f473bd088888e3abc55e984
        """
        origen = origen.upper()
        destino = destino.upper()

        if origen not in self.torres or destino not in self.torres:
<<<<<<< HEAD
            print("✗ Torres válidas: A, B o C.")
            return False
        if origen == destino:
            print("✗ Origen y destino son la misma torre.")
            return False
        if self.torres[origen].is_empty():
            print(f"✗ La torre {origen} está vacía, no hay disco para mover.")
            return False
=======
            return False, "Torres válidas: A, B o C."
        if origen == destino:
            return False, "Origen y destino son la misma torre."
        if self.torres[origen].is_empty():
            return False, f"La torre {origen} está vacía, no hay disco para mover."
>>>>>>> 65115aee89f17bd00f473bd088888e3abc55e984

        disco_origen = self.torres[origen].peek()

        # Regla: no poner un disco grande sobre uno más pequeño.
        if not self.torres[destino].is_empty():
            disco_destino = self.torres[destino].peek()
            if disco_origen > disco_destino:
<<<<<<< HEAD
                print(
                    f"✗ Movimiento inválido: el disco {disco_origen} no puede "
                    f"ponerse sobre el disco {disco_destino} (más pequeño)."
                )
                return False
=======
                return False, (
                    f"Movimiento inválido: el disco {disco_origen} no puede "
                    f"ponerse sobre el disco {disco_destino} (más pequeño)."
                )
>>>>>>> 65115aee89f17bd00f473bd088888e3abc55e984

        # Movimiento válido: desapilar de origen y apilar en destino.
        disco = self.torres[origen].pop()
        self.torres[destino].push(disco)
        self.movimientos += 1
<<<<<<< HEAD
        print(f"✓ Movimiento {self.movimientos}: {origen} -> {destino} (disco {disco})")

        self._verificar_victoria()
        return True
=======
        self.ultimo_movimiento = (origen, destino, disco)

        self._verificar_victoria()
        return True, f"Movimiento {self.movimientos}: {origen} -> {destino} (disco {disco})"
>>>>>>> 65115aee89f17bd00f473bd088888e3abc55e984

    def _verificar_victoria(self) -> None:
        """
        Victoria: todos los discos apilados en la torre destino (C),
        en orden correcto (mayor abajo, menor arriba).
        Como las reglas garantizan el orden, basta con contar.
        """
        if self.torres["C"].size() == self.num_discos:
            self.ganado = True

    def movimientos_optimos(self) -> int:
        """Número mínimo de movimientos necesarios: 2^n - 1."""
        return 2 ** self.num_discos - 1

<<<<<<< HEAD
    # --- Visualización ----------------------------------------------------

    def _render_torre(self, nombre: str, ancho_max: int) -> List[str]:
        """
        Convierte una torre en una lista de líneas (strings) para dibujarla.
        Cada disco se dibuja como un bloque proporcional a su tamaño.
        """
        discos = self.torres[nombre].to_list()  # base -> cima
        lineas: List[str] = []
        # Rellenamos desde la cima hacia abajo para alinear las torres.
        for nivel in range(self.num_discos - 1, -1, -1):
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

    def mostrar(self) -> None:
        """Dibuja las tres torres una al lado de la otra en la consola."""
        ancho_torre = self.num_discos * 2 + 3
        columnas = [self._render_torre(n, ancho_torre) for n in ("A", "B", "C")]
        alto = len(columnas[0])

        print("\n" + "=" * (ancho_torre * 3))
        for fila in range(alto):
            print("".join(col[fila] for col in columnas))
        print("=" * (ancho_torre * 3))
        print(
            f"Movimientos realizados: {self.movimientos}  |  "
            f"Óptimo: {self.movimientos_optimos()}"
        )
=======
    # --- Estado para la interfaz -----------------------------------------

    def estado_torres(self) -> Dict[str, List[int]]:
        """
        Devuelve los discos de cada torre desde la base hasta la cima.
        Ejemplo: {"A": [4, 3, 2, 1], "B": [], "C": []}
        Útil para que las interfaces dibujen las torres.
        """
        return {nombre: self.torres[nombre].to_list() for nombre in ("A", "B", "C")}
>>>>>>> 65115aee89f17bd00f473bd088888e3abc55e984

    # --- Solución automática (demostración educativa) --------------------

    def resolver(self, n: Optional[int] = None, origen: str = "A",
<<<<<<< HEAD
                 auxiliar: str = "B", destino: str = "C") -> None:
        """
        Resuelve el juego de forma recursiva (algoritmo clásico).
        Muestra la solución óptima paso a paso. Útil para estudiar
        cómo la recursión y las pilas se relacionan.
        """
        if n is None:
            n = self.num_discos
        if n == 1:
            self.mover(origen, destino)
            self.mostrar()
            return
        self.resolver(n - 1, origen, destino, auxiliar)
        self.mover(origen, destino)
        self.mostrar()
        self.resolver(n - 1, auxiliar, origen, destino)


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


def menu_principal() -> None:
    """Menú principal del juego."""
    print("\n" + "═" * 50)
    print("   TORRES DE HANOI — Aprende sobre PILAS (Stacks)")
    print("═" * 50)
    print("1. Jugar manualmente")
    print("2. Ver solución automática (demostración)")
    print("3. Salir")
    print("═" * 50)


def jugar_manualmente() -> None:
    """Bucle de juego interactivo."""
    n = pedir_entero("¿Cuántos discos quieres? (1-8): ", 1, 8)
    juego = TorresDeHanoi(num_discos=n)
    print("\nObjetivo: mueve todos los discos de A hasta C.")
    print("Regla: nunca pongas un disco grande sobre uno más pequeño.\n")
    juego.mostrar()

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
        juego.mover(partes[0], partes[1])
        juego.mostrar()

    print("\n🎉 ¡Felicidades! Has resuelto las Torres de Hanoi.")
    print(f"Movimientos usados: {juego.movimientos}")
    print(f"Movimientos óptimos: {juego.movimientos_optimos()}")
    if juego.movimientos == juego.movimientos_optimos():
        print("⭐ ¡Lograste la solución ÓPTIMA!")


def main() -> None:
    """Punto de entrada del programa."""
    while True:
        menu_principal()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            jugar_manualmente()
        elif opcion == "2":
            n = pedir_entero("¿Cuántos discos? (1-8): ", 1, 8)
            juego = TorresDeHanoi(num_discos=n)
            print("\nSolución automática paso a paso:\n")
            juego.mostrar()
            juego.resolver()
            print("\n🎉 Solución completada de forma óptima.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("✗ Opción no válida.")
=======
                 auxiliar: str = "B", destino: str = "C") -> List[str]:
        """
        Devuelve la lista de movimientos de la solución óptima (2^n - 1),
        en el formato "ORIGEN>DESTINO" (ej. "A>C"). No modifica el juego:
        la interfaz decide cómo aplicarlos (paso a paso o animación).
        """
        if n is None:
            n = self.num_discos
        movimientos: List[str] = []
        self._resolver_rec(n, origen, auxiliar, destino, movimientos)
        return movimientos

    def _resolver_rec(self, n: int, origen: str, auxiliar: str,
                      destino: str, movimientos: List[str]) -> None:
        """Recursión clásica del algoritmo de las Torres de Hanoi."""
        if n == 1:
            movimientos.append(f"{origen}>{destino}")
            return
        self._resolver_rec(n - 1, origen, destino, auxiliar, movimientos)
        movimientos.append(f"{origen}>{destino}")
        self._resolver_rec(n - 1, auxiliar, origen, destino, movimientos)


def main() -> None:
    """Punto de entrada: permite elegir entre la interfaz gráfica o la consola."""
    print("=" * 50)
    print("   TORRES DE HANOI — Aprende sobre PILAS (Stacks)")
    print("=" * 50)
    print("1. Jugar con GRÁFICOS (ventana)")
    print("2. Jugar por CONSOLA")
    print("3. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        from hanoi_grafico import main_grafico
        main_grafico()
    elif opcion == "2":
        from hanoi_consola import main_consola
        main_consola()
    else:
        print("¡Hasta luego!")
>>>>>>> 65115aee89f17bd00f473bd088888e3abc55e984


if __name__ == "__main__":
    main()