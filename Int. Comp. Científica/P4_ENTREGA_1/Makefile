clean:
	del *.o *.exe *.res

clean_u:
	rm *.exe *.o

1.a: clean triangular
	type inputs\p1_a_3.in | triangular

1.b: clean triangular
	type inputs\p1_b_3.in | triangular

1.a_u: clean_u triangular
	cat inputs/p1_c.in | ./triangular.exe

2.a_u: gauss
	cat inputs/p2_a_3.in | ./gauss.exe

2.b_u: gauss
	cat inputs/p2_b_3.in | ./gauss.exe

3.a_u: pivot
	cat inputs/p2_a_3.in | ./pivot.exe

pr27: pivot
	cat inputs/problema_27.in | ./pivot.exe	

compile: triangular gauss pivot

triangular:
	gcc -c -g triangular.c -ansi -pedantic -O -Wall -Wno-unused-result
	gcc triangular.o ../COMMON/lib/algebra_lineal.o ../COMMON/lib/matriu.o ../COMMON/lib/vector.o -o triangular.exe -lm

gauss:
	gcc -c -g gauss.c -ansi -pedantic -O -Wall -Wno-unused-result
	gcc gauss.o ../COMMON/lib/algebra_lineal.o ../COMMON/lib/matriu.o ../COMMON/lib/vector.o -o gauss.exe -lm

pivot:
	gcc -c -g pivot.c -ansi -pedantic -O -Wall -Wno-unused-result
	gcc pivot.o ../COMMON/lib/algebra_lineal.o ../COMMON/lib/matriu.o ../COMMON/lib/vector.o -o pivot.exe -lm