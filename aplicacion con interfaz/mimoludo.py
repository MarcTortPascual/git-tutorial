import math
from random import randint

def imprimir(men):
    print(men)
def iguala(num1,num2):
    if num1==num2:
        return True
    else:
        return False
def diferente_a(num1,num2):
    if num1==num2:
        
        return False
    else:
        return True  
        
def major_que(numgrande,numpequeño):
        if numgrande>numpequeño:
            return True
        else:
            return False
def menor_que(numgrande,numpequeño):
        if numgrande<numpequeño:
            return True
        else:
            return False
def es_par(num1):
    if num1%2==0:
        return True
    else:
        return False
def es_impar(num2):
    if num2%2!=0:
        return True
    else:
        return False
    
def operar_basico (operacion,num1,num2):
    if operacion=="suma":
        return(num1+num2)
    elif operacion=="resta":
        return(num1-num2)
    elif operacion=="multiplicacion":
        return(num1*num2)
    elif operacion=="division":
        return(num1/num2)
    elif operacion=="potencia":
        return math.pow(num1,num2)
    if type(operacion)==int:
        raise TypeError ("solo se permiten las siguientes opciones:suma,resta,mulktiplicacion ,division i potencia")
    else:
        raise NameError("valor de la operacion incorecto")
def operaciones_complejas(operacion,num):
    if operacion=="raiz_quadrada":
        return math.sqrt(num)
    if type(operacion)==int:
        raise TypeError ("solo se permiten las sqiguientes opciones:suma,resta,mulktiplicacion ,division i potencia")
    else:
        raise NameError("valor de la operacion incorecto")
        
def generar_integer_aleatorio(minimo,maximo):

    return (randint(minimo,maximo))








    

