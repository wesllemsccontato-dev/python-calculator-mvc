

def calcular(n1, n2, operacao):
        if operacao == "+":
                
                return n1 + n2

                
        
        elif operacao == "-":
        
                return n1 - n2
        
        elif operacao == "*":

            return n1 * n2


        
        elif operacao == "/":

                if n2 == 0:
                
                        return None

                else:
                        return n1 / n2
                
                
        elif operacao == "%":

                return (n1*n2)/100
                