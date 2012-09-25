/*
 * Programa per determinar la ortogonalitat de dos vectors.
 */

#include <stdio.h>
#include <stdlib.h>
#include "../COMMON/include/utils.h"

int main(void)
{
    int n;
    float *x = NULL, *y = NULL, tol = 0.f;

    /* printf("Doneu la dimensio dels vectors (n) = \n"); */
    scanf("%d", &n);

    /* printf("Doneu els coeficients del vector x = \n"); */
    x = llegir_vector(n);

    /* printf("Doneu els coeficients del vector y = \n"); */
    y = llegir_vector(n);

    /* printf("Doneu els coeficients del vector y = \n"); */
    scanf("%f", &tol);

    printf("Producte escalar xy = %15.6e\n", producte_escalar(n, x, y));

    return 0;
}
