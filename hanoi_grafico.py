"""
Torres de Hanoi - Interfaz GRÁFICA con tkinter
================================================
Ventana con 3 torres dibujadas como rectángulos de colores y una
gráfica de barras simple que muestra el avance (discos por torre).

Usa SOLO la biblioteca estándar de Python (tkinter), sin dependencias
externas adicionales.

Cómo jugar:
- Selecciona la torre ORIGEN y la torre DESTINO con los menús desplegables.
- Pulsa "Mover disco" para realizar el movimiento.
- Pulsa "Resolver automáticamente" para ver la solución óptima animada.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Dict, List

from hanoi import TorresDeHanoi

# Colores para los discos (más grande = abajo con índices altos y más anchos).
COLORES_DISCOS: List[str] = [
    "#FF6B6B",  # rojo
    "#4ECDC4",  # turquesa
    "#45B7D1",  # azul
    "#96CEB4",  # verde menta
    "#FFEAA7",  # amarillo
    "#DDA0DD",  # lavanda
    "#98D8C8",  # verde agua
    "#F0B429",  # dorado
]

COLOR_FONDO = "#2C3E50"
COLOR_TORRE = "#ECF0F1"
COLOR_BASE = "#95A5A6"
COLOR_TEXTO = "#FFFFFF"
COLOR_AUX = "#34495E"


class VentanaHanoi:
    """Ventana principal del juego con gráficas simples."""

    def __init__(self, root: tk.Tk, num_discos: int = 4) -> None:
        self.root = root
        self.juego = TorresDeHanoi(num_discos)
        self.num_discos = num_discos

        # Coordenadas de las torres en el canvas (centro X de cada una).
        self.canvas_ancho = 760
        self.canvas_alto = 380
        self.torre_x: Dict[str, int] = {"A": 150, "B": 380, "C": 610}
        self.base_y = 330
        self.disco_alto = 28
        self.disco_max_ancho = 150
        self.disco_min_ancho = 50

        # Gráfica de barras
        self.grafica_ancho = 760
        self.grafica_alto = 150
        self.barra_max_alto = 90
        self.grafica_base_y = 130

        self._crear_widgets()
        self._dibujar_todo()

    # --- Construcción de la interfaz --------------------------------------

    def _crear_widgets(self) -> None:
        self.root.title(f"Torres de Hanoi — {self.num_discos} discos (PILAS/Stacks)")
        self.root.configure(bg=COLOR_FONDO)
        self.root.resizable(False, False)

        # --- Canvas de las torres ---
        self.canvas_torres = tk.Canvas(
            self.root, width=self.canvas_ancho, height=self.canvas_alto,
            bg=COLOR_FONDO, highlightthickness=0
        )
        self.canvas_torres.pack(pady=(10, 5))

        # --- Canvas de la gráfica de barras ---
        self.canvas_grafica = tk.Canvas(
            self.root, width=self.grafica_ancho, height=self.grafica_alto,
            bg=COLOR_AUX, highlightthickness=0
        )
        self.canvas_grafica.pack(pady=5)

        # --- Panel de controles ---
        panel = tk.Frame(self.root, bg=COLOR_FONDO)
        panel.pack(pady=8)

        tk.Label(panel, text="Origen:", bg=COLOR_FONDO, fg=COLOR_TEXTO,
                 font=("Segoe UI", 11)).grid(row=0, column=0, padx=5)
        self.origen_var = tk.StringVar(value="A")
        self.menu_origen = ttk.Combobox(
            panel, textvariable=self.origen_var, values=["A", "B", "C"],
            state="readonly", width=3
        )
        self.menu_origen.grid(row=0, column=1, padx=5)

        tk.Label(panel, text="Destino:", bg=COLOR_FONDO, fg=COLOR_TEXTO,
                 font=("Segoe UI", 11)).grid(row=0, column=2, padx=5)
        self.destino_var = tk.StringVar(value="C")
        self.menu_destino = ttk.Combobox(
            panel, textvariable=self.destino_var, values=["A", "B", "C"],
            state="readonly", width=3
        )
        self.menu_destino.grid(row=0, column=3, padx=5)

        self.boton_mover = tk.Button(
            panel, text="⬇ Mover disco", command=self._mover_manual,
            bg="#27AE60", fg="white", font=("Segoe UI", 11, "bold"),
            padx=15, pady=5, cursor="hand2"
        )
        self.boton_mover.grid(row=0, column=4, padx=15)

        self.boton_resolver = tk.Button(
            panel, text="▶ Resolver automáticamente", command=self._resolver_auto,
            bg="#2980B9", fg="white", font=("Segoe UI", 11, "bold"),
            padx=15, pady=5, cursor="hand2"
        )
        self.boton_resolver.grid(row=0, column=5, padx=5)

        self.boton_reiniciar = tk.Button(
            panel, text="↺ Reiniciar", command=self._reiniciar,
            bg="#E67E22", fg="white", font=("Segoe UI", 11, "bold"),
            padx=15, pady=5, cursor="hand2"
        )
        self.boton_reiniciar.grid(row=0, column=6, padx=5)

        # --- Etiquetas de estado ---
        self.lbl_mensaje = tk.Label(
            self.root, text="Movimientos: 0  |  Óptimo: 1",
            bg=COLOR_FONDO, fg=COLOR_TEXTO, font=("Segoe UI", 10)
        )
        self.lbl_mensaje.pack(pady=(0, 10))

    # --- Dibujo ------------------------------------------------------------

    def _dibujar_todo(self) -> None:
        self._dibujar_torres()
        self._dibujar_grafica()
        self._actualizar_etiquetas()

    def _dibujar_torres(self) -> None:
        """Dibuja las 3 torres con sus discos actuales."""
        self.canvas_torres.delete("all")
        estado = self.juego.estado_torres()

        for nombre in ("A", "B", "C"):
            x = self.torre_x[nombre]
            # Poste vertical
            self.canvas_torres.create_rectangle(
                x - 8, self.base_y - 220, x + 8, self.base_y,
                fill=COLOR_TORRE, outline=""
            )
            # Base horizontal
            self.canvas_torres.create_rectangle(
                x - 100, self.base_y, x + 100, self.base_y + 15,
                fill=COLOR_BASE, outline=""
            )
            # Etiqueta
            self.canvas_torres.create_text(
                x, self.base_y + 35, text=nombre, fill=COLOR_TEXTO,
                font=("Segoe UI", 14, "bold")
            )
            # Discos (desde la base hacia la cima)
            discos = estado[nombre]
            for i, tam_disco in enumerate(discos):
                y = self.base_y - self.disco_alto * (i + 1) - 2
                ancho = self.disco_min_ancho + (
                    (tam_disco - 1) * (self.disco_max_ancho - self.disco_min_ancho)
                    / max(self.num_discos - 1, 1)
                )
                color = COLORES_DISCOS[(tam_disco - 1) % len(COLORES_DISCOS)]
                self.canvas_torres.create_rectangle(
                    x - ancho / 2, y, x + ancho / 2, y + self.disco_alto,
                    fill=color, outline="black", width=1
                )

    def _dibujar_grafica(self) -> None:
        """
        Gráfica de barras simple: altura de cada barra = número de discos
        en esa torre. La barra objetivo (C) se resalta en verde.
        """
        self.canvas_grafica.delete("all")
        estado = self.juego.estado_torres()
        colores_barra = {"A": "#45B7D1", "B": "#FF6B6B", "C": "#2ECC71"}
        barra_ancho = 100
        espacio = 80
        x_inicio = 150

        # Título
        self.canvas_grafica.create_text(
            self.grafica_ancho / 2, 20, text="Gráfica de avance — discos por torre",
            fill=COLOR_TEXTO, font=("Segoe UI", 11, "bold")
        )

        # Eje horizontal
        self.canvas_grafica.create_line(
            x_inicio - 40, self.grafica_base_y + 5,
            x_inicio + 2 * (espacio + barra_ancho) + 40, self.grafica_base_y + 5,
            fill=COLOR_TEXTO, width=2
        )

        for i, nombre in enumerate(("A", "B", "C")):
            x = x_inicio + i * (espacio + barra_ancho)
            cantidad = len(estado[nombre])
            alto_barra = self.barra_max_alto * cantidad / max(self.num_discos, 1)

            # Barra
            self.canvas_grafica.create_rectangle(
                x, self.grafica_base_y - alto_barra,
                x + barra_ancho, self.grafica_base_y,
                fill=colores_barra[nombre], outline="white", width=1
            )
            # Número encima de la barra
            self.canvas_grafica.create_text(
                x + barra_ancho / 2, self.grafica_base_y - alto_barra - 15,
                text=str(cantidad), fill=COLOR_TEXTO,
                font=("Segoe UI", 12, "bold")
            )
            # Etiqueta debajo
            self.canvas_grafica.create_text(
                x + barra_ancho / 2, self.grafica_base_y + 25,
                text=f"Torre {nombre}", fill=COLOR_TEXTO,
                font=("Segoe UI", 11)
            )

    def _actualizar_etiquetas(self) -> None:
        """Actualiza el contador de movimientos y el estado."""
        estado = self.juego.estado_torres()
        texto = (
            f"Movimientos: {self.juego.movimientos}  |  "
            f"Óptimo: {self.juego.movimientos_optimos()}  |  "
            f"Discos en C: {len(estado['C'])}/{self.num_discos}"
        )
        self.lbl_mensaje.config(text=texto)

    # --- Acciones -----------------------------------------------------------

    def _mover_manual(self) -> None:
        origen = self.origen_var.get()
        destino = self.destino_var.get()
        exito, mensaje = self.juego.mover(origen, destino)
        if exito:
            self._dibujar_todo()
            if self.juego.ganado:
                messagebox.showinfo(
                    "¡Victoria! 🎉",
                    f"¡Resolviste las Torres de Hanoi!\n"
                    f"Movimientos usados: {self.juego.movimientos}\n"
                    f"Movimientos óptimos: {self.juego.movimientos_optimos()}\n"
                    + ("⭐ ¡Solución ÓPTIMA!" if self.juego.movimientos
                       == self.juego.movimientos_optimos() else "")
                )
        else:
            messagebox.showwarning("Movimiento inválido", f"✗ {mensaje}")

    def _reiniciar(self) -> None:
        self.juego = TorresDeHanoi(self.num_discos)
        self._dibujar_todo()

    def _resolver_auto(self) -> None:
        """Anima la solución óptima paso a paso con un temporizador."""
        if self.juego.ganado:
            messagebox.showinfo("Juego ganado", "Ya está resuelto. Pulsa Reiniciar.")
            return

        movimientos = self.juego.resolver()
        self._deshabilitar_botones(True)

        def paso(indice: int) -> None:
            if indice >= len(movimientos):
                self._deshabilitar_botones(False)
                messagebox.showinfo(
                    "¡Victoria! 🎉",
                    f"Solución óptima completada:\n"
                    f"{len(movimientos)} movimientos.\n"
                    f"Los discos se movieron de A a C usando las pilas "
                    f"con la regla LIFO."
                )
                return
            origen, destino = movimientos[indice].split(">")
            self.juego.mover(origen, destino)
            self._dibujar_todo()
            self.root.after(350, paso, indice + 1)

        self.root.after(350, paso, 0)

    def _deshabilitar_botones(self, deshabilitar: bool) -> None:
        estado = "disabled" if deshabilitar else "normal"
        self.boton_mover.config(state=estado)
        self.boton_resolver.config(state=estado)
        self.menu_origen.config(state=estado)
        self.menu_destino.config(state=estado)


def main_grafico() -> None:
    """Lanza la ventana gráfica. Pide el número de discos primero."""
    import tkinter.simpledialog as simpledialog

    root = tk.Tk()
    root.withdraw()  # oculta la ventana vacía mientras preguntamos

    n = simpledialog.askinteger(
        "Torres de Hanoi",
        "¿Cuántos discos quieres? (1-8):",
        minvalue=1, maxvalue=8, parent=root
    )
    if n is None:
        root.destroy()
        return

    root.deiconify()
    VentanaHanoi(root, num_discos=n)
    root.mainloop()