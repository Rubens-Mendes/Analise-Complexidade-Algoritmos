#include <iostream>
#include <algorithm>

using namespace std;

//Solução Recursiva para o problema, recebe a matriz do tamanho desejado, número de linhas, colunas e um ponteiro para contador
int matQuadRec(int m[9][5], int row, int col, int* count){
    int tempCount;
    //Caso base
    if (row < 0 || col < 0)
        return 0;
    //Se a coluna for igual a 1, fazemos como no exercício dinâmico, onde pegamos os vizinhos à esquerda, acima, e na diagonal superior esquerda
    //Escolhemos o valor mínimo e somamos 1
    if(m[row][col] == 1)
        tempCount = min(matQuadRec(m,row,col-1,count),min(matQuadRec(m,row-1,col,count),matQuadRec(m,row-1,col-1,count))) + 1;
    //Se não fazemos o mesmo processo, porém sem somar 1.
    else
        tempCount = min(matQuadRec(m,row,col-1,count),min(matQuadRec(m,row-1,col,count),matQuadRec(m,row-1,col-1,count)));
    //O Count sempre será atualizado de acordo com o retorno da cláusula max, entre o próprio count e o tempCount.
    *count = max(*count, tempCount);
    return tempCount;
}

int main(){
    int mteste[9][5] = {{0,0,0,0,0},
                        {0,0,0,0,0},
                        {0,0,0,0,0},
                        {0,0,0,0,0},
                        {0,0,0,0,0},
                        {0,0,1,0,0},
                        {0,0,0,0,0},
                        {0,0,0,0,0},
                        {0,0,0,0,0}};

    int count = 0;
    //Pega as dimensões da matriz
    int col = *(&mteste[0] + 1) - mteste[0];
    int row = *(&mteste + 1) - mteste;
    //Chama a função, e retorna o count, que é o número da maior sub-matriz quadrada de 1's.
    matQuadRec(mteste,row-1,col-1,&count);
    cout << "Resultado da Solucao Recursiva: " << count;
    return 0;
}
