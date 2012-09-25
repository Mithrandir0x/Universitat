
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

float *llegir_vector(int n)
{
    int i = 0;
    float *v = NULL;

    v = (float *) malloc(n * sizeof(float));
    if ( v != NULL )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            scanf("%f", &v[i]);
        }
    }

    return v;
}

float *llegir_vector_fitxer(char *path, int n)
{
    int i = 0;
    float *v = NULL;
    FILE *handle = NULL;

    handle = fopen(path, "w");
    if ( handle != NULL )
    {
        v = (float *) malloc(n * sizeof(float));
        if ( v != NULL )
        {
            for ( i = 0 ; i < n ; i++ )
            {
                fscanf(handle, "%f", &v[i]);
            }
        }
    }
    fclose(handle);

    return v;
}

float producte_escalar(int n, float *x, float *y)
{
    int i = 0;
    float r = 0.f;

    for ( i = 0 ; i < n ; i++ )
    {
        r += x[i] * y[i];
    }

    return r;
}

int es_ortogonal(int n, float tol, float *x, float *y)
{
    float pe = producte_escalar(n, x, y);
    return fabs(pe) < tol;
}
