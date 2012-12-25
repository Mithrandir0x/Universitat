/* LOPEZ: SANCHEZ: ORIOL: 46459536L: */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define RESULT_OK 0
#define RESULT_ERROR 1

#define PI 3.141592653589793
#define A 1.46
#define B 0.0154

typedef double (*M_F_PTR_D)(double);

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

        /* printf("i: %d - x: %.15e - xn1: %.15e - |xn1 - xn|: %.15e\n", i, x, xn1, xn1 - x);
        printf("(%02d) x: %.15e - |xn1 - xn|: %.15e\n", i, x, xn1 - x); */

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

double f(double x)
{
    return x + ( A * sin(2 * PI * x) ) - B;
}

double df(double x)
{
    return 1 + ( A * 2 * PI * cos(2 * PI * x) );
}

int main()
{
    int maxIteracions = 5;
    double tolerancia = 1E-12, x0 = 0.f, x_h = 0.f, x = 0.f, zero = 0.f, h = 1E-3;

    for ( x0 = 0 ; x0 <= 1 ; x0 += h )
    {
        x = x0;
        x_h = x0 + h;

        if ( f(x) * f(x_h) < 0 )
        {
            x0 = x + ( h / 2 );
            if ( newton_d(x0, &zero, &f, &df, tolerancia, maxIteracions) == RESULT_OK )
            {
                printf("(%.4e [%.8e], %.4e [%.8e]) -> %.8e\n", x, f(x), x_h, f(x_h), zero);
            }
            else
            {
                printf("(%.4e [%.8e], %.4e [%.8e]) -> NULL\n", x, f(x), x_h, f(x_h));
            }
        }
    }

    return 0;
}
