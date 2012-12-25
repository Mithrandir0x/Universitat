/* LOPEZ: SANCHEZ: ORIOL: 46459536L: */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "../COMMON/include/algebra_lineal.h"
#include "../COMMON/include/vector.h"
#include "../COMMON/include/zero_funcions.h"

#define PI 3.141592653589793

/*
    Comanda GNUPLOT:
        f(x) = x*x + sin(x) - 3.14
        plot f(x)
 */

double f_a(double x) { return x*x + sin(x) - PI; }
double df_a(double x) { return 2*x + cos(x); }

double f_b(double x) { return 1 - log(x); }
double df_b(double x) { return -1/x; }

double f_c(double x) { return sqrt(x) - exp(-x); }
double df_c(double x) { return 1/( 2*sqrt(x) ) + exp(-x); }

/*
    Tardarà molt més a convergir cap a l'arrel per l'ordre de la funció.
    Com a tal, l'error assumit serà a prop de: e_{n+1} = K * e_{n^1},
    per tant, s'hauran de fer moltes més iteracions a diferència d'altres funcions
    d'ordre més gran.
 */
double f_d(double x) { return ( ( exp(x) - exp(-x) ) / 2 ) - sin(x); }
double df_d(double x) { return ( ( exp(x) + exp(-x) ) / 2 ) - cos(x); }

int main()
{
    int maxIteracions = 0, i = 0;
    double tolerancia = 0.f, x0 = 0.f, zero = 0.f;
    /* Es fa un vector amb els punters de les funcions a calcular newton */
    M_F_PTR_D funcions[4] = { &f_a, &f_b, &f_c, &f_d },
        funcions_derivades[4] = { &df_a, &df_b, &df_c, &df_d };

    for ( ; i < 4 ; i++ )
    {
        scanf("%d %lf %lf", &maxIteracions, &tolerancia, &x0);

        printf("F(%d) - maxiter: %d - tol: %.15e - x0: %.15e\n", i, maxIteracions, tolerancia, x0);

        if ( newton_d(x0, &zero, funcions[i], funcions_derivades[i], tolerancia, maxIteracions) == RESULT_OK )
        {
            printf("%.15e\n", zero);
        }
        else
        {
            printf("No s'ha pogut trobar un zero de funcio.\n");
        }
    }

    return 0;
}
