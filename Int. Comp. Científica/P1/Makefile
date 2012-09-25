clean:
	del *.o *.exe *.res

all: clean p1.exe p2.exe p2_double.exe p3.exe

epsilon: clean p3.exe
	p3

ex2: clean p2.exe
	type inputs\f1103.in | p2 > f1103.res
	type inputs\f11+03.in | p2 > f11+03.res
	type inputs\f11-03.in | p2 > f11-03.res
	type inputs\f1103+.in | p2 > f1103+.res
	type inputs\f1103-.in | p2 > f1103-.res

test_ex2_double: clean p2_double.exe
	type inputs\f1103.in | p2_double > f1103.res
	type inputs\f11+03.in | p2_double > f11+03.res
	type inputs\f11-03.in | p2_double > f11-03.res
	type inputs\f1103+.in | p2_double > f1103+.res
	type inputs\f1103-.in | p2_double > f1103-.res

# Commands used in GnuPlot:
# plot 'f1103.res' u 1:(log10($2)) w l, 'f11+03.res' u 1:(log10($2)) w l, 'f11-03.res' u 1:(log10($2)) w l, 'f1103+.res' u 1:(log10($2)) w l, 'f1103-.res' u 1:(log10($2)) w l

p3.exe: p3.o
	gcc p3.o -o p3.exe -lm

p3.o: p3.c
	gcc -c p3.c -ansi -pedantic -O -Wall

p2_double.exe: p2_double.o
	gcc p2_double.o -o p2_double.exe -lm

p2_double.o: p2_double.c
	gcc -c p2_double.c -ansi -pedantic -O -Wall

p2.exe: p2.o
	gcc p2.o -o p2.exe -lm

p2.o: p2.c
	gcc -c p2.c -ansi -pedantic -O -Wall

p1.exe: p1.o
	gcc p1.o -o p1.exe -lm

p1.o: p1.c
	gcc -c p1.c -ansi -pedantic -O -Wall
