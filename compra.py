class Compra:
    def __init__(self, ci, monto):
        self.ci = ci
        self.monto= monto
    def mostrar_compra(self):
        print(f' Monto: {self.monto}')