from formulario import Formulario
from correo import Correo
from catalogo import catalogos

class Prestamo:
  monto_fijo = 5000
  def __init__(self):
    self.formulario = Formulario()
    self.correo = Correo()

  def realizar_prestamo(self, usuario, titulo, ejemplar, fecha_inicio, fecha_devolucion):
    articulo = catalogos.buscar_articulo(titulo)
    if articulo is not None:
      if articulo.cantidad > 0:
        self.formulario.mostrar_formulario(usuario.identificacion, usuario.nombre_completo, titulo, ejemplar, fecha_inicio, fecha_devolucion)

  def realizar_devolucion(self):
    self.formulario.actualizar_estado()

  def aplicar_multa(self, fecha_actual):
    fecha_devolucion = self.formulario.formularios[self.formulario.ID][6]
    if fecha_actual > fecha_devolucion:
      dias_de_atraso = (fecha_actual - fecha_devolucion).days
      multa = dias_de_atraso * Prestamo.monto_fijo
      return multa
    else:
      return 0

  def notificar_prestamo(self, usuario, fecha_actual):
    fecha_devolucion = self.formulario.formularios[self.formulario.ID][6]
    if fecha_actual < fecha_devolucion:
      dias_restanes = (fecha_devolucion - fecha_actual).days
      return self.correo.enviar_correo(usuario.correo, "Aviso de días resantes de prestamo", f"Faltan {dias_restanes}, para la entrega del articulo")
    else:
      return False


  def obtener_formulario(self):
    return self.formulario.formularios[self.formulario.ID]