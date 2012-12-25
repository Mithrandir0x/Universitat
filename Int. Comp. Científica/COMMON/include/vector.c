/**
    @brief Implementació d'operacions comuns per vectors.

    Aquesta llibreria compila una sèrie de funcions comunes per vectors. Hi han
    algunes funcions disponibles que permeten fer operacions tant amb flotants
    de precisió simple com doble.

    Per identificar les funcions d'àmbit 'double', només cal mirar al final del
    nom de la funció. Si té '_d', significa que funciona amb 'double's.

    @author olopezsa13
    @file vector.c
 */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "vector.h"

/**
    @brief Constructor de vector de coma flotant de precisió simple.

    @param n Nombre d'elements del vector
    @return Punter cap al vector o NULL.
 */
float *vector(int n)
{
    return (float *) malloc(n * sizeof(float));
}

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
    @brief Constructor per copia de vector de coma flotant de precisió simple.

    Si V és NULL o no hi ha suficient memòria, aleshores es retornarà un NULL.

    @param n Nombre d'elements del vector
    @param V Vector a ser copiat.
    @return Punter cap al nou vector o NULL.
 */
float *copia_vector(int n, float *V)
{
    int i = 0;
    float *C = vector(n);

    if ( C != NULL && V != NULL )
    {
        for ( ; i < n ; i++ )
        {
            C[i] = V[i];
        }
    }

    return C;
}

/**
    @brief Constructor per copia de vector de coma flotant de precisió doble.

    Si V és NULL o no hi ha suficient memòria, aleshores es retornarà un NULL.

    @param n Nombre d'elements del vector.
    @param V Vector a ser copiat.
    @return Punter cap al nou vector.
 */
double *copia_vector_d(int n, double *V)
{
    int i = 0;
    double *C = vector_d(n);

    if ( C != NULL && V != NULL )
    {
        for ( ; i < n ; i++ )
        {
            C[i] = V[i];
            /* printf("C[%d]: %15.6e | V[%d]: %15.6e\n", i, C[i], i, V[i]); */
        }
    }

    return C;
}

/**
    @brief Permet copiar el contingut d'un vector a un altre, remplaçant-lo.

    Aquesta operació manipula vectors de coma flotant de precisió doble.

    @param n Nombre d'elements dels vectors.
    @param V Vector a ser copiat.
    @param C Vector on es desa la copia.
    @return Punter cap al vector.
 */
void copiar_en_vector_d(int n, double *V, double *C)
{
    int i = 0;

    if ( V != NULL && C != NULL )
    {
        for ( ; i < n ; i++ )
        {
            C[i] = V[i];
        }
    }
}

/**
    @brief Retorna un vector a partir de les dades enviades pel CEE.

    @param n Nombre d'elements dels vectors a ser llegit.
    @return Punter cap al vector.
 */
float *llegir_vector(int n)
{
    int i = 0;
    float *v = NULL;

    v = vector(n);
    if ( v != NULL )
    {
        for ( i = 0 ; i < n ; i++ )
        {
            scanf("%f", &v[i]);
        }
    }

    return v;
}

/**
    @brief Donat un nom de fitxer, retorna un vector amb les dades llegides del fitxer.

    Si el fitxer no existeix, es retornarà NULL.

    @param n Nombre d'elements dels vectors a ser llegit.
    @param path Ruta cap al fitxer a ser llegit.
    @return Punter cap al vector.
 */
