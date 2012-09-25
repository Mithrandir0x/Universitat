
/*
 * Calcul del producte escalar de dos vectors usant memoria dinamica
 */

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n, i;
    float *x, *y, prod = 0.f;
    
    printf("Doneu la dimensio dels vectors (n) = \n");
    scanf("%d", &n);

    x = (float *) malloc(n * sizeof(float));
    y = (float *) malloc(n * sizeof(float));
    if ( x == NULL || y == NULL )
    {
        printf("No hi ha prou memoria.");
        exit(1);
    }

    printf("Doneu els %d termes de x\n", n);
    for ( i = 0 ; i < n ; i++ )
    {
        scanf("%f", &x[i]);
    }

    printf("Doneu els %d termes de y\n", n);
    for ( i = 0 ; i < n ; i++ )
    {
        scanf("%f", &y[i]);
    }

    for ( i = 0 ; i < n ; i++ )
    {
        prod += x[i] * y[i];
    }

    printf("El producte escalar val: %16.7e\n", prod);
    free(x);
    free(y);

    return 0;
}
