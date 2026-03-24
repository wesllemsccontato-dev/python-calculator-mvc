
from src.calculadora.controller.operacoes import calcular

print("Calculadora1")
print("Digite o Primeiro Numero")
print("Depois Informe a Operação desejada entre + - * / %")
print("Depois Digite o segundo Numero")
print("Ao Final Digite C Para Limpar   \n")

def operaçoes(operacao):
        while True:
            
            
            if operacao in ("+","-","*","/"):
                return operacao
                
            
            else:
                
                operacao = input("Digite a Operação: ")
                
                
                
                if operacao not in ("+","-","*","/","%"):
                    print('Operação Invalida')
                    continue
                return operacao
            
            
def pedirnumero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Número inválido")
            

operacao = None
            
            
numero1 = pedirnumero("Primeiro Número: ")

while True:
    
    operacao = operaçoes(operacao)

    numero2 = pedirnumero("Segundo Número: ")

    while True:
        resultado = calcular(numero1, numero2, operacao)
        if resultado is None:
            print(resultado)
            break
        if operacao == "%":
            print(f"\n{numero1:} {operacao} {numero2} = {resultado}%")
                    
        else:
            print(f"\n{numero1:} {operacao} {numero2} = {resultado}")
            numero1 = resultado 
        cont = input()
                
        if cont == "":
            continue
        
        elif cont in ("-","+","*","/","%"):
            operacao = cont
        
        else:
            print("Error") 
    
            
    if cont == "c":
            break


