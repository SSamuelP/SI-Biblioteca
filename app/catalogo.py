from articulo import Articulo


class Catalogo:

    def __init__(self):
        self.articulos = []

    def agregar_articulo(self, articulo: Articulo):
        self.articulos.append(articulo)

    def elimminar_articulo(self, articulo: Articulo):
        self.articulos.remove(articulo)

    def buscar_articulo(self, titulo):
        for articulo in self.articulos:
            if articulo.titulo == titulo:
                return articulo
        return None

    def __repr__(self) -> str:
        return f"{self.articulos}"


catalogos = Catalogo()
