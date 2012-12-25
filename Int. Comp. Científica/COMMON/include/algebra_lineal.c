/**
    @brief Implementació d'operacions comunes d'àlgebra lineal.

    Aquesta llibreria agrupa una sèrie de funcions de càlcul comunes en àlgebra lineal.

    Per identificar les funcions d'àmbit 'double', només cal mirar al final del
    nom de la funció. Si té '_d', significa que funciona amb 'double's.

    @author olopezsa13
    @file algebra_lineal.c
 */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "algebra_lineal.h"
#include "matriu.h"
#include "vector.h"

/**
    @brief Retorna el vector resultant de la multiplicació d'una matriu amb un vector.

    Donat el vector V i la matriu M:

    \f[
        V\quad = \quad \begin{bmatrix} v_{ 1 } \\ v_{ 2 } \\ \vdots  \\ v_{ m } \end{bmatrix}
    \f]

    \f[
        M\quad =\quad 
            \begin{bmatrix} 
                m_{ 11 } & m_{ 12 } & \dots  & m_{ 1m } \\
                m_{ 21 } & m_{ 22 } & \dots  & m_{ 2m } \\
                \vdots  & \vdots  & \ddots  & \vdots  \\
                m_{ n1 } & m_{ n2 } & \dots  & m_{ nm }
            \end{bmatrix}
    \f]

    Es calcula el seu producte resultant:

    \f[
        M \times V \quad = \quad
            \begin{bmatrix}
                \sum _{ k=1 }^{ m }{ { m }_{ 1k }{ v }_{ k } } \\
                \sum _{ k=1 }^{ m }{ { m }_{ 2k }{ v }_{ k } } \\
                \vdots \\
                \sum _{ k=1 }^{ m }{ { m }_{ nk }{ v }_{ k } }
            \end{bmatrix}
    \f]

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu i d'elements del vector.
    @param M Matriu.
    @param V Vector.
    @return Punter del vector resultant del producte.
 */
float *producte_matriu_vector(int n, int m, float **M, float *V)
{
    int i = 0, j = 0;
    float *r = vector(n);

    for ( i = 0 ; i < n ; i++ )
    {
        r[i] = 0.f;
        for ( j = 0 ; j < m ; j++ )
        {
            r[i] += M[i][j] * V[j];
        }
    }

    return r;
}

/**
    @brief Retorna el vector resultant de la multiplicació d'una matriu amb un vector.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    Donat el vector V i la matriu M:

    \f[
        V\quad = \quad \begin{bmatrix} v_{ 1 } \\ v_{ 2 } \\ \vdots  \\ v_{ m } \end{bmatrix}
    \f]

    \f[
        M\quad =\quad 
            \begin{bmatrix} 
                m_{ 11 } & m_{ 12 } & \dots  & m_{ 1m } \\
                m_{ 21 } & m_{ 22 } & \dots  & m_{ 2m } \\
                \vdots  & \vdots  & \ddots  & \vdots  \\
                m_{ n1 } & m_{ n2 } & \dots  & m_{ nm }
            \end{bmatrix}
    \f]

    Es calcula el seu producte resultant:

    \f[
        M \times V \quad = \quad
            \begin{bmatrix}
                \sum _{ k=1 }^{ m }{ { m }_{ 1k }{ v }_{ k } } \\
                \sum _{ k=1 }^{ m }{ { m }_{ 2k }{ v }_{ k } } \\
                \vdots \\
                \sum _{ k=1 }^{ m }{ { m }_{ nk }{ v }_{ k } }
            \end{bmatrix}
    \f]

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu i d'elements del vector.
    @param M Matriu.
    @param V Vector.
    @return Punter del vector resultant del producte.
 */
double *producte_matriu_vector_d(int n, int m, double **M, double *V)
{
    int i = 0, j = 0;
    double *R = vector_d(n);

    for ( i = 0 ; i < n ; i++ )
    {
        R[i] = 0.f;
        for ( j = 0 ; j < m ; j++ )
        {
            R[i] += M[i][j] * V[j];
        }
    }

    return R;
}

/**
    @brief Retorna la matriu resultant del producte de dues matrius.

    Donades dues matrius A, de tamany n x p i B, de tamany p x m:

    \f[
        A\quad =\quad 
            \begin{bmatrix} 
                a_{ 11 } & a_{ 12 } & \dots  & a_{ 1p } \\
                a_{ 21 } & a_{ 22 } & \dots  & a_{ 2p } \\
                \vdots  & \vdots  & \ddots  & \vdots  \\
                a_{ n1 } & a_{ n2 } & \dots  & a_{ np }
            \end{bmatrix}
    \f]

    \f[
        B\quad =\quad 
            \begin{bmatrix} 
                b_{ 11 } & b_{ 12 } & \dots  & b_{ 1m } \\
                b_{ 21 } & b_{ 22 } & \dots  & b_{ 2m } \\
                \vdots  & \vdots  & \ddots  & \vdots  \\
                b_{ p1 } & b_{ p2 } & \dots  & b_{ pm }
            \end{bmatrix}
    \f]

    Es calcula el producte de les matrius, donant una matriu de tamany n x m:

    @param n Nombre de files de la matriu A.
    @param p Nombre de columnes de la matriu A i nombre de files de la columna B.
    @param m Nombre de files de la matriu B.
    @param A Matriu.
    @param B Matriu.
    @return Punter a matriu de tamany n x m, amb el resultat del producte.
 */
