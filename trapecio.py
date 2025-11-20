from figuras_geometricas import Figuras_geometricas

class Trapecio(Figuras_geometricas):

    def __init__(self, nombre: str, base_mayor: float, base_menor: float, altura: float):
        super().__init__(nombre)
        self._base_mayor = base_mayor
        self._base_menor = base_menor
        self._altura = altura

    # ----- BASE MAYOR -----
    @property
    def base_mayor(self) -> float:
        return self._base_mayor

    @base_mayor.setter
    def base_mayor(self, base_mayor: float):
        self._base_mayor = base_mayor

    # ----- BASE MENOR -----
    @property
    def base_menor(self) -> float:
        return self._base_menor

    @base_menor.setter
    def base_menor(self, base_menor: float):
        self._base_menor = base_menor

    # ----- ALTURA -----
    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, altura: float):
        self._altura = altura

    # ----- ÁREA -----
    def area(self) -> float:
        return ((self._base_mayor + self._base_menor) * self._altura) / 2
