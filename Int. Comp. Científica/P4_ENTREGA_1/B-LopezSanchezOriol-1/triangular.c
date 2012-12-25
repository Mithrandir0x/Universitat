/* LOPEZ: SANCHEZ: ORIOL: 46459536L: */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

/*
    Constants usades a diversos llocs de l'aplicació per indicar
    el resultat de la crida d'un mètode.
 */
#define RESULT_OK 0
#define RESULT_ERROR 1

/**
    @brief Constructor de vector de coma flotant de precisió doble.

    @param n Nombre d'elements del vector
    @return Punter cap al vector o NULL.
 */
double *vector_d(int n)
{
    return (double *) malloc(n * sizeof(double));
}

/**
    @brief Constructor de matriu de coma flotant de precisió doble.

    En cas de no haber suficient espai, es retornarà un NULL.

    Si durant la creació de la matriu, no hi hagués suficient espai, 
    s'alliberaria tota la memòria que s'hagués reservat fins al moment
    de l'error.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @return Punter cap a la matriu creada o NULL.
 */
double **matriu_d(int n, int m)
{
    int i = 0, x = 0;
    double **M = NULL;

    M = (double **) malloc(n * sizeof(double *));
    if ( M != NULL )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            M[i] = (double *) malloc(m * sizeof(double));
            if ( M[i] == NULL )
            {
                /* 
                    Si no hi ha suficient memoria, alliberar totes
                    les files reservades a memoria, i finalment,
                    alliberar la mateixa referencia a la matriu i
                    posar-la a NULL per garantir l'atomicitat de la
                    operacio.
                */
                for ( x = 0 ; x < i ; x++ )
                {
                    free(M[x]);
                }
                free(M);
                M = NULL;
                break;
            }
        }
    }

    return M;
}

/**
    @brief Retorna un vector a partir de les dades enviades pel CEE.

    El vector retornat és de coma flotant de precisió doble.

    @param n Nombre d'elements dels vectors a ser llegit.
    @return Punter cap al vector.
 */
double *llegir_vector_d(int n)
{
    int i = 0;
    double *v = NULL;

    v = vector_d(n);
    if ( v != NULL )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            scanf("%lf", &v[i]);
        }
    }

    return v;
}

/**
    @brief Retorna una matriu llegida pel CEE.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @return Punter cap a la matriu llegida.
 */
double **llegir_matriu_d(int n, int m)
{
    int i = 0, j = 0;
    double **M = matriu_d(n, m);

    if ( M != NULL )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            for ( j = 0 ; j < m ; j++ )
            {
                scanf("%lf", &M[i][j]);
            }
        }
    }

    return M;
}

/**
    @brief Escriu un vector pel CES.

    Aquest vector té que ser de coma flotant de precisió doble.

    @param n Nombre d'elements del vector.
    @param V Vector a ser escrit.
 */
void escriure_vector_d(int n, double *v)
{
    int i = 0;

    for ( i = 0 ; i < n ; i++ )
        printf(" %16.7e \n", v[i]);
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
