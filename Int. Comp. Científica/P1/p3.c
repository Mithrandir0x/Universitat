
/*
 * Programa per calcular l'epsilon de la maquina.
 *
 * Vale, si, es una copiada de la Wikipedia... (http://en.wikipedia.org/wiki/Machine_epsilon)
 */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void calculateMachineEpsilonDoubleFloat()
{
    float f_m_eps = 1.0f;
    double d_m_eps = 1.0f;

    printf("(float) epsilon, (float) 1 + epsilon, (double) epsilon, (double) 1 + epsilon\n");

    do
    {
        printf("%G\t%.20f\t%G\t%.20f\n", f_m_eps, ( 1.0f + f_m_eps ), d_m_eps, ( 1.0f + d_m_eps ));
        
        if ( (float)(1.0f + (f_m_eps/2.0f)) != 1.0f ) 
            f_m_eps /= 2.f;

        d_m_eps /= 2.f;
    }
    while( (float)(1.0f + (f_m_eps/2.0f)) != 1.0f || (double)(1.0f + (d_m_eps/2.0f)) != 1.0f );

    printf("\nEpsilon de la maquina (FLOAT): %G\n", f_m_eps);
    printf("\nEpsilon de la maquina (DOUBLE): %G\n", d_m_eps);
}

int main(void)
{
    calculateMachineEpsilonDoubleFloat();

    return 0;
}
