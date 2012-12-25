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
    Macro per intercanviar valors. NO ÉS C-STANDARD!

    Nota: El fet d'utilitzar un do-while és per permetre declaracions de macros
    amb múltiples líneas de codi.

    Aquest codi font prové de: http://rosettacode.org/wiki/Generic_swap#C
 */
#define intercanviar(X, Y) do { \
            __typeof__ (X) _T = X; \
            X = Y; \
            Y = _T; \
        } while(0)

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
    @brief Permet copiar el contingut d'un vector a un altre, remplaçant-lo.

    Aquesta operació manipula vectors de coma flotant de precisió doble.

    @param n Nombre d'elements dels vectors.
    @param V Vector a ser copiat.
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
    @brief Retorna el vector resultant de la multiplicació d'una matriu amb un vector.

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
                if ( A[l_][k] > A[l_max][k] )
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

int main(void)
{
    int n = 0;
    double tolerancia = 0.f, mod = -1.0f;
    double **A = NULL, *B = NULL, *x = NULL;
    double **c_A = NULL, *c_B = NULL;

    scanf("%d %lf", &n, &tolerancia);
    A = llegir_matriu_d(n, n);
    B = llegir_vector_d(n);
    x = vector_d(n);

    c_A = copia_matriu_d(n, n, A);
    c_B = copia_vector_d(n, B);

    printf("A:\n");
    escriure_matriu_d(n, n, A);

    printf("\nB:\n");
    escriure_vector_d(n, B);

    if ( A != NULL && B != NULL && x != NULL )
    {
        if ( gauss_pivotatge_maxim_d(n, A, B, tolerancia) == RESULT_OK )
        {
            printf("\nA:\n");
            escriure_matriu_d(n, n, A);

            printf("\nB:\n");
            escriure_vector_d(n, B);

            if ( resol_sistema_lineal_triangular_simple_d(n, A, B, x, tolerancia) == RESULT_OK )
            {
                printf("\nX:\n");
                escriure_vector_d(n, x);

                mod = verificar_resolucio_sistema(n, n, c_A, x, c_B);

                printf("\nModerador: %15.e\n", mod);
            }
            else
            {
                printf("Hi ha hagut un problema alhora de calcular les solucions del sistema triangular, despres de fer Gauss.\n");
            }
        }
        else
        {
            printf("Hi ha hagut un problema alhora de fer gauss amb pivotatge de maxims amb la matriu proposada.\n");
        }
    }

    alliberar_matriu_d(n, A);
    alliberar_matriu_d(n, c_A);
    free(B);
    free(c_B);
    free(x);

    return 0;
}
