"""
Torres de Hanoi - Lógica del juego con PILAS (Stacks)
=====================================================

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

Arquitectura (refactorizada):
- Este módulo contiene SOLO la lógica del juego (sin imprimir en pantalla).
- hanoi_consola.py  -> interfaz de consola (ASCII).
- hanoi_grafico.py  -> interfaz gráfica con tkinter (gráficas simples).
"""

from typing import Dict, List, Optional, Tuple


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
    Lógica pura: no imprime ni dibuja; devuelve mensajes de texto
    para que cualquier interfaz (consola o gráfica) los muestre.

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
        self.torres: Dict[str, Pila] = {
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
        # (origen, destino, disco) del último movimiento válido.
        self.ultimo_movimiento: Optional[Tuple[str, str, int]] = None

    # --- Lógica del juego -------------------------------------------------

    def mover(self, origen: str, destino: str) -> Tuple[bool, str]:
        """
        Intenta mover el disco de la cima de `origen` a `destino`.

        Devuelve una tupla (éxito, mensaje):
        - éxito = True si el movimiento fue válido y se realizó.
        - mensaje describe el resultado (para que la UI lo muestre).
        """
        origen = origen.upper()
        destino = destino.upper()

        if origen not in self.torres or destino not in self.torres:
            return False, "Torres válidas: A, B o C."
        if origen == destino:
            return False, "Origen y destino son la misma torre."
        if self.torres[origen].is_empty():
            return False, f"La torre {origen} está vacía, no hay disco para mover."

        disco_origen = self.torres[origen].peek()

        # Regla: no poner un disco grande sobre uno más pequeño.
        if not self.torres[destino].is_empty():
            disco_destino = self.torres[destino].peek()
            if disco_origen > disco_destino:
                return False, (
                    f"Movimiento inválido: el disco {disco_origen} no puede "
                    f"ponerse sobre el disco {disco_destino} (más pequeño)."
                )

        # Movimiento válido: desapilar de origen y apilar en destino.
        disco = self.torres[origen].pop()
        self.torres[destino].push(disco)
        self.movimientos += 1
        self.ultimo_movimiento = (origen, destino, disco)

        self._verificar_victoria()
        return True, f"Movimiento {self.movimientos}: {origen} -> {destino} (disco {disco})"

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

    # --- Estado para la interfaz -----------------------------------------

    def estado_torres(self) -> Dict[str, List[int]]:
        """
        Devuelve los discos de cada torre desde la base hasta la cima.
        Ejemplo: {"A": [4, 3, 2, 1], "B": [], "C": []}
        Útil para que las interfaces dibujen las torres.
        """
        return {nombre: self.torres[nombre].to_list() for nombre in ("A", "B", "C")}

    # --- Solución automática (demostración educativa) --------------------

    def resolver(self, n: Optional[int] = None, origen: str = "A",
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


if __name__ == "__main__":
    main()