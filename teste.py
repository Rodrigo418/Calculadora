from main import Calculadora

print(" Calculadora ")


n1 = float(input(" digite o primeiro valor: "))
n2 = float(input(" digite o segundo valor valor: "))
operacao = int(input("Escolha qual operação:(1- soma, 2- subtrair, 3- multiplicar, 4- dividir) "))

calculo = Calculadora(n1,n2)

if operacao == 1:
    resultado = calculo.soma()
    print(resultado)
elif operacao == 2:
    resultado = calculo.subtrair()
    print(resultado)
elif operacao == 3:
    resultado = calculo.multiplicar()
    print(resultado)
elif operacao == 4:
    resultado = calculo.dividir()
    print(resultado)
else:
    print("Por favor, digite o valor pedido ")