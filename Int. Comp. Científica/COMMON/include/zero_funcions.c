/**
    @brief Funcions comunes per càlcul de zeros de funcions.

    @author olopezsa13
    @file zero_funcions.c
 */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "common.h"
#include "vector.h"
#include "matriu.h"
#include "algebra_lineal.h"
#include "zero_funcions.h"

/**
    @brief Calcular la imatge d'un punt donat un polinomi de forma \f$p(x) = a_0 + a_1x + a_2x^2 + ... + a_nx^n\f$

    Donat un polinomi p expressat com a \f$p(x) = a_0 + a_1x + a_2x^2 + ... + a_nx^n\f$, es vol calcular la imatge
    d'un punt \f$x\f$ en el polinomi pel mètode de Horner.

    S'ha d'expressar el polinomi pels seus coeficients en un vector: \f$[a_0,a_1,a_2,...,a_n]\f$

    @param g Grau del polinomi
    @param x Punt en la recta real a calcular la imatge.
    @param P Vector amb els coeficients del polinomi.
    @return La imatge del punt x en el polinomi P.
 */
float horner(int g, float x, float *P)
{
    int i = g - 1;
    float r = P[g];

    for ( ; i >= 0 ; i-- )
    {
        r = ( r * x ) + P[i];
    }
    return r;
}

/**
    @brief Calcular la imatge d'un punt donat un polinomi de forma \f$p(x) = a_0 + a_1x + a_2x^2 + ... + a_nx^n\f$

    Donat un polinomi p expressat com a \f$p(x) = a_0 + a_1x + a_2x^2 + ... + a_nx^n\f$, es vol calcular la imatge
    d'un punt \f$x\f$ en el polinomi pel mètode de Horner.

    S'ha d'expressar el polinomi pels seus coeficients en un vector: \f$[a_0,a_1,a_2,...,a_n]\f$

    @param g Grau del polinomi.
    @param x Punt en la recta real a calcular la imatge.
    @param P Vector amb els coeficients del polinomi.
    @return La imatge del punt x en el polinomi P.
 */
double horner_d(int g, double x, double *P)
{
    int i = g - 1;
    double r = P[g];

    for ( ; i >= 0 ; i-- )
    {
        r = ( r * x ) + P[i];
    }
    return r;
}

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

/**
    @brief Mètode de Newton per a funcions amb més d'una variable.

    @param r Índex de l'espai R.
    @param x Vector que descriu el punt inicial per on comença Newton.
    @param zero Vector on guardar el zero de funció si convergeix amb el punt inicial proposat.
    @param f Punter a funció de diverses variables.
    @param df Punter a funció derivada de la primera funció.
    @param tol La tolerància permessa pel zero de funció si convergeix.
    @param maxIteracions Nombre màxim d'iteracions que Newton fa abans de finalitzar el procés sense haver pogut trobar un zero.
    @return RESULT_OK si Newton convergeix cap a un zero donat el punt inicial proposat. En cas contrari, RESULT_ERROR.
 */
int newton_multiple_d(int r, double *x, double *zero, M_F_GEN_PTR_D f, M_DF_GEN_PTR_D df, double tol, int maxIteracions)
{
    int i = 0;
    double *f_x = NULL, *ax = NULL, *xn1 = NULL, *dif_xn1_x = NULL;
    double **df_x = NULL;

    f_x = vector_d(r);
    df_x = matriu_d(r, r);
    ax = vector_d(r);
    xn1 = vector_d(r);
    dif_xn1_x = vector_d(r);

    /* printf("\n"); */

    copiar_en_vector_d(r, x, xn1);
    maxIteracions--;

    while ( TRUE )
    {
        f(x, f_x);
        df(x, df_x);

        /* printf("x: "); escriure_vector_d(3, x);
        printf("f_x: "); escriure_vector_d(3, f_x);
        printf("df_x:\n");escriure_matriu_d(3, 3, df_x); */

        if ( i > maxIteracions /* || sarrus_d(df_x) == 0 */ /* || fabs(df(x)) < tol */ )
        {
            printf("S'ha asolit el màxim d'iteracions permeses.\n");
            break;
        }

        /*

        No és necessari comprobar el determinant de la matriu, per que quan es fa gauss,
        ja s'està comprobant.


        if ( sarrus_d(df_x) == 0 )
        {
            printf("El determinant de la matriu de derivades parcials de la funció és zero.\n");
            break;
        } */

        if ( gauss_pivotatge_maxim_d(r, df_x, f_x, tol) == RESULT_OK )
        {
            if ( resol_sistema_lineal_triangular_simple_d(r, df_x, f_x, ax, tol) == RESULT_OK )
            {
                restar_en_vector_d(r, xn1, ax);

                /* printf("ax: "); escriure_vector_d(3, ax);
                printf("xn1: "); escriure_vector_d(3, xn1); */
            }
            else
            {
                printf("El sistema proposat no es pot resoldre.\n");
                break;
            }
        }
        else
        {
            printf("No es pot fer gauss amb pivotatge de màxims.\n");
            break;
        }

        copiar_en_vector_d(r, xn1, dif_xn1_x);
        restar_en_vector_d(r, dif_xn1_x, x);

        if ( modul_vector_d(r, dif_xn1_x) < tol || modul_vector_d(r, f_x) < tol )
        {
            copiar_en_vector_d(r, xn1, zero);

            free(f_x);
            free(ax);
            free(dif_xn1_x);
            free(xn1);
            alliberar_matriu_d(r, df_x);

            return RESULT_OK;
        }

        copiar_en_vector_d(r, xn1, x);
        i++;
    }
    
    free(f_x);
    free(ax);
    free(dif_xn1_x);
    free(xn1);
    alliberar_matriu_d(r, df_x);

    return RESULT_ERROR;
}

