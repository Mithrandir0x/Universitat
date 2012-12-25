/* LOPEZ: SANCHEZ: ORIOL: 46459536L: */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "../COMMON/include/algebra_lineal.h"
#include "../COMMON/include/matriu.h"
#include "../COMMON/include/vector.h"
#include "../COMMON/include/zero_funcions.h"

void S0(double *x, double *y)
{
    y[0] = x[0] + x[1] + x[2] - 1;
    y[1] = x[1] + x[2];
    y[2] = ( x[0] * x[0] ) + ( 0.75 * x[1] );
}

void D_S0(double *x, double **y)
{
    y[0][0] = 1;
    y[0][1] = 1;
    y[0][2] = 1;

    y[1][0] = 0;
    y[1][1] = 1;
    y[1][2] = 1;

    y[2][0] = 2 * x[0];
    y[2][1] = 0.75;
    y[2][2] = 0;
}

void S1(double *x, double *y)
{
    y[0] = ( x[0] * x[0] ) + ( x[1] * x[1] ) + ( x[2] * x[2] ) - 1;
    y[1] = ( 0.25 * ( x[0] - x[1] ) * ( x[0] - x[1] ) ) + ( ( x[0] + x[1] ) * ( x[0] + x[1] ) ) + ( x[2] * x[2] ) - 1;
    y[2] = ( ( x[0] - x[1] ) * ( x[0] - x[1] ) ) + ( ( x[0] + x[1] ) * ( x[0] + x[1] ) ) + ( 0.25 * x[2] * x[2] ) - 1;
}

void D_S1(double *x, double **y)
{
    y[0][0] = 2 * x[0];
    y[0][1] = 2 * x[1];
    y[0][2] = 2 * x[2];

    y[1][0] = ( 0.5 * ( x[0] - x[1] ) ) + ( 2 * ( x[0] + x[1] ) );
    y[1][1] = ( 0.5 * ( x[0] - x[1] ) ) + ( 2 * ( x[0] + x[1] ) );
    y[1][2] = 2 * x[2];

    y[2][0] = ( 2 * ( x[0] - x[1] ) ) + ( 2 * ( x[0] + x[1] ) );
    y[2][1] = ( 2 * ( x[0] - x[1] ) ) + ( 2 * ( x[0] + x[1] ) );
    y[2][2] = 0.5 * x[2];
}

int main()
{
    int i = 0, j = 0, k = 100, maxIteracions = 50;
    double q_a = -1, q_b = 1, tolerancia = 1E-10, q_a_b = 0, RAND_MAX_D = 0;
    double *x0 = NULL, *zero = NULL;

    M_F_GEN_PTR_D sistemes[2] = {
        &S0,
        &S1
    };

    M_DF_GEN_PTR_D derivades_sistemes[2] = {
        &D_S0,
        &D_S1
    };

    scanf("%d %d %lf", &maxIteracions, &k, &tolerancia);

    x0 = vector_d(3);
    zero = vector_d(3);

    srand(time(NULL));
    RAND_MAX_D = (double) RAND_MAX;
    q_a_b = q_b - q_a;

    for ( i = 0 ; i < 2 ; i++ )
    {
        for ( j = 0 ; j < k ; j++ )
        {
            x0[0] = q_a + ( ( (double) rand() / RAND_MAX_D ) * ( q_a_b ) );
            x0[1] = q_a + ( ( (double) rand() / RAND_MAX_D ) * ( q_a_b ) );
            x0[2] = q_a + ( ( (double) rand() / RAND_MAX_D ) * ( q_a_b ) );

            printf("(%3.14e, %3.14e, %3.14e)", x0[0], x0[1], x0[2]);

            if ( newton_multiple_d(3, x0, zero, sistemes[i], derivades_sistemes[i], tolerancia, maxIteracions) == RESULT_OK )
            {
                printf(" -> (%3.10e, %3.10e, %3.10e)\n", zero[0], zero[1], zero[2]);
            }
            else
            {
                printf(" -> NULL\n");
            }
        }
    }

    free(x0);
    free(zero);

    return 0;
}
