/* LOPEZ: SANCHEZ: ORIOL: 46459536L: */

#include <stdio.h>
#include <stdlib.h>

#include "../COMMON/include/algebra_lineal.h"
#include "../COMMON/include/matriu.h"
#include "../COMMON/include/vector.h"

int main(void)
{
    int n = 0;
    double tolerancia = 0.f;
    double **A = NULL, *B = NULL, *x = NULL;

    scanf("%d %lf", &n, &tolerancia);
    A = llegir_matriu_d(n, n);
    B = llegir_vector_d(n);
    x = vector_d(n);

    if ( A != NULL && B != NULL && x != NULL )
    {
        resol_sistema_lineal_triangular_simple_d(n, A, B, x, tolerancia);
        escriure_vector_d(n, x);
    }

    return 0;
}
