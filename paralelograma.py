from figuras_geometricas import Figuras_geometricas

class Paralelograma(Figuras_geometricas):

    def __init__(self, nombre: str, base: float, altura: float):
        super().__init__(nombre)
        self._base = base
        self._altura = altura

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, base: float):
        self._base = base

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, altura: float):
        self._altura = altura

    def area(self) -> float:
        return self._base * self._altura