float **producte_matriu_matriu(int n, int p, int m, float **A, float **B)
{
    int i = 0, j = 0, k = 0;
    float **C = NULL;

    C = matriu(n, m);
    for ( i = 0 ; i < n ; i++ )
    {
        for ( j = 0 ; j < m ; j++ )
        {
            C[i][j] = 0.0f;
            for ( k = 0 ; k < p ; k++ )
            {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return C;
}

/**
    @brief Retorna el moderador de la bondat de les solucions d'un sistema.

    Donat un sistema d'equacions expressat per \f$Ax=B\f$, retorna el moderador de la bondat
    de la solució x proposada.

    Quan més proper a zero és el valor retornat, major la correctessa de la solució proposada.

    @param n Nombre de files de la matriu A i d'elements del vector B.
    @param m Nombre de columnes de la matriu A.
    @param A Matriu.
    @param X Vector de solucions.
    @param B Vector de termes independents.
    @return Moderador.
 */
double verificar_resolucio_sistema(int n, int m, double **A, double *X, double *B)
{
    double *aux = NULL;

    aux = producte_matriu_vector_d(n, m, A, X);
    aux = resta_vector_d(n, aux, B);

    return modul_vector_d(n, aux);
}

/**
    @brief Resol el sistema triangular.

    Donat un sistema \f$Ax=B\f$, on A és una matriu triangular superior, s'intenta calcular
    les solucions del sistema de forma tradicional.

    Si algun dels elements de la diagonal de la matriu és menor que la tolerància, aleshores
    el sistema no es pot resoldre, ja que hi hauria un error de càlcul relativament important.

    @param n Nombre de files i columnes de la matriu A, i el nombre d'elements del vector B.
    @param A Matriu.
    @param B Vector de termes independents.
    @param x Vector de solucions a calcular.
    @param tol Valor de tolerància permesa.
    @return RESULT_OK si tot ha anat be. RESULT_ERROR si ha hagut algun error.
 */
int resol_sistema_lineal_triangular_simple(int n, float **A, float *B, float *x, float tol)
{
    int i = n - 1, j = 0;
    int rollback = 0;

    if ( fabs(A[i][i]) < tol )
        return RESULT_ERROR;

    x[i] = B[i] / A[i][i];

    for ( ; i >= 0 ; i-- )
    {
        if ( fabs(A[i][i]) < tol )
        {
            rollback = 1;
            break;
        }

        x[i] = B[i];
        for ( j = i + 1 ; i < n ; j++ )
        {
            x[i] -= A[i][j] * x[j];
        }
        x[i] = x[i] / A[i][i];
    }

    if ( rollback )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            x[i] = 0.f;
        }

        return RESULT_ERROR;
    }

    return RESULT_OK;
}

/**
    @brief Resol el sistema triangular.

    Donat un sistema \f$Ax=B\f$, on A és una matriu triangular superior, s'intenta calcular
    les solucions del sistema de forma tradicional.

    Si algun dels elements de la diagonal de la matriu és menor que la tolerància, aleshores
    el sistema no es pot resoldre, ja que hi hauria un error de càlcul relativament important.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files i columnes de la matriu A, i el nombre d'elements del vector B.
    @param A Matriu.
    @param B Vector de termes independents.
    @param x Vector de solucions a calcular.
    @param tol Valor de tolerància permesa.
    @return RESULT_OK si tot ha anat be. RESULT_ERROR si ha hagut algun error.
 */
int resol_sistema_lineal_triangular_simple_d(int n, double **A, double *B, double *x, double tol)
{
    int i = n - 1, j = 0;
    int rollback = 0;

    if ( fabs(A[i][i]) < tol )
        return RESULT_ERROR;

    x[i] = B[i] / A[i][i];
    i--;

    for ( ; i >= 0 ; i-- )
    {
        if ( fabs(A[i][i]) < tol )
        {
            rollback = 1;
            break;
        }

        x[i] = B[i];
        for ( j = i + 1 ; j < n ; j++ )
        {
            x[i] -= A[i][j] * x[j];
        }
        x[i] = x[i] / A[i][i];
    }

    if ( rollback )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            x[i] = 0.f;
        }

        return RESULT_ERROR;
    }

    return RESULT_OK;
}

/**
    @brief Intenta transformar el sistema proposat en un sistema triangular resoluble.

    Donat un sistema \f$Ax=B\f$, s'aplica l'algorisme de Gauss per calcular un sistema
    triangular.

    Aquesta operació és atòmica. Si hi ha un problema durant el càlcul, aleshores es
    restauraran les variables al seu estat inicial.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files i columnes de la matriu A, i el nombre d'elements del vector B.
    @param A Matriu.
    @param B Vector de termes independents.
    @param tol Valor de tolerància permesa.
    @return RESULT_OK si tot ha anat be. RESULT_ERROR si ha hagut algun error.
 */
