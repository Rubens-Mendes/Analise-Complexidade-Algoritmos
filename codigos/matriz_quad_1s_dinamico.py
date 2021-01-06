#!/usr/bin/env python
# coding: utf-8

# In[77]:


import numpy as np
#Função para encontrar o tamanho da sub-matriz de 1's com programação dinâmica
def matQuadDin(m):
    rows = len(m) #Pega a quantidade de linhas
    cols = len(m[0]) #Pega a quantidade de colunas
    
    optSub = np.zeros((rows,cols)) #Gera uma matriz de 0, do formato rows x cols
    
    #Precorre linha e coluna de 0 até o número de linhas ou colunas
    for row in range(0,rows):
        for col in range(0,cols):
            #Se em determinada posição na matriz de entrada o número for 1, a posição correspondente na matriz da subestrutura
            #ótima é o mínimo entre os vizinhos de cima, esquerdo e diagonal superior esquerdo + 1, se não é mantida como zero
            #na matriz resultante, para que seu resultado não afete no final.
            if m[row][col] == 1:
                optSub[row][col] = min(optSub[row-1][col-1],optSub[row-1][col],optSub[row][col-1]) + 1
            else:
                optSub[row][col] = 0
                
    #Passa a matriz 2D para 1D e pega o valor máximo da mesma, esse é o resultado da maior sub-matriz quadrada composta por 1's.         
    arrM = []
    for row in range(0,rows):
        for col in range(0,cols):
            arrM.append(optSub[row][col])
            
    return max(arrM)

mTeste = [[1,1,1,1,0],
          [1,1,1,1,0],
          [1,1,1,1,0],
          [1,1,0,1,0],
          [1,1,1,1,1],
          [1,1,1,1,1],
          [1,1,0,1,1],
          [1,1,1,1,1],
          [1,1,1,1,1]]
print("Implementação Dinâmica: ",matQuadDin(mTeste))


# In[ ]:




