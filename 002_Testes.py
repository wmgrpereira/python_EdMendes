from unittest import TestCase, main

class Calc:
    
    def __init__(self):
        self.cache = 0 #Estabelecendo o valor inicial
    
    def soma(self, x, y=None):
        if isinstance (x, int) and isinstance(y, int): # Varifica se x e y são inteiros (se são instâncias de classes de inteiros)
            self.cache = x + y
            return self.cache
        elif y is None:
            return x + self.cache
        else:
            raise Exception('insira somente números')          #raise: palavra reservadas para gerar excessão no código. Tratar erros
    
    def sub(self, x, y=None):
        if y is None:
            self.cache = x - self.cache
        else:
            self.cache = x - y
            return self.cache
    
    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x // y # Divisão com '/' retorna float. Divisão com '//' retorna inteiro
    
    def clear_cache (self):
        self.cache = 0
    
class Testes_calculadora(TestCase):
    def setUp(self):
        self.calc = Calc()
    
    def teste_soma(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.soma(2,2), 4)
    
    def teste_soma_neg(self):
        self.assertEqual(self.calc.soma(-2,-3), -5)
    
    # def teste_soma_float(self):
    #     self.assertEqual(self.calc.soma(2.0,1.0), 3.0)
        
    def teste_sub(self):
        self.assertEqual(self.calc.sub(2, 2), 0)
        
    def teste_sub_float(self):
        self.assertEqual(self.calc.sub(2.0, 2.0), 0)
    
    def teste_soma_string(self):
        with self.assertRaises(Exception): # assertRaises valida se provem do raise
                self.calc.soma('Eduardo', 'jaber')
    
    def teste_sub_string(self):
        with self.assertRaises(Exception): # assertRaises valida se provem do raise
                self.calc.sub('Eduardo', 'jaber')
    
    def teste_mul(self):
        self.assertEqual(self.calc.mul(3, 3), 9)

    def teste_mul_string(self):
        with self.assertRaises(Exception): # assertRaises valida se provem do raise
                self.calc.mul(3, 'Eduardo') # O python não trata multiplicação de int e string como erro. Mas nosso código precisa tratar como erro
    
    def teste_div(self):
        self.assertEqual(self.calc.div(3, 3), 1)
        
    def teste_div_string(self):
        with self.assertRaises(Exception): # assertRaises valida se provem do raise
                self.calc.div(3, 'Eduardo') # O python não trata divisao de int e string como erro. Mas nosso código precisa tratar como erro
    def teste_cache_soma(self):
        self.assertEqual(self.calc.soma(self.calc.soma(2,2)),8)
    
    def teste_cache_sub(self):
        self.assertEqual(self.calc.sub(self.calc.sub(10,5)),0)

if __name__ == '__main__': # Na execução do sistema, o local onde estamos é o __main__. Então atribuimos a variável __name__ o valor de __main__
    main()                 # Se estivermos no lucal onde a execução do sistema estiver sendo feita, ela vai chamar a função main() que importamos
                           # de unittest, que executa a função método por método