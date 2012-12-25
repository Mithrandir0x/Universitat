#ifndef _ALGEBRA_LINEAL_H_
#define _ALGEBRA_LINEAL_H_

#include "common.h"

float *producte_matriu_vector(int, int, float **, float *);
double *producte_matriu_vector_d(int, int, double **, double *);
float **producte_matriu_matriu(int, int, int, float **, float **);

float **descompon_lu(int, int, float **, float **, float**); /* IMPLEMENTAR! */
double **descompon_lu_d(int, int, double **, double **, double**); /* IMPLEMENTAR! */

double verificar_resolucio_sistema(int, int, double **, double *, double *);

int resol_sistema_lineal_triangular_simple(int, float **, float *, float *, float);
int resol_sistema_lineal_triangular_simple_d(int, double **, double *, double *, double);

int gauss_d(int, double **, double *, double);
int gauss_pivotatge_maxim_d(int, double **, double *, double);

double sarrus_d(double **);

#endif
