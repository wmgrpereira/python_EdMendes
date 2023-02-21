from unittest import TestCase, main
from numbers import Number #Essa classe engloba todos os números. Decimais, floats e inteiros.
from pdb import set_trace #cria um break point. Retorna um shell até o ponto especificado. Comando "l" lista. Comando "s" executa linha a linha.
                          # "p x" printa o valor de x. "dir()" mostra todos os "objetos" na seção. "h" imprime todos os comandos possíveis. "w" onde vc está.
                          # "ll" é long liste. "n" é next pra executar linha a linha.

pdb = False
def validade_cache(func, cache={}):
    # TODO: Criar closure
    def validate_apply_cache(self, x, y=None):
        if pdb:
            set_trace()
        chave = False  
        if y == None: 
            y = cache['value']      
            chave = True         
        if isinstance(x, Number) and isinstance(y, Number):
            if chave:
                cache['value'] = func(self, y, x)
            else:
                cache['value'] = func(self, x, y)
            return cache['value']
        else:
            raise Exception ('Insira somente números')
    return validate_apply_cache
  

class Calc:
    @validade_cache # Decorando a função
    def soma(self, x, y):
        return x + y
  
    @validade_cache # Decorando a função
    def sub(self, x, y):
        return x - y

    @validade_cache # Decorando a função
    def mul(self, x, y):
             return x * y

    @validade_cache # Decorando a função
    def div(self, x, y):
        return x / y # Divisão com '/' retorna float. Divisão com '//' retorna inteiro

    
class Testes_calculadora(TestCase):
    def setUp(self):
        self.calc = Calc()
    
    def teste_soma(self):
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
    
    def teste_sub_result_neg(self):
        self.assertEqual(self.calc.sub(3, 10),-7)
        self.assertEqual(self.calc.soma(3), -4)
    
    def teste_soma_result_pos_com_sub_cache(self):
        # global pdb
        # pdb = True
        self.assertEqual(self.calc.soma(1, 1), 2)
        self.assertEqual(self.calc.sub(3), -1)
    

if __name__ == '__main__': # Na execução do sistema, o local onde estamos é o __main__. Então atribuimos a variável __name__ o valor de __main__
    main()                 # Se estivermos no lucal onde a execução do sistema estiver sendo feita, ela vai chamar a função main() que importamos
                           # de unittest, que executa a função método por método