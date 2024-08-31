from catalogo import catalogos

class Formulario:
  ID = 1
  def __init__(self):
    Formulario.ID += 1
    self.ID = Formulario.ID
    self.formularios = {}

  def mostrar_formulario(self, ID_user, usuario, titulo, ejemplar, fecha_inicio, fecha_devolucion, estado = "No devuelto"):
    print(f"ID del usuario: {ID_user}")
    print(f"Usuario: {usuario}")
    print(f"Título: {titulo}")
    print(f"Ejemplar: {ejemplar}")
    print(f"Fecha de inicio: {fecha_inicio}")
    print(f"Fecha de devolución: {fecha_devolucion}")
    print(f"Estado: {estado}")
    self.formularios[self.ID] = [ID_user, usuario, titulo, ejemplar, fecha_inicio, fecha_devolucion, estado]
    articulo = catalogos.buscar_articulo(titulo)
    if articulo is not None:
      articulo.estado = "Prestado"
      articulo.cantidad -= 1
    return self.formularios
  #actualizar el estado del prestamo y que ahora tenga estado "Devuelto"
  def actualizar_estado(self):
    if self.ID in self.formularios:
      self.formularios[self.ID][7] = "Devuelto"
      articulo = catalogos.buscar_articulo(self.formularios[self.ID][3])
      if articulo is not None:
        articulo.estado = "Disponible"
        articulo.cantidad += 1