float *llegir_vector_fitxer(int n, char *path)
{
    int i = 0;
    float *v = NULL;
    FILE *handle = NULL;

    handle = fopen(path, "r");
    if ( handle != NULL )
    {
        v = vector(n);
        if ( v != NULL )
        {
            for ( i = 0 ; i < n ; i++ )
            {
                fscanf(handle, "%f", &v[i]);
            }
        }
    }
    fclose(handle);

    return v;
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
    @brief Donat un nom de fitxer, retorna un vector amb les dades llegides del fitxer.

    Si el fitxer no existeix, es retornarà NULL.

    @param n Nombre d'elements dels vectors a ser llegit.
    @param path Ruta cap al fitxer a ser llegit.
    @return Punter cap al vector.
 */
double *llegir_vector_fitxer_d(int n, char *path)
{
    int i = 0;
    double *v = NULL;
    FILE *handle = NULL;

    handle = fopen(path, "w");
    if ( handle != NULL )
    {
        v = vector_d(n);
        if ( v != NULL )
        {
            for ( i = 0 ; i < n ; i++ )
            {
                fscanf(handle, "%lf", &v[i]);
            }
        }
    }
    fclose(handle);

    return v;
}

/**
    @brief Escriu un vector pel CES.

    @param n Nombre d'elements del vector.
    @param V Vector a ser escrit.
 */
void escriure_vector(int n, float *V)
{
    int i = 0;

    for ( i = 0 ; i < n ; i++ )
        printf(" %16.7e \n", V[i]);
}

/**
    @brief Escriu un vector pel CES.

    Aquest vector té que ser de coma flotant de precisió doble.

    @param n Nombre d'elements del vector.
    @param V Vector a ser escrit.
 */
void escriure_vector_d(int n, double *V)
{
    int i = 0;

    printf("(");
    for ( i = 0 ; i < n ; i++ )
        printf(" %16.7e ", V[i]);
    printf(")\n");
}

/**
    @brief Calcula el producte escalar de dos vectors.

    El tamany de tots dos vector ha de ser el mateix.

    @param n Nombre d'elements del vector.
    @param U Vector.
    @param V Vector.
    @return Resultat del càlcul del producte escalar.
 */
float producte_escalar(int n, float *U, float *V)
{
    int i = 0;
    float r = 0.f;

    if ( U != NULL && V != NULL )
    {
        for ( ; i < n ; i++ )
        {
            r += U[i] * V[i];
        }
    }

    return r;
}

/**
    @brief Calcula el mòdul d'un vector.

    @param n Nombre d'elements del vector.
    @param V Vector a calcular el mòdul.
    @return El mòdul del vector.
 */
float modul_vector(int n, float *V)
{
    int i = 0;
    float r = 0.f;

    for ( ; i < n ; i++ )
    {
        r += V[i] * V[i];
    }
    r = sqrt(r);

    return r;
}

/**
    @brief Calcula el mòdul d'un vector.

    Aquest vector té que ser de coma flotant de precisió doble.

    @param n Nombre d'elements del vector.
    @param V Vector a calcular el mòdul.
    @return El mòdul del vector.
 */
double modul_vector_d(int n, double *V)
{
    int i = 0;
    double r = 0.f;

    for ( i = 0 ; i < n ; i++ )
    {
        r += V[i] * V[i];
    }
    r = sqrt(r);

    return r;
}

/**
    @brief Indica si dos vectors són ortogonals entre si.

    @param n Nombre d'elements del vector.
    @param tol La tolerància.
    @param U Vector.
    @param V Vector.
    @return Valor '0' si els vectors no són ortogonals o '1' si ho són.
 */
int es_ortogonal(int n, float tol, float *U, float *V)
{
    if ( U != NULL && V != NULL )
    {
        return fabs(producte_escalar(n, U, V)) < tol;
    }
    else
    {
        return 0;
    }
}

/**
    @brief Retorna un vector, resultant de fer la resta entre dos vectors.

    @param n Nombre d'elements del vector.
    @param U Vector.
    @param V Vector.
    @return Punter cap al vector resultant de la resta de dos vectors.
 */
double *resta_vector_d(int n, double *U, double *V)
{
    int i = 0;
    double *R = vector_d(n);

    if ( R != NULL && U != NULL && V != NULL )
    {
        for ( ; i < n ; i++ )
        {
            R[i] = U[i] - V[i];
        }
    }

    return R;
}

/**
    @brief Resta el vector V a U.

    @param n Tamany del vector
    @param U Vector que restar.
    @param V Vector qui resta.
 */
void restar_en_vector_d(int n, double *U, double *V)
{
    int i = 0;

    if ( U != NULL && V != NULL )
    {
        for ( ; i < n ; i++ )
        {
            U[i] = U[i] - V[i];
        }
    }
}
