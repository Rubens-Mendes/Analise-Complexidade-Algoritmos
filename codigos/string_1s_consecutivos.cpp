#include <iostream>
using namespace std;
//Str[n] = Se lastN é 0 = str[n-1] + str[n-1]
//       = Se lastN é 1 = str[n-1]
//Função que conta as strings utilizando recursão recebe o tamanho da string e o último nó
int binaryStringsCounterRec(int n, int lastN)
{
    //Previne erro caso o usuário digite 0
    if(n == 0)
        return 0;
    //Caso a string termine em 1 ou seja, addon seja 1, soma apenas 1 na probabilidade, caso seja 0, somam 2 probabilidades de string - Caso Base da recursão
    if(n == 1)
        return (lastN == 1) ? 1 : 2;
    //Se terminar em 0, chama recursão para 2 probabilidades (0 ou 1)
    if(lastN == 0) //T(N) = 2*T(N-1)
        return binaryStringsCounterRec(n-1, 1) + binaryStringsCounterRec(n-1,0);
    //Se terminar em 1, chama recursão para 1 probabilidade (0)
    else
      return binaryStringsCounterRec(n-1, 0);
}

//Função que conta as strings por programação dinâmica
int binaryStringsCounterDin(int n)
{
    //Previne erro caso o usuário digite 0
    if(n == 0)
        return 0;
    //Inicializa 2 inteiros do mesmo tamanho que a string desejada
    int str0, str1, temp_str0;
    //Inicializa os primeiros inteiros com 1, pois caso o tamanho final da string no fim das contas será str0 + str1, sendo str0 = str1 = 1, o caso base.
    //Mostrando que quando o tamanho da string é igual a 1, existem 2 possibilidades de string, sendo elas 0 ou 1.
    //Levando em consideração que str0 contém todas as strings que terminam em 0 sem 1's consecutivos, e str1 contém todas as strings terminadas em 1.
    str0 = str1 = 1; // Caso 0
    for(int i = 1; i < n; i++){
        temp_str0 = str0;
        //Primeiro, se acrescenta o número 1 em todas as strings anteriores que terminam em 0
        str0 += str1;
        //Segundo, se acrescenta o número 0 em todas as strings anteriores que terminam em 1
        str1 = temp_str0;
    }
    //Por último, se somam as duas quantidades, o resultado final será a quantidade de strings sem 1's consecutivos possíveis para determinado valor de n.
    return str0 + str1;
}

// Driver program to test above functions
int main()
{
    cout << binaryStringsCounterDin(20) << endl;
    cout << binaryStringsCounterRec(20,0) << endl;
    return 0;
}