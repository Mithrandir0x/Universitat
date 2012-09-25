
/**
 * Avaluacio d'un polinomi en m punts equiespaiats a l'interval [a,b]
 * fent us de calcul directe i el metode de Horner. 
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float poli(float z, float a[])
{
    int i;
    float sum;
    sum = a[0];
    for ( i = 1 ; i <= 7 ; i++ )
    {
        sum = sum + a[i] * pow(z, i);
    }
    return sum;
}

float horner(float z, float a[])
{
    int i;
    float sum;
    sum = a[7];
    for ( i = 6 ; i >= 0 ; i-- )
    {
        sum = ( sum * z ) + a[i];
    }
    return sum;
}

int main(void)
{
    int i, m;
    float a, b, x, aval1, aval2, h;
    float coef[8];
    FILE *entrada;
    
    entrada = fopen("inputs\\coeficients.dad", "r");
    if ( entrada == NULL )
    {
        printf("Error en obrir el fitxer inputs\\coeficients.dad\n");
        exit(1);
    }
    for ( i = 0 ; i < 8 ; i++ )
    {
        fscanf(entrada, "%f", &coef[i]);
    }
    fclose(entrada);

    /*/ printf("Indiqueu a, b, m = \n"); */
    scanf("%f %f %d", &a, &b, &m);
    h = ( b - a ) / m;
    printf("%8s %17s %17s %17s\n", "x", "poli", "horner", "diferencia");
    for ( i = 0 ; i < m ; i++ )
    {
        x = a + ( i * h );
        aval1 = poli(x, coef);
        aval2 = horner(x, coef);
        printf("%15.6e %15.6e %15.6e %15.6e\n", x, aval1, aval2, fabs(aval1 - aval2));
    }

    return 0;
}
