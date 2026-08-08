"""
Tests para la lógica refactorizada de las Torres de Hanoi.
Ejecutar con: python -m unittest test_hanoi -v
"""

import unittest

from hanoi import Pila, TorresDeHanoi


class TestPila(unittest.TestCase):
    """Pruebas de la estructura Pila (Stack) LIFO."""

    def test_push_pop(self):
        pila = Pila()
        pila.push(1)
        pila.push(2)
        pila.push(3)
        self.assertEqual(pila.pop(), 3)  # LIFO: sale el último
        self.assertEqual(pila.pop(), 2)
        self.assertEqual(pila.pop(), 1)

    def test_peek_no_retira(self):
        pila = Pila()
        pila.push("A")
        self.assertEqual(pila.peek(), "A")
        self.assertEqual(pila.size(), 1)

    def test_empty_y_size(self):
        pila = Pila()
        self.assertTrue(pila.is_empty())
        self.assertEqual(pila.size(), 0)
        pila.push(10)
        self.assertFalse(pila.is_empty())
        self.assertEqual(pila.size(), 1)

    def test_pop_vacio_lanza_error(self):
        pila = Pila()
        with self.assertRaises(ValueError):
            pila.pop()

    def test_to_list(self):
        pila = Pila()
        for v in (3, 2, 1):
            pila.push(v)
        self.assertEqual(pila.to_list(), [3, 2, 1])


class TestTorresDeHanoi(unittest.TestCase):
    """Pruebas de la lógica del juego."""

    def test_estado_inicial(self):
        juego = TorresDeHanoi(4)
        self.assertEqual(juego.estado_torres()["A"], [4, 3, 2, 1])
        self.assertEqual(juego.estado_torres()["B"], [])
        self.assertEqual(juego.estado_torres()["C"], [])
        self.assertEqual(juego.movimientos, 0)
        self.assertFalse(juego.ganado)

    def test_mover_devuelve_tupla(self):
        """La refactorización: mover() devuelve (éxito, mensaje)."""
        juego = TorresDeHanoi(3)
        exito, mensaje = juego.mover("A", "C")
        self.assertTrue(exito)
        self.assertIn("Movimiento 1", mensaje)
        self.assertEqual(juego.movimientos, 1)

    def test_mover_invalido(self):
        juego = TorresDeHanoi(2)
        # Mover disco 2 (grande) sobre disco 1 (pequeño) es inválido
        juego.mover("A", "C")  # disco 1 -> C
        exito, mensaje = juego.mover("A", "C")  # disco 2 sobre disco 1
        self.assertFalse(exito)
        self.assertIn("inválido", mensaje)
        self.assertEqual(juego.movimientos, 1)  # no incrementó

    def test_resolver_devuelve_lista_sin_modificar(self):
        """La refactorización: resolver() devuelve la lista de pasos."""
        juego = TorresDeHanoi(3)
        movimientos = juego.resolver()
        self.assertEqual(len(movimientos), 7)  # 2^3 - 1
        # No ejecutó nada sobre el juego
        self.assertEqual(juego.movimientos, 0)
        self.assertEqual(juego.estado_torres()["A"], [3, 2, 1])

    def test_victoria_al_mover_todos_a_c(self):
        juego = TorresDeHanoi(3)
        for mov in juego.resolver():
            origen, destino = mov.split(">")
            exito, _ = juego.mover(origen, destino)
            self.assertTrue(exito)
        self.assertTrue(juego.ganado)
        self.assertEqual(juego.estado_torres()["C"], [3, 2, 1])
        self.assertEqual(juego.movimientos, 7)
        # Con 3 discos la solución óptima es exactamente 7
        self.assertEqual(juego.movimientos, juego.movimientos_optimos())

    def test_movimientos_optimos(self):
        self.assertEqual(TorresDeHanoi(1).movimientos_optimos(), 1)
        self.assertEqual(TorresDeHanoi(2).movimientos_optimos(), 3)
        self.assertEqual(TorresDeHanoi(3).movimientos_optimos(), 7)
        self.assertEqual(TorresDeHanoi(4).movimientos_optimos(), 15)

    def test_num_discos_invalido(self):
        with self.assertRaises(ValueError):
            TorresDeHanoi(0)


if __name__ == "__main__":
    unittest.main()