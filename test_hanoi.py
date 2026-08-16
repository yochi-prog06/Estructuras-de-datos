"""
Pruebas automáticas para el juego de Torres de Hanoi.
Verifica que la Pila y la lógica del juego funcionen correctamente.
"""

from hanoi import Pila, TorresDeHanoi


def test_pila() -> None:
    """Prueba las operaciones básicas de la Pila (LIFO)."""
    print("=== Prueba de la Pila ===")
    p = Pila()
    assert p.is_empty() is True
    assert p.size() == 0

    p.push(1)
    p.push(2)
    p.push(3)
    assert p.size() == 3
    assert p.peek() == 3  # El último en entrar es la cima

    assert p.pop() == 3   # Último en entrar, primero en salir
    assert p.pop() == 2
    assert p.pop() == 1
    assert p.is_empty() is True
    print("✓ Pila funciona correctamente (LIFO verificado).\n")


def test_juego_ganable() -> None:
    """Resuelve el juego con 3 discos y verifica la victoria."""
    print("=== Prueba del juego (3 discos) ===")
    juego = TorresDeHanoi(num_discos=3)
    assert juego.movimientos_optimos() == 7  # 2^3 - 1 = 7

    # Solución óptima para 3 discos: A -> C
    movimientos = [
        ("A", "C"),
        ("A", "B"),
        ("C", "B"),
        ("A", "C"),
        ("B", "A"),
        ("B", "C"),
        ("A", "C"),
    ]
    for origen, destino in movimientos:
        ok = juego.mover(origen, destino)
        assert ok, f"Movimiento {origen}->{destino} debió ser válido."

    assert juego.ganado is True, "El juego debió detectar la victoria."
    assert juego.movimientos == 7
    assert juego.torres["C"].size() == 3
    print("✓ Juego resuelto en 7 movimientos (óptimo). Victoria detectada.\n")


def test_movimiento_invalido() -> None:
    """Verifica que no se pueda poner un disco grande sobre uno pequeño."""
    print("=== Prueba de movimiento inválido ===")
    juego = TorresDeHanoi(num_discos=3)
    # Disco 1 (cima de A) -> C, válido
    assert juego.mover("A", "C") is True
    # Disco 2 (nueva cima de A) -> C, inválido (2 > 1)
    assert juego.mover("A", "C") is False
    # El movimiento inválido no debe contar
    assert juego.movimientos == 1
    print("✓ Movimiento inválido rechazado correctamente.\n")


def test_torre_vacia() -> None:
    """Verifica que no se pueda mover desde una torre vacía."""
    print("=== Prueba de torre vacía ===")
    juego = TorresDeHanoi(num_discos=3)
    assert juego.mover("B", "C") is False  # B está vacía
    assert juego.movimientos == 0
    print("✓ No se puede mover desde una torre vacía.\n")


def main() -> None:
    test_pila()
    test_juego_ganable()
    test_movimiento_invalido()
    test_torre_vacia()
    print("🎉 Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()