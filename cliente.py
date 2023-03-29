class Cliente:
  def __init__(self, nombre, apellido, edad, ci, entrada, id_entrada, costo, acceso, monto, ronda):
    self.nombre = nombre
    self.apellido = apellido
    self.edad= edad
    self.ci = ci
    self.entrada=entrada
    self.id_entrada=id_entrada
    self.costo=costo
    self.acceso= acceso
    self.monto= monto
    self.ronda=ronda
  
  
  def mostrar_cliente(self):
    print (f"{self.nombre}  {self.apellido}\nCI: {self.ci}\n Entrada: {self.entrada}")