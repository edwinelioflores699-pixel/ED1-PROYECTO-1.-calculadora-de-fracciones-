from __future__ import annotations

from models.fraction_model import FractionError, FractionModel
from views.main_view import MainView


class FractionController:
    """Controlador que conecta el modelo con la vista y maneja los eventos del usuario."""

    def __init__(self, model: FractionModel, view: MainView) -> None:
        """Inicializa el controlador con el modelo y la vista, y registra los handlers."""
        self.model = model
        self.view = view
        self.view.set_calculator_handler(self.handle_calculate)
        self.view.set_sorter_handler(self.handle_sort)

    def handle_calculate(self, left: str, right: str, operation: str) -> None:
        """Maneja el evento de cálculo: valida, procesa y muestra el resultado."""
        try:
            result = self.model.calculate(left, right, operation)
            self.view.show_calculator_result(f"Resultado: {result}", is_error=False)
            """Cuando Python pone {result} dentro de un string, llama automáticamente a __str__:"""
        except FractionError as exc:
            self.view.show_calculator_result(f"Error: {exc}", is_error=True)

    def handle_sort(self, raw_values: str, ascending: bool) -> None: 
        """Maneja el evento de ordenamiento: parsea, ordena y muestra el resultado."""
        try:
            values = [value for value in raw_values.split(",")]
            ordered = self.model.sort_fractions(values, ascending=ascending)
            ordered_text = ", ".join(str(item) for item in ordered)
            self.view.show_sort_result(f"Ordenadas: {ordered_text}", is_error=False)

            if len(ordered) >= 2:
                comparison = ordered[0].compare(ordered[1])
                if comparison == 0:
                    relation = "="
                elif comparison < 0:
                    relation = "<"
                else:
                    relation = ">"
                self.view.show_comparison_hint(
                    f"Comparación de las dos primeras: {ordered[0]} {relation} {ordered[1]}"
                )
            else:
                self.view.show_comparison_hint("Ingresa al menos dos fracciones para comparar.")
        except FractionError as exc:
            self.view.show_sort_result(f"Error: {exc}", is_error=True)
            self.view.show_comparison_hint("")