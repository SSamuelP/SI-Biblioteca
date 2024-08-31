class Sugerencia:

  def __init__(self):
    self.sugerencias = {}

  def agregar_sugerencia(self, usuario, mensaje):
    self.sugerencias[usuario] = mensaje

  def __repr__(self):
    return f"{self.sugerencias}"
