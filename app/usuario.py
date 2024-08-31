from correo import Correo


class Usuario:

    def __init__(self, identificacion: int, nombre_completo: str,
                 direccion: str, celular: str, correo: str,
                 fecha_nacimiento: str, ocupacion: str):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.celular = celular
        self.correo_electronico = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.ocupacion = ocupacion
        self.correo = Correo()

    def validar_usuario(self):
        return f"{self.validar_identificacion()} {self.validar_correo()}. {self.validar_celular()}"

    def validar_identificacion(self):
        if len(str(self.identificacion)) == 10:
            return "Identificación válida."
        else:
            return "Identificación inválida."

    def validar_correo(self):
        return self.correo.validar_correo(self.correo_electronico)

    def validar_celular(self):
        return f"Enviando mensaje de texto a {self.celular}"
