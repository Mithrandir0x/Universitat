/* LOPEZ: SANCHEZ: ORIOL: 46459536L: */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

/*
    Constants usades a diversos llocs de l'aplicació per indicar
    el resultat de la crida d'un mètode.
 */
#define RESULT_ERROR 0

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
    @brief Constructor per còpia de matriu de coma flotant de precisió doble.

    En cas de no haber suficient espai, es retornarà un NULL.

    Si durant la creació de la matriu, no hi hagués suficient espai, 
    s'alliberaria tota la memòria que s'hagués reservat fins al moment
    de l'error.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @param M Matriu a ser copiada.
    @return Punter cap a la matriu creada o NULL.
 */
double **copia_matriu_d(int n, int m, double **M)
{
    int i = 0, j = 0;
    double **cm = matriu_d(n, m);

    if ( cm != NULL && M != NULL )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            for ( j = 0 ; j < m ; j++ )
            {
                cm[i][j] = M[i][j];
            }
        }
    }

    return cm;
}

/**
    @brief Funció per copiar una matriu en una altra.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @param M Matriu a ser copiada.
    @return Punter cap a la matriu creada o NULL.
 */
void copiar_en_matriu_d(int n, int m, double **A, double **C)
{
    int i = 0, j = 0;

    if ( A != NULL && C != NULL )
    {
        for ( ; i < n ; i++ )
        {
            for ( ; j < m ; j++ )
            {
                C[i][j] = A[i][j];
            }
        }
    }
}

/**
    @brief Escriu el contingut d'una matriu pel CES.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @param M Matriu a ser escrita.
 */
void escriure_matriu_d(int n, int m, double **M)
{
    int i = 0, j = 0;

    for ( i = 0 ; i < n ; i++ )
    {
        for ( j = 0 ; j < m ; j++ )
        {
            printf(" %16.7e ", M[i][j]);
        }
        printf("\n");
    }
}

/**
    @brief Allibera la matriu donada de la memòria.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files de la matriu.
    @param M Matriu.
 */
void alliberar_matriu_d(int n, double **M)
{
    int i = 0;
    for ( i = 0 ; i < n ; i++ )
        free(M[i]);
    free(M);
}

/**
    @brief Intercanvia els valors de dues files de la matriu.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param m Nombre de columnes de la matriu.
    @param r_o Fila a intercanviar.
    @param r_c Fila a intercanviar.
    @param M Matriu.
 */
void intercanviar_fila_d(int m, int r_o, int r_c, double **M)
{
    int i = 0;
    double aux = 0.f;

    for ( ; i < m ; i++ )
    {
        aux = M[r_o][i];
        M[r_o][i] = M[r_c][i];
        M[r_c][i] = aux;
    }
}

/**
    @brief Calcula el determinant d'una matriu.

    @param n Nombre de files i columnes de la matriu.
    @param A La matriu a calcular el seu determinant.
    @param tol La tolerancia.
    @return El determinant o RESULT_ERROR si algun dels pivots no és més gran que la tolerancia.
 */
double determinant(int n, double **A, double tol)
{
    int k = 0, l = 0, j = 0, l_ = 0, l_max = 0, swaps = 0;
    double d = 1.f;
    double **m = matriu_d(n, n);
    double **c_A = copia_matriu_d(n, n, A);

    /* printf("n: %d\n", n); */

    if ( A != NULL )
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
                if ( A[l_][k] > A[l_max][k] )
                {
                    l_max = l_;
                }
            }

            if ( l_max != l )
            {
                intercanviar_fila_d(n, l, l_max, A);
                swaps++;
            }

            if ( fabs(A[k][k]) < tol )
            {
                copiar_en_matriu_d(n, n, c_A, A);
                alliberar_matriu_d(n, c_A);

                printf("Nombre amb tolerancia molt baixa.\n");

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
            }
        }

        alliberar_matriu_d(n, c_A);

        for ( k = 0 ; k < n ; k++ )
        {
            d = d * A[k][k]; 
        }

        if ( swaps % 2 != 0 )
        {
            printf("Nombre senar de canvis de columnes.\n");
            d = d * -1;
        }

        return d;
    }

    return RESULT_ERROR;
}

int main(void)
{
    int n = 8, i = 0, j = 0;
    double tolerancia = 1.e-10, resultat = 0.f;
    double **A = NULL;

    A = matriu_d(n, n);
    A[0][0] = 1;
    A[0][1] = 4;
    A[0][2] = 6;
    A[0][3] = 0;
    A[0][4] = 0;
    A[0][5] = 1;
    A[0][6] = 5;
    A[0][7] = 4;
    for ( i = 1 ; i < n ; i++ )
    {
        for ( j = 0 ; j < n ; j++ )
        {
            A[i][j] = fabs(i - j);
        }
    }

    printf("A:\n");
    escriure_matriu_d(n, n, A);

    resultat = determinant(n, A, tolerancia);

    printf("\nA:\n");
    escriure_matriu_d(n, n, A);

    if ( resultat != RESULT_ERROR )
    {
        printf("Determinant: %+.121e\n", resultat);
    }
    else
    {
        printf("No s'ha pogut calcular el determinant de la matriu.\n");
    }

    alliberar_matriu_d(n, A);

    return 0;
}
