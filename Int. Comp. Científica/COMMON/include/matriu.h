#ifndef _MATRIX_H_
#define _MATRIX_H_

float **matriu(int, int);
double **matriu_d(int, int);

float **copia_matriu(int, int, float **);
double **copia_matriu_d(int, int, double **);
void copiar_en_matriu_d(int, int, double **, double **); /* INVASIU */

float **llegir_matriu(int, int);
double **llegir_matriu_d(int, int);
float **llegir_matriu_fitxer(int, int, char *);
float **llegir_matriu_generica_fitxer(char *);

void escriure_matriu(int, int, float **);
void escriure_matriu_d(int, int, double **);

float **transposada(int, int, float **);
double **transposada_d(int, int, double **);

void transposar(int, int, float **); /* IMPLEMENTAR! */
void transposar_d(int, int, double **); /* IMPLEMENTAR! */

void intercanviar_columna(int, int, int, float **); /* IMPLEMENTAR! */
void intercanviar_fila(int, int, int, float **);
void intercanviar_columna_d(int, int, int, double **); /* IMPLEMENTAR! */
void intercanviar_fila_d(int, int, int, double **);

void alliberar_matriu(int, float **);
void alliberar_matriu_d(int, double **);

#endif
