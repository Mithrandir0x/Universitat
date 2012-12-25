/* LOPEZ: SANCHEZ: ORIOL: 46459536L: */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define RESULT_OK 0
#define RESULT_ERROR 1

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

double p_a(double x) { return ( x * x ) - 1; }
double p_a_d(double x) { return 2 * x; }

double p_b(double x) { return ( x * x * x ) - x; }
double p_b_d(double x) { return ( 3 * x * x ) - 1; }

double p_c(double x) { return ( 3 * x * x * x ) - x + 1; }
double p_c_d(double x) { return ( 9 * x * x ) - 1; }

double p_d(double x) { return ( x * x * x * x ) + 1; }
double p_d_d(double x) { return ( 4 * x * x * x ); }

double p_e(double x)
{
    int i = 0;
    double r = 1.f;

    for ( ; i < 6 ; i++ )
    {
        r = r * ( x - ( ( 10 * i ) / ( i + 1 ) ) );
    }

    return r;
}
double p_e_d(double x)
{
    int i = 1;
    double r = 0.f;

    for ( ; i <= 6 ; i++ )
    {
        r = r + ( p_e(x) / ( x - ( ( 10 * i ) / ( i + 1 ) ) ) );
    }

    return r;
}

double p_f(double x)
{
    int i = 1;
    double r = 1.f;

    for ( ; i <= 6 ; i++ )
    {
        r = r * ( x - ( ( i + 1 ) / ( 10 * i ) ) );
    }

    return r;
}
double p_f_d(double x)
{
    int i = 1;
    double r = 1.0f;

    for ( ; i <= 6 ; i++ )
    {
        r = r + ( p_f(x) / ( x - ( ( i + 1 ) / ( 10 * i ) ) ) );
    }

    return r;
}

int main()
{
    int maxIteracions = 0, i = 0;
    double tolerancia = 0.f, x0 = 0.f, zero = 0.f, zero_anterior = 0.f, h = 0.f,
        interval_principi = 0.f, interval_final = 0.f;

    M_F_PTR_D polinomis[6] = { /* FUN */
        &p_a,
        &p_b,
        &p_c,
        &p_d,
        &p_e,
        &p_f
    };

    M_F_PTR_D derivades[6] = { /* DFUN */
        &p_a_d,
        &p_b_d,
        &p_c_d,
        &p_d_d,
        &p_e_d,
        &p_f_d
    };

    double M[6];
    M[0] = 2;
    M[1] = 2;
    M[2] = 5/3;
    M[3] = 2;
    M[4] = 9.f;
    M[5] = 0.3f;

    scanf("%d %lf %lf", &maxIteracions, &h, &tolerancia);

    for ( i = 0 ; i < 1 ; i++ )
    {
        printf("--- Polinomi (%i) ---\n", i);

        for ( x0 = -M[i] ; x0 < M[i] ; x0 += h )
        {
            if ( newton_d(x0, &zero, polinomis[i], derivades[i], tolerancia, maxIteracions) == RESULT_OK )
            {
                /*
                    Els intervals d'atracció queden agrupats de forma més compacta
                    si s'eliminen la resta de decimals que no seran considerats
                    donada la tolerància demanada.
                */
                zero = floor(zero / h) * h;

                if ( zero_anterior != zero )
                {
                    /* Nou zero de funcio trobat */
                    if ( interval_principi < interval_final )
                    {
                        printf("(%.18e, %.18e) -> %.18e\n", interval_principi, interval_final, zero);
                    }

                    interval_principi = x0;
                }
            }
            else
            {
                printf("%.15e -> NULL\n", x0);
            }

            interval_final = x0;
            zero_anterior = zero;
        }

        printf("x0: %.15e - zero: %.15e - i_p: %.15e - i_f: %.15e\n", x0, zero, interval_principi, interval_final);
        printf("---------------------\n");
    }

    return 0;
}
