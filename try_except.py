#https://www.youtube.com/watch?v=RHSxIKGCX7c
#try e except funcionam com if e else e são utilizados para tratamento de erro.
#ele tenta executar o que contém no try e se algo der erro ele cai no except
try:
    a = 0
    # try: 
    #     a=1/0
    # except:
    print('Erro')
except NameError as erro: #tratamento para erros de nome de variáveis
    print('Erro:', erro)
except IndexError as erro: #tratamento para erros de nome de indices
    print('Erro de Indice:', erro)
except Exception as erro: #genérico
    print('Ocorreu um erro inesperado:', erro)
else:
    print('código executado sem erro')# Execução quando não dá nenhum tipo de erro  
finally:
    print('sempre exeucuta, independente se deu erro ou não')
    #importante para fechar alguma conexão ou arquivo de log que tenha sido aberto durante os tratamentos.
print('continuação do código') # Com esse tratamento de excessão, o restante do código não é interrompido