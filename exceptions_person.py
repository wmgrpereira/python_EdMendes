#https://www.youtube.com/watch?v=m08xaNwaFLc

def divide (n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print('Erro para registro de log:', erro)
        raise       # Relança a exceção, após o tratamento, dando sequencia para outro tratamento fora da função

try:
    print(divide(2,0))
except Exception as erro:
    print('Erro2:', erro)


#Outra forma mais específica:

def div(n1, n2):
    if n2 == 0:
        raise ValueError ('n2 não pode ser 0.')
    return n1 / n2

try:
    print(div(n1=2, n2=0))
except ValueError as erro:
    print('Você está tentando dividir por 0.')
    print('Log:', erro) #Inserirndo log num arquivo de texto