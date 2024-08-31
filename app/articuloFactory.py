from articulo import Articulo, Libro, Revista, DVD, CD, Periodico


# ArticuloFactory para crear instancias de Articulo
class ArticuloFactory:

  @staticmethod
  def crear_articulo(tipo_articulo, ID, titulo, autor, año_publicacion,
                     categoria, estado, cantidad, palabras_clave,
                     editorial) -> Articulo:
    if tipo_articulo == "Libro":
      return Libro(ID, titulo, autor, año_publicacion, categoria, estado,
                   cantidad, palabras_clave, editorial)
    elif tipo_articulo == "Revista":
      return Revista(ID, titulo, autor, año_publicacion, categoria, estado,
                     cantidad, palabras_clave, editorial)
    elif tipo_articulo == "DVD":
      return DVD(ID, titulo, autor, año_publicacion, categoria, estado,
                 cantidad, palabras_clave, editorial)
    elif tipo_articulo == "CD":
      return CD(ID, titulo, autor, año_publicacion, categoria, estado,
                cantidad, palabras_clave, editorial)
    elif tipo_articulo == "Periodico":
      return Periodico(ID, titulo, autor, año_publicacion, categoria, estado,
                       cantidad, palabras_clave, editorial)
    else:
      raise ValueError("Tipo de artículo no soportado")
