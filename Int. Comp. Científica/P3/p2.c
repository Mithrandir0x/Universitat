/*
 * Calcul del producte de matrius de forma eficient
 */

#include <stdio.h>
#include <stdlib.h>
#include "../COMMON/include/utils.h"

int main(void)
{
    int m = 0, n = 0;
    float *x = NULL, *y = NULL, *aux = NULL;
    float **A = NULL, **B = NULL;

    /* printf("Doneu les dimensions de la matriu (n, m) = \n"); */
    scanf("%d %d", &n, &m);

    /* printf("Doneu els (%d x %d) elements de la matriu A\n", m, n); */
    A = llegir_matriu(m, n);

    /* printf("Doneu els (%d x %d) elements de la matriu B\n", n, m); */
    B = llegir_matriu(n, m);

    /* printf("Doneu els %d elements del vector x\n", m); */
    x = llegir_vector(m);

    aux = producte_matriu_vector(n, m, B, x); /* aux = B * x       */
    y = producte_matriu_vector(n, m, A, aux); /*   y = A * ( aux ) */

    escriure_vector(m, x);
    escriure_vector(m, y);

    printf("El modul de x es = %15.6e\n", modul_vector(m, x));
    printf("El modul de y es = %15.6e\n", modul_vector(m, y));

    printf("El producte escalar de x amb y es = %15.6e\n", producte_escalar(m, x, y));

    return 0;
}
