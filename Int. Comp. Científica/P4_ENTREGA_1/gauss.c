/* LOPEZ: SANCHEZ: ORIOL: 46459536L: */

#include <stdio.h>
#include <stdlib.h>

#include "../COMMON/include/algebra_lineal.h"
#include "../COMMON/include/matriu.h"
#include "../COMMON/include/vector.h"

int main(void)
{
    int n = 0;
    double tolerancia = 0.f, mod = -1.0f;
    double **A = NULL, *B = NULL, *x = NULL;
    double **c_A = NULL, *c_B = NULL;

    scanf("%d %lf", &n, &tolerancia);
    A = llegir_matriu_d(n, n);
    B = llegir_vector_d(n);
    x = vector_d(n);

    c_A = copia_matriu_d(n, n, A);
    c_B = copia_vector_d(n, B);

    printf("A:\n");
    escriure_matriu_d(n, n, A);

    printf("\nB:\n");
    escriure_vector_d(n, B);

    if ( A != NULL && B != NULL && x != NULL )
    {
        if ( gauss_d(n, A, B, tolerancia) == RESULT_OK )
        {
            printf("\nA:\n");
            escriure_matriu_d(n, n, A);

            printf("\nB:\n");
            escriure_vector_d(n, B);

            if ( resol_sistema_lineal_triangular_simple_d(n, A, B, x, tolerancia) == RESULT_OK )
            {
                printf("\nX:\n");
                escriure_vector_d(n, x);

                mod = verificar_resolucio_sistema(n, n, c_A, x, c_B);

                printf("\nModerador: %15.e\n", mod);
            }
            else
            {
                printf("Hi ha hagut un problema alhora de calcular les solucions del sistema triangular, despres de fer Gauss.\n");
            }
        }
        else
        {
            printf("Hi ha hagut un problema alhora de fer gauss amb la matriu proposada.\n");
        }
    }

    alliberar_matriu_d(n, A);
    alliberar_matriu_d(n, c_A);
    free(B);
    free(c_B);
    free(x);

    return 0;
}
