from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from typing import Iterable


class FractionError(ValueError):
    """Error de validación u operación con fracciones."""


@dataclass(frozen=True)
class Rational:
    """Representa una fracción racional irreducible con numerador y denominador."""
    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        """Normaliza la fracción: denominador positivo, irreducible y sin denominador cero."""
        if self.denominator == 0:
            raise FractionError("El denominador no puede ser cero.")

        num = self.numerator
        den = self.denominator

        if den < 0:
            num = -num
            den = -den

        divisor = gcd(abs(num), den)
        num //= divisor
        den //= divisor

        object.__setattr__(self, "numerator", num)
        object.__setattr__(self, "denominator", den)

    @classmethod
    #convertimos de texto a racional.
    def parse(cls, text: str) -> "Rational":
        """Convierte un string (ej: '1/2' o '3') en un objeto Rational."""
        raw = text.strip()
        if not raw:
            raise FractionError("Debes ingresar una fracción.")

        if "/" in raw:
            parts = raw.split("/")
            if len(parts) != 2:
                raise FractionError(
                    f"Formato inválido: '{text}'. Usa numerador/denominador."
                )

            left = parts[0].strip()
            right = parts[1].strip()
            if not left or not right:
                raise FractionError(f"Formato inválido: '{text}'.")

            try:
                num = int(left)
                den = int(right)
            except ValueError as exc:
                raise FractionError(f"Formato inválido: '{text}'.") from exc
            return cls(num, den)

        try:
            num = int(raw)
        except ValueError as exc:
            raise FractionError(
                f"Formato inválido: '{text}'. Usa entero o numerador/denominador."
            ) from exc
        return cls(num, 1)

    def add(self, other: "Rational") -> "Rational":
        """Suma dos fracciones y retorna una nueva fracción irreducible."""
        return Rational(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def sub(self, other: "Rational") -> "Rational":
        """Resta dos fracciones y retorna una nueva fracción irreducible."""
        return Rational(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def mul(self, other: "Rational") -> "Rational":
        """Multiplica dos fracciones y retorna una nueva fracción irreducible."""
        return Rational(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )

    def div(self, other: "Rational") -> "Rational":
        """Divide dos fracciones y retorna una nueva fracción irreducible."""
        if other.numerator == 0:
            raise FractionError("No se puede dividir entre cero.")
        return Rational(
            self.numerator * other.denominator,
            self.denominator * other.numerator,
        )

    def compare(self, other: "Rational") -> int:
        """Compara dos fracciones: retorna -1 (menor), 0 (igual) o 1 (mayor)."""
        left = self.numerator * other.denominator
        right = other.numerator * self.denominator
        if left < right:
            return -1
        if left > right:
            return 1
        return 0

    def __lt__(self, other: "Rational") -> bool:
        """Define el operador < usando compare() para ordenamiento."""
        return self.compare(other) < 0

    def __str__(self) -> str:
        """Retorna la fracción como string."""
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"


class FractionModel:
    """Lógica donde identificamos las operaciones, comparación y ordenamiento."""

    def calculate(self, left_text: str, right_text: str, operation: str) -> Rational:
        """Calcula una operación (+, -, *, /) entre dos fracciones ."""
        left = Rational.parse(left_text)
        right = Rational.parse(right_text)
        """aqui seleccionamos cual era la operacion indicada y la calculamos"""

        if operation == "+":
            return left.add(right)
        if operation == "-":
            return left.sub(right)
        if operation == "*":
            return left.mul(right)
        if operation == "/":
            return left.div(right)
        raise FractionError(f"Operación no soportada: {operation}")

    def compare(self, left_text: str, right_text: str) -> int:
        """Compara dos fracciones dadas como strings y retorna -1, 0 o 1."""
        left = Rational.parse(left_text)
        right = Rational.parse(right_text)
        return left.compare(right)

    def sort_fractions(self, values: Iterable[str], ascending: bool = True) -> list[Rational]:
        """Convierte una lista de strings a Rational y los ordena asc/desc según __lt__."""
        rationals: list[Rational] = []
        for value in values:
            cleaned = value.strip()
            if cleaned:
                rationals.append(Rational.parse(cleaned))

        if not rationals:
            raise FractionError("Debes ingresar al menos una fracción.")

        return sorted(rationals, reverse=not ascending)  # reverse=False → ascendente