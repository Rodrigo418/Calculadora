class Calculadora:

  def __init__(self, numero1, numero2):
    self.numero1 = numero1
    self.numero2 = numero2
  
  def soma(self):
    resultado = self.numero1 + self.numero2
    return(resultado)

  def subtrair(self):
    resultado = self.numero1 - self.numero2
    return(resultado)

  def multiplicar(self):
    resultado = self.numero1 * self.numero2
    return(resultado)

  def dividir(self):
    resultado = self.numero1 / self.numero2
    return(resultado)
