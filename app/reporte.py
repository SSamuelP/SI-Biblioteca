class Reporte:
  def generar_reporte_historial_usuario(self, usuario_id: int):
      print(f"Generando reporte del historial de préstamos para el usuario {usuario_id}...")

  def generar_reporte_articulos_mas_prestados(self):
      print("Generando reporte de artículos más prestados...")

  def generar_reporte_articulos_por_categoria(self, categoria: str):
      print(f"Generando reporte de artículos en la categoría: {categoria}...")

  def generar_reporte_articulos_por_año(self, año_publicacion: int):
      print(f"Generando reporte de artículos publicados en el año: {año_publicacion}...")