int gauss_d(int n, double **A, double *B, double tol)
{
    int k = 0, l = 0, j = 0;
    double **m = matriu_d(n, n);

    double **c_A = copia_matriu_d(n, n, A);
    double *c_B = copia_vector_d(n, B);

    /* printf("n: %d\n", n); */

    if ( A != NULL && B != NULL )
    {
        /*printf("%15.6e\n", B[0]);
        printf("%15.6e\n", c_B[0]);*/

        for ( ; k < n - 1 ; k++ )
        {
            /* printf("k: %d\n", k); */
            if ( fabs(A[k][k]) < tol )
            {
                copiar_en_matriu_d(n, n, c_A, A);
                copiar_en_vector_d(n, c_B, B);

                alliberar_matriu_d(n, c_A);
                free(c_B);

                printf("Nombre amb tolerancia molt baixa.\n");

                return RESULT_ERROR;
            }
            
            for ( l = k + 1 ; l < n ; l++ )
            {
                /* printf("  l: %d\n", l); */
                /* printf("%15.6e\n", A[k][k]); */
                m[l][k] = A[l][k] / A[k][k];
                A[l][k] = 0;
                
                for ( j = k + 1 ; j < n ; j++ )
                {
                    /* printf("    j: %d\n", j); */
                    A[l][j] = A[l][j] - ( m[l][k] * A[k][j] );
                }
                B[l] = B[l] - ( m[l][k] * B[k] );
            }
        }

        alliberar_matriu_d(n, c_A);
        free(c_B);

        return RESULT_OK;
    }

    return RESULT_ERROR;
}

/**
    @brief Intenta transformar el sistema proposat en un sistema triangular resoluble.

    Donat un sistema \f$Ax=B\f$, s'aplica l'algorisme de Gauss amb pivotatge màxim per
    calcular un sistema triangular.

    Aquesta operació és atòmica. Si hi ha un problema durant el càlcul, aleshores es
    restauraran les variables al seu estat inicial.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files i columnes de la matriu A, i el nombre d'elements del vector B.
    @param A Matriu.
    @param B Vector de termes independents.
    @param tol Valor de tolerància permesa.
    @return RESULT_OK si tot ha anat be. RESULT_ERROR si ha hagut algun error.
 */
int gauss_pivotatge_maxim_d(int n, double **A, double *B, double tol)
{
    int k = 0, l = 0, j = 0, l_ = 0, l_max = 0;
    double **m = matriu_d(n, n);
    double **c_A = copia_matriu_d(n, n, A);
    double *c_B = copia_vector_d(n, B);

    /* printf("n: %d\n", n); */

    if ( A != NULL && B != NULL )
    {
        /*printf("%15.6e\n", B[0]);
        printf("%15.6e\n", c_B[0]);*/

        for ( ; k < n - 1 ; k++ )
        {
            l = k + 1;
            l_max = l;
            for ( l_ = l + 1 ; l_ < n ; l_++ )
            {
                /* printf("    l_: %d\n", l_); */
                if ( fabs(A[l_][k]) > fabs(A[l_max][k]) )
                {
                    l_max = l_;
                }
            }

            if ( l_max != l )
            {
                intercanviar_fila_d(n, l, l_max, A);
                intercanviar(B[l], B[l_max]);
            }

            if ( fabs(A[k][k]) < tol )
            {
                copiar_en_matriu_d(n, n, c_A, A);
                copiar_en_vector_d(n, c_B, B);

                alliberar_matriu_d(n, c_A);
                free(c_B);

                printf("Nombre amb tolerancia molt baixa.\n");
                printf("GURU MEDITATION. k: %d - l_max: %d\n", k, l_max);

                return RESULT_ERROR;
            }

            for ( ; l < n ; l++ )
            {
                /* printf("  l: %d\n", l); */
                /* printf("%15.6e\n", A[k][k]); */
                m[l][k] = A[l][k] / A[k][k];
                A[l][k] = 0;
                
                for ( j = k + 1 ; j < n ; j++ )
                {
                    /* printf("    j: %d\n", j); */
                    A[l][j] = A[l][j] - ( m[l][k] * A[k][j] );
                }
                B[l] = B[l] - ( m[l][k] * B[k] );
            }
        }

        alliberar_matriu_d(n, c_A);
        free(c_B);

        return RESULT_OK;
    }

    return RESULT_ERROR;
}

/**
    @brief Retorna el determinant d'una matriu de 3x3.

    @param M Punter cap a la matriu.
    @return Valor del determinant de la matriu.
 */
double sarrus_d(double **M)
{
    return (M[0][0] * M[1][1] * M[2][2]) +
        (M[0][1] * M[1][2] * M[2][0]) +
        (M[0][2] * M[1][0] * M[2][1]) -
        (M[2][0] * M[1][1] * M[0][2]) -
        (M[2][1] * M[1][2] * M[0][0]) -
        (M[2][2] * M[1][0] * M[0][1]);
}
