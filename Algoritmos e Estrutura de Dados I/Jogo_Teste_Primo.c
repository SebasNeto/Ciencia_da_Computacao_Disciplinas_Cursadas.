/*  Jogo: Teste Primo.

    Dinânima do jogo:
        Será apresentando ao jogador números primos e será perguntando a ele se o número apresentado é primo (sim) ou (não).

        A cada acerto o jogador ganha 10 pontos.

        A cada erro será descanto -5 pontos do acerto anterior, se logo na primeira pergunta o jogador errar ele ficara com um saldo
        negativo de -5 pontos.

        Jogador: você tem apenas 10 segundos para responder a pergunta, caso contrário o jogo termina automaticamente.

        No final do jogo ou quando ele for finalizado, será apresentado o número de acertos, erros e porcentagem de rendimento.

        Bom jogo! 
*/


/*  Lógica do programa:

    Determinar a lógica de números primos.
    Como identificar o fim do programa e imprimir o desempenho do jogador? Utilizar Bibliotecas especificas.
    Na função Main do programa deve ser incrementado os acertos e erros do jogador para poder apresenta-ló no fim do programa.

*/


#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <stdlib.h>
#include <signal.h> //vai permitir que um processo capture e trate sinais enviados pelo S.O ou por outros processos. Esses sinais são gerados pelo S.O ou por outros processo que podem interromper a execução do processo.
#include <unistd.h> // vai permitir que em determinado processo especifque o tempo em segundos antes do sinal "SIGALRM" ser enviado para o processo.

//#include <windows.h>



#define menorPrimo 2 //menor número primo que pode ser gerado 
#define maiorPrimo 100 //maior número primo que pode ser gerado 
#define pontosCorretos 10 //parabéns - 10 pontos
#define pontosIncorretos -5 //tente mais uma vez - (-5) pontos.
#define tempoEsgotado 10 //seu tempo esgotou - 10 segundos

//função que vai determinar se o número é primo ou não
bool ePrimo(int valor) {
    if (valor <= 1)
        return false;
    for (int i = 2; i < valor; i++) {
        if (valor % i == 0)
            return false;
    }
    return true;
}

//a função abaixo está relacionado com o fim do programa e apresentação dos resultados ao usuário.
//Encerra o jogo assim que o tempo termina
//função relacionada ao SIGALARM e alarm()
//quando o temporizador alarm(time_up) expira o sinal SIGALRM é enviado e chama time_up
int totalPontos = 0, pontosCertos = 0, pontosErrados = 0;
int jogadorAcertou[maiorPrimo], jogadorErrou[maiorPrimo];
int contadorAcertou =0, contadorErrou = 0;

void time_up(int sig) {
    printf(" Tempo Esgotado!!! \n");
    printf("Pontuacao Final: %d\n", totalPontos);
    printf("Pontos Corretos: %d\n", pontosCertos);
    printf("Pontos Incorretos: %d\n", pontosErrados);
    printf("Desempenho: %.2f%%\n", (float) pontosCertos / (pontosCertos + pontosErrados) * 100);
    printf("Numeros corretos pelo Jogador: \n");
    for(int i = 0; i < contadorAcertou; i++){
        printf("%d ",jogadorAcertou[i]);
    }
    printf(" \n Numeros Errados pelo Jogador: \n");
    for(int j = 0; j <contadorErrou; j++){
        printf("%d ",jogadorErrou[j]);
    }
    if((float) pontosCertos / (pontosCertos + pontosErrados) < 0.5){

        printf("\n\nPara saber mais sobre numeros primos, acesse o site: https://pt.wikipedia.org/wiki/Número_primo\n");
        
        system("open https://pt.wikipedia.org/wiki/Número_primo");
        //windons start em vez de open
        printf("Características dos números primos:\n");

        printf("- São divisíveis apenas por 1 e por eles mesmos.\n");

        printf("- São infinitos.\n");

        printf("- O primeiro número primo é o 2.\n");

        printf("- O número primo mais conhecido é o 3.\n");

    }
    exit(0);
}


int main() {
    
    srand(time(NULL)); //inicializa números aleatórios, a cada execução é gerado números diferentes.
    while (1) {
        int valor = menorPrimo + rand() % (maiorPrimo - menorPrimo + 1);
        printf("%d \n",valor);
        printf("O valorero sorteado e primo? (sim/nao): ");

        time_t inicioTime = time(NULL); //armazena a hora atual, servira como comparação.
        char respostaJogador[4];
        
        
        //sleep(tempoEsgotado * 1000);
        //time_up();
        //SIGABRT
        //signal(SIGABRT , time_up); windons 
        signal(SIGALRM, time_up); //quando SIGALRM é recebido time_up é chamado interrompendendo o programa.
        alarm(tempoEsgotado); //envia o sinal SIGALRM assim que o tempo limite expira
        scanf("%s", respostaJogador);

        time_t fimTime = time(NULL); //armazena a hora atual, servira como comparação.

        if (fimTime - inicioTime >= tempoEsgotado) {
            printf("Tempo esgotado!\n");
            break;
        }

        //comparações das respostas do jogador.
        //definições de pontos corretos e incorretos.
        if (ePrimo(valor)) {
            if (respostaJogador[0] == 's') {
                totalPontos += pontosCorretos; //+= adiciona o valor do lado direito ao valor atual da variável.
                pontosCertos++;
                jogadorAcertou[contadorAcertou++] = valor;
            } else {
                totalPontos = totalPontos + pontosIncorretos;  //subtrai os pontos incorretos da pontuação
                pontosErrados++;
                jogadorErrou[contadorErrou++] = valor;
            }
        } else {
            if (respostaJogador[0] == 'n') {
                totalPontos += pontosCorretos;
                pontosCertos++;
                jogadorAcertou[contadorAcertou++] = valor;
            } else {
                totalPontos = totalPontos + pontosIncorretos;
                pontosErrados++;
                jogadorErrou[contadorErrou++] = valor;
            }
        }
    }

    return 0;
}
