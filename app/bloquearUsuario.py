class BloqueoUsuario:
  def __init__(self):
      self.usuarios_bloqueados = {}

  def bloquear_usuario(self, usuario):
      self.usuarios_bloqueados[usuario.identificacion] = True
      print(f"Usuario {usuario.nombre_completo} ha sido bloqueado.")

  def desbloquear_usuario(self, usuario):
      if usuario.identificacion in self.usuarios_bloqueados:
          del self.usuarios_bloqueados[usuario.identificacion]
          print(f"Usuario {usuario.nombre_completo} ha sido desbloqueado.")
      else:
          print(f"Usuario {usuario.nombre_completo} no estaba bloqueado.")

  def es_usuario_bloqueado(self, usuario) -> bool:
      return self.usuarios_bloqueados.get(usuario.identificacion, False)
