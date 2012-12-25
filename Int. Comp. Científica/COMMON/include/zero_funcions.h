#ifndef _ZERO_FUNCIONS_H_
#define _ZERO_FUNCIONS_H_

#include "common.h"

float horner(int, float, float *);
double horner_d(int, double, double *);

int newton(float, float *, M_F_PTR, M_F_PTR, float, int); /* IMPLEMENTAR */
int newton_d(double, double *, M_F_PTR_D, M_F_PTR_D, double, int);
int newton_multiple_d(int, double *, double *, M_F_GEN_PTR_D, M_DF_GEN_PTR_D, double, int);

double *producte_polinomis_d(int, int, double *, double *);
double *derivar_coeficients_polinomi_d(int, double *);
/* double m_polinomi_d(int n, double *P);
M_F_PTR_D polinomi_d(int, double *);
M_F_PTR_D polinomi_factoritzat_d(int, M_F_PTR_D); */
double *polinomi_coeficients_d(int, M_F_PTR_D);

#endif
