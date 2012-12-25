/* exercici-practica1.c */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double determinant (int, double **, double);

int main(void) {
   double **a, tol=1.e-10;
   int i, j, n=8;

   a = (double **)malloc( n*sizeof(double *) );
   if ( a==NULL) exit(1);
   for(i=0; i<n; i++) {
      a[i]= (double *)malloc( n*sizeof(double) );
      if ( a[i]==NULL) exit(1);
   }
   /* omplim la matriu i l'escrivim */	
   for(i=1; i<n; i++) {
      for(j=0; j<n; j++) a[i][j]=fabs(i-j);
   }
   printf(" entra el niub separant els dígits \n");
   for(j=0; j<n; j++)  scanf("%le", &a[0][j]);
   
   printf("matriu inicial:\n");
   for(i=0; i<n; i++) {
      for(j=0; j<n; j++) printf(" %3d ", (int)a[i][j]);
      printf("\n");
   }
   /* càlcul i escriptura del determinant */
   printf("det = %+.12le \n", determinant(n, a, tol));

   printf("/*matriu final:\n");
   for(i=0; i<n; i++) {
      for(j=0; j<n; j++) printf(" %3d ", (int)a[i][j]);
      printf("\n");
   }

   for (i=0; i<n; i++) free (a[i]);
   free (a);

   return 0;
}
			
double determinant(int n, double **a, double tol) {
   double amax, *aux, f, det=1.e0;
   int i, j, k, imax, cont=0;
   /* imax indica la fila on hi ha l'element màxim */
   for (k=0; k<n-1; k++) { /* k: columna d'eliminació */
      /* cerca del màxim en valor absolut */
      amax = fabs(a[k][k]);
      imax = k;
      for (i=k+1; i<n; i++) {
         if (fabs(a[i][k]) > amax) {
            amax = fabs(a[i][k]);
            imax = i;
         }
      }
      /* si el màxim és 0 llavors el determinant és 0 */
      if (amax < tol ) return 0.e0 ;
      /* Cas d'haver d'intercanviar files */
      if (imax != k) {
         printf("intercanvi de les files %d i %d \n", k, imax);
         /* comptem la quantitat d'intercanvis i
            actualitzem el determinant */
         cont = cont+1;
         det = -det;
         /* permutem els apuntadors a fila */
         aux = a[k];
         a[k] = a[imax];
         a[imax] = aux;
      }
      /* procés d'eliminació (no posem els zeros) */
      for (i=k+1; i<n; i++){
         f = a[i][k]/a[k][k];
         for (j=k+1; j<n; j++)
            a[i][j] = a[i][j]-f*a[k][j];  
      }
   }
   /* condició de determinant 0 degut a l'últim element */
   if (fabs(a[n-1][n-1]) < tol) return 0.e0;
   /* det = (+-1) * producte d'elements diagonals */
   for (i=0; i<n; i++) det = det*a[i][i];
   printf("cont = %d \n", cont);

   return det;
}

