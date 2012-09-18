# Anotacions d'aquesta pràctica:

El `Makefile` està fet per Windows. Pedrades en 3... 2... 1...

Comandes disponibles (apart de `make clean` i `make all`):

`make ex2` Compila l'executable del segón exercici i a més, genera els fitxers
necessaris per ser visualitzats a gnuplot.

`make test_ex2_double` Compila l'executable del segón exercici, però en comptes
d'utilitzar nombres en coma flotant simple, utilitza coma flotant doble. També
genera els fitxers necessaris per visualitzar a gnuplot.

`make epsilon` Compila l'executable per calcular l'epsilon de la màquina per
`float`s i `double`s.

Per veure les gràfiques a gnuplot, s'ha d'executar la següent comanda:

```
plot 'f1103.res' u 1:(log10($2)) w l, 'f11+03.res' u 1:(log10($2)) w l, 'f11-03.res' u 1:(log10($2)) w l, 'f1103+.res' u 1:(log10($2)) w l, 'f1103-.res' u 1:(log10($2)) w l
```

Per últim, una petita comparativa entre els diferents errors de càlcul propagat
pel tipus de dada emprada:

`40 iteracions, amb float`
![40 iteracions, amb float](https://dl.dropbox.com/u/9123154/cdn/uni/ICC_P1_P2_Plot.png)

`40 iteracions, amb double`
![40 iteracions, amb double](https://dl.dropbox.com/u/9123154/cdn/uni/ICC_P1_P2_Plot_40_Double.png)

`60 iteracions, amb double`
![60 iteracions, amb double](https://dl.dropbox.com/u/9123154/cdn/uni/ICC_P1_P2_Plot_60_Double.png)
