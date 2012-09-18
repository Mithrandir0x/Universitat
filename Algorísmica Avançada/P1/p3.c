
/*
 * Programa per calcular l'epsilon de la maquina.
 *
 * Vale, si, es una copiada de la Wikipedia... (http://en.wikipedia.org/wiki/Machine_epsilon)
 */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void calculateMachineEpsilonDouble()
{
    double eps = 1.0f;

    printf("epsilon, 1 + epsilon\n");
    do
    {
        printf("%G\t%.20f\n", eps, ( 1.0f + eps ));
        eps /= 2.f;
    }
    while( (double)(1.0f + (eps/2.0f)) != 1.0f );

    printf("\nEpsilon de la maquina (DOUBLE): %G\n", eps);
}

void calculateMachineEpsilonFloat()
{
    float eps = 1.0f;

    printf("epsilon, 1 + epsilon\n");

    do
    {
        printf("%G\t%.20f\n", eps, ( 1.0f + eps ));
        eps /= 2.f;
    }
    while( (float)(1.0f + (eps/2.0f)) != 1.0f );

    printf("\nEpsilon de la maquina (FLOAT): %G\n", eps);
}

int main(void)
{
    calculateMachineEpsilonFloat();
    printf("\n");
    calculateMachineEpsilonDouble();

    return 0;
}
