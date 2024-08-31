from abc import ABC, abstractmethod

class Articulo(ABC):
    def __init__(self, ID, titulo: str, autor: str, año_publicacion: int, categoria: str, estado: str, cantidad:int, palabras_clave: list[str], editorial:  str):
        self.ID = ID
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.categoria = categoria
        self.estado = estado
        self.cantidad = cantidad
        self.palabras_clave = palabras_clave
        self.editorial = editorial


    def __repr__(self):
        return f"{self.titulo} de {self.autor}, {self.año_publicacion}, {self.categoria}"

# Clases concretas para cada tipo de artículo
class Libro(Articulo):
    def __init__(self, ID, titulo: str, autor: str, año_publicacion: int, categoria: str, estado: str, cantidad: int, palabras_clave: str, editorial: str):
        super().__init__(ID, titulo, autor, año_publicacion, categoria, estado, cantidad, palabras_clave, editorial)


class Revista(Articulo):
    def __init__(self, ID, titulo: str, autor: str, año_publicacion: int, categoria: str, estado: str, cantidad: int, palabras_clave: str, editorial: str):
        super().__init__(ID, titulo, autor, año_publicacion, categoria, estado, cantidad, palabras_clave, editorial)


class DVD(Articulo):
    def __init__(self, ID, titulo: str, autor: str, año_publicacion: int, categoria: str, estado: str, cantidad: int, palabras_clave: str, productora: str):
        super().__init__(ID, titulo, autor, año_publicacion, categoria, estado, cantidad, palabras_clave)
        self.productora = productora


class CD(Articulo):
    def __init__(self, ID, titulo: str, autor: str, año_publicacion: int, categoria: str, estado: str, cantidad: int, palabras_clave: str, disquera: str):
        super().__init__(ID, titulo, autor, año_publicacion, categoria, estado, cantidad, palabras_clave)
        self.disquera = disquera



class Periodico(Articulo):
    def __init__(self, ID, titulo: str, autor: str, año_publicacion: int, categoria: str, estado: str, cantidad: int, palabras_clave: str, nombre: str):
        super().__init__(ID, titulo, autor, año_publicacion, categoria, estado, cantidad, palabras_clave)
        self.nombre = nombre
