
/*
 * Calcul del producte escalar de dos vectors usant memoria dinamica
 *
 * Modificat per llegir l'input des d'un fitxer.
 */

#include <stdio.h>
#include <stdlib.h>

FILE *agafarFitxer(char *name, char *mode)
{
    FILE *handle;

    handle = fopen(name, mode);
    if ( handle == NULL )
    {
        printf("Error en obrir el fitxer %s\n", name);
        exit(1);
    }

    return handle;
}

void llegirValors(int n, FILE *fitxer, float **v)
{
    int i;
    float *tmp;

    tmp = (float *) malloc(n * sizeof(float));
    if ( v == NULL )
    {
        printf("No hi ha prou memoria.");
        exit(1);
    }

    for ( i = 0 ; i < n ; i++ )
    {
        fscanf(fitxer, "%f", &tmp[i]);
    }

    *v = tmp;
}

float producteEscalar(int n, float *x, float *y)
{
    int i;
    float r = 0.f;

    /* printf("llargada vector: %d\n", n); */

    for ( i = 0 ; i < n ; i++ )
    {
        r += x[i] * y[i];
    }

    return r;
}

int main(void)
{
    int n;
    float *x = NULL, *y = NULL, prod = 0.f;
    char nomFitxer[80];
    FILE *fitxer;

    printf("Doneu la dimensio dels vectors (n) = \n");
    scanf("%d", &n);

    printf("Doneu el nom de fitxer amb els coeficients del vector x = \n");
    scanf("%s", nomFitxer);

    fitxer = agafarFitxer(nomFitxer, "r");
    llegirValors(n, fitxer, &x);
    fclose(fitxer);

    printf("Doneu el nom de fitxer amb els coeficients del vector y = \n");
    scanf("%s", nomFitxer);

    fitxer = agafarFitxer(nomFitxer, "r");
    llegirValors(n, fitxer, &y);
    fclose(fitxer);

    printf("calculant producte escalar\n");
    prod = producteEscalar(n, x, y);

    printf("El producte escalar val: %16.7e\n", prod);
    free(x);
    free(y);

    return 0;
}
