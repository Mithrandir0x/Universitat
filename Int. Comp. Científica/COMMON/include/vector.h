#ifndef _VECTOR_H_
#define _VECTOR_H_

float *vector(int);
double *vector_d(int);

float *copia_vector(int, float *);
double *copia_vector_d(int, double *);
void copiar_en_vector_d(int, double *, double *); /* INVASIU */

float *llegir_vector(int);
float *llegir_vector_fitxer(int, char *);
double *llegir_vector_d(int);
double *llegir_vector_fitxer_d(int, char *);

void escriure_vector(int, float *);
void escriure_vector_d(int, double *);

float producte_escalar(int, float *, float*);
double producte_escalar_d(int, double *, double*); /* IMPLEMENTAR */

float modul_vector(int, float*);
double modul_vector_d(int, double *);

int es_ortogonal(int, float, float *, float *);
int es_ortogonal_d(int, double, double *, double *); /* IMPLEMENTAR */

float *resta_vector(int, float *, float *); /* IMPLEMENTAR */
double *resta_vector_d(int, double *, double *);

void restar_en_vector_d(int, double *, double *);

#endif
