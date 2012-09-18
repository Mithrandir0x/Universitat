
/*
 * Calcul d'una sucessio en precisio simple.
 */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    int n;
    float a, b, x0, y0, x1, y1, t, aux0, aux1;

    scanf("%f %f %f", &a, &b, &x0);

    aux0 = x0 / a;
    if ( fabs(aux0) > 1. )
    {
        printf("No es pot fer l'arrel quadrada\n");
        exit(1);
    }

    y0 = b * sqrt(1.f  - aux0 * aux0);
    aux1 = y0 / b;
    printf("%3s %18s\n", "#n", "t");
    t = aux0 * aux0 + aux1 * aux1;
    printf("%3d%18.e\n", 0, t);
    for ( n = 1 ; n <= 40 ; n++ )
    {
        aux0 = x0 / a;
        aux1 = y0 / b;
        
        x1 = ( 2.f * x0 * y0 ) / b;
        y1 = aux0 * aux0 - aux1 * aux1;
        
        aux0 = x1 / a;
        aux1 = y1 / b;
        t = aux0 * aux0 + aux1 * aux1;
        
        printf("%3d%18.6e\n", n, t);

        x0 = x1;
        y0 = y1;
    }

    return 0;
}
