#!/usr/bin/env python
# coding: utf-8

# In[7]:


import timeit
import numpy as np
    
#Implementação recursiva, cuja explicação está na documentação.
def countPRec(s, i, f):
    #Caso Base 1, quando os iteradores de início e fim se encontram, ou seja, estamos no último caractere da palavra,
    #determinando o fim das comparações
    if i == f:
        return 1
    #Caso base 2, para caso hajam apenas 2 caracteres no palíndromo e ambos sejam iguais, impede casos de erro onde a entrada
    #ja é um palíndromo, como "jeej" ou "aa"
    if s[i] == s[f] and i+1 == f:
        return 2
    #Recursão 1, caso s[i] e s[f] sejam iguais soma-se 2 à quantidade do palíndromo final
    if s[i] == s[f]:
        return countPRec(s, i+1 , f-1) + 2
    #Recursão 2, caso s[i] e s[f] sejam diferentes, pega o máximo entre as 2 recursões
    elif s[i] != s[f]:
        return max(countPRec(s, i+1 , f), countPRec(s, i , f-1))     


#O segredo da memoização está aqui, a função memoize_palindrome recebe a função countPMemo como parâmetro, que é a função à ser
#otimizada. Nela é instanciado o dicionário que será utilizado como cache para a memoização. 
#Como retorno, tem uma outra função chamada access. 
#Basicamente, esta função é um decorador.
def memoize_palindrome(func):
    palindrome_cache = dict()
    
    #A função access, recebe os parâmetros de countPMemo, o objetivo aqui é lidar com problemas sobrepostos armazenando cada 
    #retorno de passo recursivo em um dicionário do formato palindrome_cache[entradas da recursão] = retorno da recursão.  
    #Esse processo é feito quando as entradas um de passo recursivo não estiverem armazenadas no cache.
    #Caso as entradas sejam encontradas no cache, pula esse passo recursivo, poupando o processamento de novos passos
    #que já foram calculados anteriormente.
    def access(s,i,f):
        if (s,i,f) not in palindrome_cache:
            palindrome_cache[s,i,f] = func(s,i,f)
        return palindrome_cache[s,i,f]
    
    return access;
    
#O "@" seguido do nome do decorador, indica que essa função é a que será passada por parâmetro para o decorador
#Faz a mesma função dessas linhas: 
#1 - countPMemo = memoize_palindrome(countPMemo) 
#2 - memoize_palindrome()
@memoize_palindrome
def countPMemo(s, i, f):
    if i == f:
        return 1
    if s[i] == s[f] and i+1 == f:
        return 2
    if s[i] == s[f]:
        return countPMemo(s, i+1 , f-1) + 2
    elif s[i] != s[f]:
        return max(countPMemo(s, i+1 , f), countPMemo(s, i , f-1))    


def countPTab(s): 
    str_size = len(s)
  
    #Inicializa uma matriz n*n com zeros, sendo n o tamanho da string de entrada
    m = np.zeros((str_size,str_size)) 
  
    #Caso base para strings iguais a 1
    for i in range(str_size): 
        m[i][i] = 1
        
    #'j' é o tamanho da subsequência que está sendo avaliada - inicialmente, como já cuidamos do caso base no loop acima
    #iniciamos ele como 2, como queremos que ele vá até o tamanho final da string, adicionamos 1 ao str_size, para que 
    #não percamos uma letra na avaliação.
    for j in range(2, str_size+1): 
        #'i' é o passo da iteração, por exemplo, para a palavra 'balaio' temos os passos 'ba','al','la','ai','io', levando
        #em consideração que o número de passos é tamanho da string - tamanho da substring +1, o loop vai de 0 até o número de passos
        #o 'i' pode ser utilizado para denotar a letra inicial da subsequência.
        for i in range(str_size-j+1): 
            #f é a última letra da subsequência, sendo assim, utilizaremos i e f para fazer as comparações
            f = i+j-1
            #Se A letra inicial da subsequência e a final forem iguais:
            if s[i] is s[f]: 
                #Caso hajam apenas 2 letras na substring, a posição [i][f] da matriz recebe 2
                if j == 2:
                    m[i][f] = 2
                #Senão a posição [i][f] da matriz assume o valor da diagonal inferior esquerda somando 2
                else:
                    m[i][f] = m[i+1][f-1] + 2
            #Se as letras não forem iguais, a posição [i][f] da matriz assume o valor máximo entre o vizinho esquerdo ou de baixo.
            elif s[i] is not s[f]: 
                m[i][f] = max(m[i][f-1], m[i+1][f])
    #print(m)
    return m[0][str_size-1] 

#Função de teste recebe como parâmetro a string a ser avaliada e o método - "Memo"(Memoização) - "Tab"(Tabulação) - "Rec"(Recursão)
def test(s, method):
    print("Tamanho da String: ", len(s))
    if method == "Memo":
        res = countPMemo(s, 0, len(s) - 1)
    elif method == "Tab":
        res = countPTab(s)
    elif method == "Rec":
        res = countPRec(s, 0, len(s) - 1)
        
    print("Tamanho do maior palíndromo: ", res)

#string para testes
str_teste = "abcdefghijklmnopqrstuvwxyz"
#Chamadas da função de teste
test(str_teste,"Memo") #Memoizado
test(str_teste,"Tab") #Tabulado
test(str_teste,"Rec") #Recursivo

#Testes de tempo - recebem a string str_teste
#print("Tempo da Solução Memoizada: ", timeit.timeit('countPMemo(str_teste,0, len(str_teste) - 1)', globals=globals(), number=1))
#print("Tempo da Solução Tabulada: ", timeit.timeit('countPTab(str_teste)', globals=globals(), number=1))
#print("Tempo da Solução Recursiva: ", timeit.timeit('countPRec(str_teste,0, len(str_teste) - 1)', globals=globals(), number=1))


# In[ ]:




