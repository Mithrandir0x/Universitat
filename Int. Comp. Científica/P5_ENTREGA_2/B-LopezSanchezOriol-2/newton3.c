/* LOPEZ: SANCHEZ: ORIOL: 46459536L: */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TRUE 1
#define FALSE 0
#define RESULT_OK 0
#define RESULT_ERROR 1

/**
    Macro per intercanviar valors. NO ÉS C-STANDARD!

    Aquest codi font prové de: http://rosettacode.org/wiki/Generic_swap#C
    Més informació a: http://gcc.gnu.org/onlinedocs/gcc/Typeof.html
 */
#define intercanviar(X, Y) do { \
            __typeof__ (X) _T = X; \
            X = Y; \
            Y = _T; \
        } while(0)

/**
    Definició de tipus de punter de funció matemàtica de diverses variables.

    Qualsevol funció matemàtica expressada per \f$y = f(x), x = { x_0, x_1, x_2, ... , x_n }, x \in N\f$, es
    pot referenciar utilitzant aquesta definició de punter.

    Aquest component utilitza dades en coma flotant de precisió doble.
 */
typedef void (*M_F_GEN_PTR_D)(double *, double *);

/**
    Definició de tipus de punter de funció matemàtica derivada d'una altra funció de diverses variables.

    
 */
typedef void (*M_DF_GEN_PTR_D)(double *, double **);

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

    copiar_en_vector_d(r, x, xn1);
    maxIteracions--;

    while ( TRUE )
    {
        f(x, f_x);
        df(x, df_x);

        if ( i > maxIteracions )
        {
            printf("S'ha asolit el màxim d'iteracions permeses.\n");
            break;
        }

        if ( gauss_pivotatge_maxim_d(r, df_x, f_x, tol) == RESULT_OK )
        {
            if ( resol_sistema_lineal_triangular_simple_d(r, df_x, f_x, ax, tol) == RESULT_OK )
            {
                restar_en_vector_d(r, xn1, ax);
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

void S0(double *x, double *y)
{
    y[0] = x[0] + x[1] + x[2] - 1;
    y[1] = x[1] + x[2];
    y[2] = ( x[0] * x[0] ) + ( 0.75 * x[1] );
}

void D_S0(double *x, double **y)
{
    y[0][0] = 1;
    y[0][1] = 1;
    y[0][2] = 1;

    y[1][0] = 0;
    y[1][1] = 1;
    y[1][2] = 1;

    y[2][0] = 2 * x[0];
    y[2][1] = 0.75;
    y[2][2] = 0;
}

void S1(double *x, double *y)
{
    y[0] = ( x[0] * x[0] ) + ( x[1] * x[1] ) + ( x[2] * x[2] ) - 1;
    y[1] = ( 0.25 * ( x[0] - x[1] ) * ( x[0] - x[1] ) ) + ( ( x[0] + x[1] ) * ( x[0] + x[1] ) ) + ( x[2] * x[2] ) - 1;
    y[2] = ( ( x[0] - x[1] ) * ( x[0] - x[1] ) ) + ( ( x[0] + x[1] ) * ( x[0] + x[1] ) ) + ( 0.25 * x[2] * x[2] ) - 1;
}

void D_S1(double *x, double **y)
{
    y[0][0] = 2 * x[0];
    y[0][1] = 2 * x[1];
    y[0][2] = 2 * x[2];

    y[1][0] = ( 0.5 * ( x[0] - x[1] ) ) + ( 2 * ( x[0] + x[1] ) );
    y[1][1] = ( 0.5 * ( x[0] - x[1] ) ) + ( 2 * ( x[0] + x[1] ) );
    y[1][2] = 2 * x[2];

    y[2][0] = ( 2 * ( x[0] - x[1] ) ) + ( 2 * ( x[0] + x[1] ) );
    y[2][1] = ( 2 * ( x[0] - x[1] ) ) + ( 2 * ( x[0] + x[1] ) );
    y[2][2] = 0.5 * x[2];
}

int main()
{
    int i = 0, j = 0, k = 100, maxIteracions = 50;
    double q_a = -1, q_b = 1, tolerancia = 1E-10, q_a_b = 0, RAND_MAX_D = 0;
    double *x0 = NULL, *zero = NULL;

    M_F_GEN_PTR_D sistemes[2] = {
        &S0,
        &S1
    };

    M_DF_GEN_PTR_D derivades_sistemes[2] = {
        &D_S0,
        &D_S1
    };

    scanf("%d %d %lf", &maxIteracions, &k, &tolerancia);

    x0 = vector_d(3);
    zero = vector_d(3);

    srand(time(NULL));
    RAND_MAX_D = (double) RAND_MAX;
    q_a_b = q_b - q_a;

    for ( i = 0 ; i < 2 ; i++ )
    {
        for ( j = 0 ; j < k ; j++ )
        {
            x0[0] = q_a + ( ( (double) rand() / RAND_MAX_D ) * ( q_a_b ) );
            x0[1] = q_a + ( ( (double) rand() / RAND_MAX_D ) * ( q_a_b ) );
            x0[2] = q_a + ( ( (double) rand() / RAND_MAX_D ) * ( q_a_b ) );

            printf("(%3.14e, %3.14e, %3.14e)", x0[0], x0[1], x0[2]);

            if ( newton_multiple_d(3, x0, zero, sistemes[i], derivades_sistemes[i], tolerancia, maxIteracions) == RESULT_OK )
            {
                printf(" -> (%3.10e, %3.10e, %3.10e)\n", zero[0], zero[1], zero[2]);
            }
            else
            {
                printf(" -> NULL\n");
            }
        }
    }

    free(x0);
    free(zero);

    return 0;
}
