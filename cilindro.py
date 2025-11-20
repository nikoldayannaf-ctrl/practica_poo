from figuras_geometricas import Figuras_geometricas
from math import pi

class Cilindro(Figuras_geometricas):

    def __init__(self, nombre: str, radio: float, altura: float):
        super().__init__(nombre)
        self._radio = radio
        self._altura = altura

    # ---------- RADIO ----------
    @property
    def radio(self) -> float:
        return self._radio

    @radio.setter
    def radio(self, radio: float):
        self._radio = radio

    # ---------- ALTURA ----------
    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, altura: float):
        self._altura = altura

    # ---------- ÁREA TOTAL ----------
    def area(self) -> float:
        return 2 * pi * self._radio * (self._radio + self._altura)

    # ---------- VOLUMEN (extra opcional) ----------
    def volumen(self) -> float:
        return pi * self._radio**2 * self._altura