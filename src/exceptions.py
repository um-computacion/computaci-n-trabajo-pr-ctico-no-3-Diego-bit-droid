class NumeroDebeSerPositivo(Exception):
    def __init__(self, mensaje="El numero tiene que ser positivo"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)