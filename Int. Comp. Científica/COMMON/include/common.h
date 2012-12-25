/**
    @author olopezsa13
    @file common.h
 */

#ifndef _COMMON_H_
#define _COMMON_H_

#ifndef TRUE
/**
    Constant TRUE.
 */
#define TRUE 1
#endif

#ifndef FALSE
/**
    Constant FALSE.
 */
#define FALSE 0
#endif

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
    Definició de tipus de punter de funció matemàtica.

    Qualsevol funció matemàtica expressada per \f$y = f(x)\f$, es pot
    referenciar utilitzant aquesta definició de punter.

    Per saber més sobre punters a funcions mirar a:
        http://stackoverflow.com/questions/5488608/how-define-an-array-of-function-pointers-in-c
 */
typedef float (*M_F_PTR)(float);

/**
    Definició de tipus de punter de funció matemàtica.

    Qualsevol funció matemàtica expressada per \f$y = f(x)\f$, es pot
    referenciar utilitzant aquesta definició de punter.

    Aquesta operació utilitza dades en coma flotant de precisió doble.
 */
typedef double (*M_F_PTR_D)(double);

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

#endif
