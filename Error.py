class Error:
  def __init__(self, tipo, mensaje, fila, columna):
    self.tipo = tipo
    self.mensaje = mensaje
    self.fila = fila
    self.columna = columna