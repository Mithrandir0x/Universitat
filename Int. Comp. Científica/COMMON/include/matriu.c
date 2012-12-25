/**
    @brief Implementació d'operacions comunes amb matrius.

    Per identificar les funcions d'àmbit 'double', només cal mirar al final del
    nom de la funció. Si té '_d', significa que funciona amb 'double's.

    @author olopezsa13
    @file matriu.c
 */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "matriu.h"

/**
    @brief Constructor de matriu.

    En cas de no haber suficient espai, es retornarà un NULL.

    Si durant la creació de la matriu, no hi hagués suficient espai, 
    s'alliberaria tota la memòria que s'hagués reservat fins al moment
    de l'error.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @return Punter cap a la matriu creada o NULL.
 */
float **matriu(int n, int m)
{
    int i = 0, x = 0;
    float **M = NULL;

    M = (float **) malloc(n * sizeof(float *));
    if ( M != NULL )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            M[i] = (float *) malloc(m * sizeof(float));
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
    @brief Constructor per còpia de matriu.

    En cas de no haber suficient espai, es retornarà un NULL.

    Si durant la creació de la matriu, no hi hagués suficient espai, 
    s'alliberaria tota la memòria que s'hagués reservat fins al moment
    de l'error.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @param M Matriu a ser copiada.
    @return Punter cap a la matriu creada o NULL.
 */
float **copia_matriu(int n, int m, float **M)
{
    int i = 0, j = 0;
    float **C = matriu(n, m);

    if ( C != NULL )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            for ( j = 0 ; j < m ; j++ )
            {
                C[i][j] = M[i][j];
            }
        }
    }

    return C;
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
    @param A Matriu a ser copiada.
    @param C Matriu a on es copia A.
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
    @brief Retorna una matriu llegida pel CEE.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @return Punter cap a la matriu llegida.
 */
float **llegir_matriu(int n, int m)
{
    int i = 0, j = 0;
    float **M = matriu(n, m);

    if ( M != NULL )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            for ( j = 0 ; j < m ; j++ )
            {
                scanf("%f", &M[i][j]);
            }
        }
    }

    return M;
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
    @brief Retorna una matriu llegida des d'un fitxer.

    Si la ruta del fitxer no existeix, aleshores es retornarà NULL.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @param path Ruta cap al fitxer a ser llegit.
    @return Punter cap a la matriu llegida o NULL.
 */
float **llegir_matriu_fitxer(int n, int m, char *path)
{
    int i = 0, j = 0;
    float **r = matriu(n, m);
    FILE *handle = fopen(path, "r");

    if ( handle != NULL && r != NULL )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            for ( j = 0 ; j < m ; j++ )
            {
                fscanf(handle, "%f", &r[i][j]);
            }
        }
    }

    return r;
}

/**
    @brief Retorna una matriu llegida des d'un fitxer.

    El fitxer llegit ha de tenir els tamanys indicats al principi, de la seguent
    manera:

    [nombre_de_files] [nombre_de_columnes] [valors_matriu]

    @param path Ruta cap al fitxer a ser llegit.
    @return Punter cap a la matriu llegida o NULL.
 */
float **llegir_matriu_generica_fitxer(char *path)
{
    int i = 0, j = 0, n = 0, m = 0;
    float **r = NULL;
    FILE *handle = NULL;
    
    handle = fopen(path, "r");
    if ( handle != NULL )
    {
        fscanf(handle, "%d %d", &n, &m);

        r = matriu(n, m);
        if ( r != NULL )
        {
            for ( i = 0 ; i < n ; i++ )
            {
                for ( j = 0 ; j < m ; j++ )
                {
                    fscanf(handle, "%f", &r[i][j]);
                }
            }
        }
    }

    return r;
}

/**
    @brief Escriu el contingut d'una matriu pel CES.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @param M Matriu a ser escrita.
 */
void escriure_matriu(int n, int m, float **M)
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
    @brief Retorna la matriu transposada d'una matriu donada.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @param M Matriu a ser transposada.
    @return Punter de la matriu transposada.
 */
float **transposada(int n, int m, float **M)
{
    int i = 0, j = 0;
    float **T = matriu(m, n);

    for ( i = 0 ; i < n ; i++ )
    {
        for ( j = 0 ; j < m ; j++ )
        {
            M[i][j] = T[j][i];
        }
    }

    return T;
}

/**
    @brief Retorna la matriu transposada d'una matriu donada.

    Aquesta operació manipula matrius de coma flotant de precisió doble.

    @param n Nombre de files de la matriu.
    @param m Nombre de columnes de la matriu.
    @param M Matriu a ser transposada.
    @return Punter de la matriu transposada.
 */
double **transposada_d(int n, int m, double **M)
{
    int i = 0, j = 0;
    double **T = matriu_d(m, n);

    for ( i = 0 ; i < n ; i++ )
    {
        for ( j = 0 ; j < m ; j++ )
        {
            M[i][j] = T[j][i];
        }
    }

    return T;
}

/**
    @brief Intercanvia els valors de dues files de la matriu.

    @param m Nombre de columnes de la matriu.
    @param r_o Fila a intercanviar.
    @param r_c Fila a intercanviar.
    @param M Matriu.
 */
void intercanviar_fila(int m, int r_o, int r_c, float **M)
{
    int i = 0;
    float aux = 0.f;

    for ( ; i < m ; i++ )
    {
        aux = M[r_o][i];
        M[r_o][i] = M[r_c][i];
        M[r_c][i] = aux;
    }
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
    @brief Allibera la matriu donada de la memòria.

    @param n Nombre de files de la matriu.
    @param M Matriu.
 */
void alliberar_matriu(int n, float **M)
{
    int i = 0;
    for ( i = 0 ; i < n ; i++ )
        free(M[i]);
    free(M);
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
