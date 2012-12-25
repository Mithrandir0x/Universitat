/* LOPEZ: SANCHEZ: ORIOL: 46459536L: */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define PI 3.141592653589793

#define TRUE 1
#define FALSE 0
#define RESULT_OK 0
#define RESULT_ERROR 1

/*
    Comanda GNUPLOT:
        f(x) = x*x + sin(x) - 3.14
        plot f(x)
 */

/**
    Definició de tipus de punter de funció matemàtica.

    Qualsevol funció matemàtica expressada per y = f(x), es pot
    referenciar utilitzant aquesta definició de punter.
 */
typedef double (*M_F_PTR_D)(double);

/**
    @brief Donada una funció i la seva funció derivada, s'intenta calcular una arrel pel mètode de Newton-Raphson.

    @param x0 Punt inicial en fer la cerca.
    @param y Punter a variable on podrà contenir la solució.
    @param f Punter a la funció.
    @param df Punter a la funció derivada.
    @param tol Valor de la tolerància permesa.
    @param maxIter Nombre màxim d'iteracions a fer abans
    @return RESULT_OK si s'ha pogut calcular l'arrel propera al punt x0. En cas contrari, RESULT_ERROR.
 */
int newton_d(double x0, double *y, M_F_PTR_D f, M_F_PTR_D df, double tol, int maxIter)
{
    int i = 0;
    double x = x0, xn1 = 0.f;

    maxIter--;

    while ( TRUE )
    {
        if ( i > maxIter || fabs(df(x)) < tol )
        {
            return RESULT_ERROR;
        }

        xn1 = x - ( f(x) / df(x) );

        /* printf("i: %d - x: %.15e - xn1: %.15e - |xn1 - xn|: %.15e\n", i, x, xn1, xn1 - x); */
        /* printf("(%02d) x: %.15e - |xn1 - xn|: %.15e\n", i, x, xn1 - x); */

        if ( fabs(xn1 - x) < tol || fabs(f(x)) < tol )
        {
            *y = x;
            return RESULT_OK;
        }

        x = xn1;
        i++;
    }

    return RESULT_ERROR;
}

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
