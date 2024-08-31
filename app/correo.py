class Correo:
  def enviar_correo(self, destinatario, concepto, mensaje):
    return f"Enviando correo a {destinatario} con concepto {concepto}: {mensaje}"

  def validar_correo(self, destinatario):
    return f"Validando correo a {destinatario}..."