/**
    @brief Retorna el vector de coeficients del producte de polinomis P i Q.

    @param g_p Grau del polinomi P.
    @param g_q Grau del polinomi Q.
    @param P Vector amb els coeficients del polinomi P.
    @param Q Vector amb els coeficients del polinomi Q.
    @return Vector amb els coeficients del producte de polinomis entre P i Q.
 */
double *producte_polinomis_d(int g_p, int g_q, double *P, double *Q)
{
    int k = 0, p = 0, g = g_p + g_q;
    double *R = vector_d(g);

    for ( ; k < g ; k++ )
    {
        R[k] = 0;
        for ( p = 0 ; p <= k ; p++ )
        {
            R[k] = R[k] + ( P[p] * Q[k - p] );
        }
    }

    return R;
}

/**
    @brief Calcula la derivada d'un polinomi.

    Donat un polinomi \f$P(x) = a_0 + a_1x^1 + a_2x^2 + ... + a_nx^n, a_n \neq 0\f$, expressat
    en un vector \f$\begin{bmatrix} a_0 & a_1 & a_2 & \cdots &a_n \end{bmatrix}\f$,
    es calcula la seva derivada.

    @param g El grau del polinomi.
    @param P Vector amb els coeficients del polinomi.
    @return Nou vector amb la derivada del polinomi.
 */
double *derivar_coeficients_polinomi_d(int g, double *P)
{
    int i = g - 1;
    double *p = vector_d(g - 1);

    for ( ; i > 0 ; i-- )
    {
        p[i - 1] = P[i] * i;
    }

    return p;
}

/**
    @brief Retorna una funció polinomi, donat un vector de coeficients.

    @param g Grau del polinomi.
    @param P Vector amb els coeficients del polinomi.
    @return Punter amb la funció polinomi a ser usada.
 */
/* M_F_PTR_D polinomi_d(int g, double *P)
{
    double p(double x)
    {
        return horner_d(g, x, P);
    }

    return &p;
} */

/**
    @brief Retorna una funció polinomi factoritzada.

    @param g Grau del polinomi desitjat.
    @param ti Punter a la funció del terme independent.
    @return Punter amb la funció polinomi factoritzada.
 */
/* M_F_PTR_D polinomi_factoritzat_d(int g, M_F_PTR_D ti)
{
    double p(double x)
    {
        int i = 0;
        double r = 0.f;
        
        for ( ; i < g ; i++ )
        {
            r = r * ( x - ti(i) );
        }

        return r;
    }

    return &p;
} */

/**
    @brief Calcula els coeficients del polinomi de grau concret de la funció \f$\prod _{ i=1 }^{ g }{ x-f\left( g \right) }\f$.

    Per calcular el polinomi de la funció \f$\prod _{ i=1 }^{ g }{ x-f\left( g \right) }\f$, on \f$f(g)\f$ és una funció que
    determina els termes independents del polinomi.

    El primer pas es desenvolupar el producte, obtenint els monomis de la funció. A partir d'aquí, es fa el producte de polinomis
    entre cadascun dels monomis i es retorna el resultat.

    @param g Grau del polinomi
    @param ti Punter de funció de termes independents
    @return Vector de coeficients
 */
double *polinomi_coeficients_d(int g, M_F_PTR_D ti)
{
    int i = 0, j = 0;
    /*
        El vector p eventualment arriba a tenir el tamany del grau
        demanat.

        En canvi, q sempre serà de grau 1.
     */
    double *p = vector_d(g);
    double *q = vector_d(2);
    double *r = NULL;

    p[0] = ti(0) * -1;
    p[1] = 1;

    for ( i = 1 ; i < g ; i++ )
    {
        q[0] = ti(i) * -1;
        q[1] = 1;
        r = producte_polinomis_d(i, 1, p, q);
        
        for ( j = 0 ; j < i ; j++ )
        {
            p[j] = r[j];
        }
        /*
            No volem estar acumulant vectors al heap, dels quals no
            s'utilitzaran, tret de l'últim calculat. No es vol
            embrutar de forma innecessaria el heap.
        */
        free(r);
    }
    free(q);

    return p;
}
