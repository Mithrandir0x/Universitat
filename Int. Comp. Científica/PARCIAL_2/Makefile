clean:
	rm *.exe *.o

ex: clean B-LopezSanchezOriol-E2
	./B-LopezSanchezOriol-E2.exe

compile: B-LopezSanchezOriol-E2

B-LopezSanchezOriol-E2:
	gcc -c -g B-LopezSanchezOriol-E2.c -ansi -pedantic -O -Wall -Wno-unused-result
	gcc B-LopezSanchezOriol-E2.o -o B-LopezSanchezOriol-E2.exe -lm
