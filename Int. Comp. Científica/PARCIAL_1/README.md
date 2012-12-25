# Anotacions del parcial:

Hi ha un error a la línea 214 de la implementació presentada:

```
if ( A[l_][k] > A[l_max][k] )
```

Aquesta comprobació deuria de ser amb els valors absoluts dels dos elements
de la fila a ser comprobats. Per tant, deuria de quedar algo com a:

```
if ( fabs(A[l_][k]) > fabs(A[l_max][k]) )
```

Això està corregit a la llibreria.

A més, la resolució correcte és al fitxer `resolucio-exercici-practica1.c`.
