from figuras_geometricas import Figuras_geometricas

class Pentagono(Figuras_geometricas):

    def __init__(self, nombre: str, lado: float, apotema: float):
        super().__init__(nombre)
        self._lado = lado
        self._apotema = apotema

    # ----- LADO -----
    @property
    def lado(self) -> float:
        return self._lado

    @lado.setter
    def lado(self, lado: float):
        self._lado = lado

    # ----- APOTEMA -----
    @property
    def apotema(self) -> float:
        return self._apotema

    @apotema.setter
    def apotema(self, apotema: float):
        self._apotema = apotema

    # ----- ÁREA -----
    def area(self) -> float:
        return (5 * self._lado * self._apotema) / 2
