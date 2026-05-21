from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import Callable


class MainView(tk.Tk):
    """Vista principal de la aplicación con pestañas de calculadora y ordenador de fracciones."""

    def __init__(self) -> None:
        """Inicializa la ventana principal, configura estilos y construye la interfaz."""
        super().__init__()
        self.title("Proyectos con Fracciones - MVC")
        self.geometry("860x520")
        self.minsize(820, 480)
        self.configure(bg="#f4f6fb")

        self._calculator_handler: Callable[[str, str, str], None] | None = None
        self._sorter_handler: Callable[[str, bool], None] | None = None

        self._configure_styles()
        self._build_ui()

    def _configure_styles(self) -> None:
        """Configura los estilos visuales de todos los widgets (colores, fuentes, bordes)."""
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Root.TFrame", background="#f4f6fb")
        style.configure(
            "Card.TFrame",
            background="#ffffff",
            relief="solid",
            borderwidth=1
        )

        style.configure(
            "Title.TLabel",
            background="#f4f6fb",
            foreground="#1d2433",
            font=("Segoe UI", 18, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            background="#f4f6fb",
            foreground="#4d5875",
            font=("Segoe UI", 10),
        )
        style.configure(
            "CardTitle.TLabel",
            background="#ffffff",
            foreground="#293247",
            font=("Segoe UI", 12, "bold"),
        )
        style.configure(
            "CardText.TLabel",
            background="#ffffff",
            foreground="#2f3a52",
            font=("Segoe UI", 10),
        )
        style.configure(
            "Status.TLabel",
            background="#eef1f8",
            foreground="#35405a",
            font=("Segoe UI", 9),
            padding=(8, 6),
        )

        style.configure(
            "Primary.TButton",
            background="#4f46e5",
            foreground="#ffffff",
            padding=(12, 6),
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
        )
        style.map(
            "Primary.TButton",
            background=[
                ("active", "#4338ca"),
                ("pressed", "#3730a3")
            ],
            foreground=[
                ("disabled", "#cad0ff"),
                ("!disabled", "#ffffff")
            ],
        )
        style.configure(
            "Secondary.TButton",
            background="#e6eaf5",
            foreground="#22304e",
            padding=(10, 6),
            font=("Segoe UI", 10),
            borderwidth=0,
        )
        style.map(
            "Secondary.TButton",
            background=[
                ("active", "#d8e0f2"),
                ("pressed", "#7b87a5")
            ],
        )

    def _build_ui(self) -> None:
        """Construye la estructura principal: contenedor, títulos, pestañas y barra de estado."""
        container = ttk.Frame(self, style="Root.TFrame", padding=16)
        container.pack(fill="both", expand=True)
        container.columnconfigure(0, weight=1)
        container.rowconfigure(2, weight=1)

        title = ttk.Label(
            container,
            text="Fracciones Pro",
            style="Title.TLabel",
        )
        title.grid(row=0, column=0, sticky="w")

        subtitle = ttk.Label(
            container,
            text="Calculadora y comparador de fracciones con arquitectura MVC",
            style="Subtitle.TLabel",
        )
        subtitle.grid(row=1, column=0, sticky="w", pady=(2, 12))

        notebook = ttk.Notebook(container)
        notebook.grid(row=2, column=0, sticky="nsew")

        self._build_calculator_tab(notebook)
        self._build_sorter_tab(notebook)

        self.status_var = tk.StringVar(value="Listo para operar con fracciones.")
        status_bar = ttk.Label(
            container,
            textvariable=self.status_var,
            style="Status.TLabel"
        )
        status_bar.grid(row=3, column=0, sticky="ew", pady=(12, 0))

    def _build_calculator_tab(self, notebook: ttk.Notebook) -> None:
        """Construye la pestaña de calculadora con campos para dos fracciones y operación."""
        frame = ttk.Frame(notebook, style="Root.TFrame", padding=14)
        frame.columnconfigure(0, weight=1)
        notebook.add(frame, text="Calculadora")

        card = ttk.Frame(frame, style="Card.TFrame", padding=16)
        card.grid(row=0, column=0, sticky="nsew")
        card.columnconfigure(1, weight=1)

        ttk.Label(
            card,
            text="Calculadora de Fracciones",
            style="CardTitle.TLabel"
        ).grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 8))

        ttk.Label(
            card,
            text="Ingresa dos fracciones y selecciona la operación.",
            style="CardText.TLabel",
        ).grid(row=1, column=0, columnspan=3, sticky="w", pady=(0, 12))

        ttk.Label(
            card,
            text="Fracción 1 (ej: 1/2):",
            style="CardText.TLabel"
        ).grid(row=2, column=0, sticky="w")

        self.frac1_entry = ttk.Entry(card, width=28)
        self.frac1_entry.grid(row=2, column=1, padx=8, pady=6, sticky="ew")

        ttk.Label(
            card,
            text="Operación:",
            style="CardText.TLabel"
        ).grid(row=3, column=0, sticky="w")

        self.operation_var = tk.StringVar(value="+")
        operation_box = ttk.Combobox(
            card,
            textvariable=self.operation_var,
            values=["+", "-", "*", "/"],
            width=6,
            state="readonly",
        )
        operation_box.grid(row=3, column=1, padx=8, pady=6, sticky="w")

        ttk.Label(
            card,
            text="Fracción 2 (ej: 3/4):",
            style="CardText.TLabel"
        ).grid(row=4, column=0, sticky="w")

        self.frac2_entry = ttk.Entry(card, width=28)
        self.frac2_entry.grid(row=4, column=1, padx=8, pady=6, sticky="ew")

        calculate_btn = ttk.Button(
            card,
            text="calcular",
            style="Primary.TButton",
            command=self._on_calculate_clicked,
        )
        calculate_btn.grid(row=5, column=0, pady=(14, 6), sticky="w")
        # Botón para limpiar los campos de la calculadora
        clear_btn = ttk.Button(
            card,
            text="Limpiar",
            style="Secondary.TButton",
            command=self._clear_calculator_fields,
        )
        clear_btn.grid(row=5, column=1, pady=(14, 6), sticky="w")

        self.calc_result_var = tk.StringVar(value="Resultado: ")
        self.calc_result_label = ttk.Label(
            card,
            textvariable=self.calc_result_var,
            font=("Segoe UI", 10, "bold"),
            background="#ffffff",
            foreground="#1c7c3b",
        )
        self.calc_result_label.grid(
            row=6,
            column=0,
            columnspan=3,
            sticky="w",
            pady=(8, 0)
        )

        self.bind("<Return>", lambda _: self._on_calculate_clicked())

    def _build_sorter_tab(self, notebook: ttk.Notebook) -> None:
        """Construye la pestaña de ordenador con campo para lista de fracciones y radio buttons."""
        frame = ttk.Frame(notebook, style="Root.TFrame", padding=14)
        frame.columnconfigure(0, weight=1)
        notebook.add(frame, text="Comparador / Ordenador")

        card = ttk.Frame(frame, style="Card.TFrame", padding=16)
        card.grid(row=0, column=0, sticky="nsew")
        card.columnconfigure(0, weight=1)

        ttk.Label(
            card,
            text="Comparador y Ordenador",
            style="CardTitle.TLabel"
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 8))

        ttk.Label(
            card,
            text="Ingresa varias fracciones separadas por coma para ordenarlas.",
            style="CardText.TLabel",
        ).grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 12))

        ttk.Label(
            card,
            text="Fracciones (ej: 1/2, 3/4, -2/5):",
            style="CardText.TLabel",
        ).grid(row=2, column=0, columnspan=2, sticky="w")

        self.list_entry = ttk.Entry(card, width=62)
        self.list_entry.grid(row=3, column=0, columnspan=2, pady=8, sticky="ew")

        self.sort_order_var = tk.StringVar(value="asc")
        ttk.Radiobutton(
            card,
            text="Menor a mayor",
            variable=self.sort_order_var,
            value="asc"
        ).grid(row=4, column=0, sticky="w")

        ttk.Radiobutton(
            card,
            text="Mayor a menor",
            variable=self.sort_order_var,
            value="desc"
        ).grid(row=4, column=1, sticky="w")

        sort_btn = ttk.Button(
            card,
            text="Ordenar / Comparar",
            style="Primary.TButton",
            command=self._on_sort_clicked,
        )
        sort_btn.grid(row=5, column=0, pady=(14, 6), sticky="w")

        clear_btn = ttk.Button(
            card,
            text="Limpiar",
            style="Secondary.TButton",
            command=self._clear_sort_fields,
        )
        clear_btn.grid(row=5, column=1, pady=(14, 6), sticky="w")

        self.sort_result_var = tk.StringVar(value="Ordenadas: ")
        self.sort_result_label = ttk.Label(
            card,
            textvariable=self.sort_result_var,
            font=("Segoe UI", 10, "bold"),
            background="#ffffff",
            foreground="#1c7c3b",
        )
        self.sort_result_label.grid(
            row=6,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(8, 0)
        )

        self.comparison_var = tk.StringVar(value="")
        self.comparison_label = ttk.Label(
            card,
            textvariable=self.comparison_var,
            style="CardText.TLabel",
        )
        self.comparison_label.grid(
            row=7,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(8, 0)
        )

    def set_calculator_handler(self, handler: Callable[[str, str, str], None]) -> None:
        """Registra la función callback que manejará el cálculo de fracciones."""
        self._calculator_handler = handler

    def set_sorter_handler(self, handler: Callable[[str, bool], None]) -> None:
        """Registra la función callback que manejará el ordenamiento de fracciones."""
        self._sorter_handler = handler

    def _on_calculate_clicked(self) -> None:
        """Evento: obtiene los valores de los campos y llama al handler de calculadora."""
        if self._calculator_handler is None:
            return
        self._calculator_handler(   #la operacion es llamada por el controlador.
            self.frac1_entry.get(), #la primera fraccion.
            self.frac2_entry.get(),
            self.operation_var.get(),
        )

    def _on_sort_clicked(self) -> None:
        """Evento: obtiene la lista de fracciones y el orden, luego llama al handler de ordenamiento."""
        if self._sorter_handler is None:
            return
        ascending = self.sort_order_var.get() == "asc"
        self._sorter_handler(self.list_entry.get(), ascending)

    def show_calculator_result(self, message: str, is_error: bool = False) -> None:
        """Muestra el resultado de la calculadora y actualiza la barra de estado."""
        self.calc_result_var.set(message)
        self.calc_result_label.configure(foreground="red" if is_error else "darkgreen")
        self.status_var.set("Resultado actualizado en calculadora.")

    def show_sort_result(self, message: str, is_error: bool = False) -> None:
        """Muestra el resultado del ordenamiento y actualiza la barra de estado."""
        self.sort_result_var.set(message)
        self.sort_result_label.configure(foreground="red" if is_error else "darkgreen")
        self.status_var.set("Resultado actualizado en comparador/ordenador.")

    def show_comparison_hint(self, message: str) -> None:
        """Muestra una pista de comparación entre fracciones (mayor/menor/igual)."""
        self.comparison_var.set(message)

    def _clear_calculator_fields(self) -> None:
        """Limpia los campos de entrada y el resultado de la calculadora."""
        self.frac1_entry.delete(0, tk.END)
        self.frac2_entry.delete(0, tk.END)
        self.operation_var.set("+")
        self.calc_result_var.set("Resultado: ")
        self.calc_result_label.configure(foreground="darkgreen")
        self.status_var.set("Campos de calculadora limpiados.")

    def _clear_sort_fields(self) -> None:
        """Limpia el campo de entrada, el resultado y la comparación del ordenador."""
        self.list_entry.delete(0, tk.END)
        self.sort_order_var.set("asc")
        self.sort_result_var.set("Ordenadas: ")
        self.comparison_var.set("")
        self.sort_result_label.configure(foreground="darkgreen")
        self.status_var.set("Campos de comparador/ordenador limpiados.")