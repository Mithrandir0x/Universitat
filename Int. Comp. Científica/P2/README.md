# Anotacions d'aquesta pràctica:

Algunes de les comandes utilitzades per compilar i executar els exercicis:

`make ex1_ap_a` Compila i executa el primer apartat del primer exercici, on es
fa el càlcul d'error que hi ha al calcular nombres d'un polinomi de grau 7 amb
el mètode pico-y-pala i [Horner](http://en.wikipedia.org/wiki/Horner%27s_method).

> Utiliza com a input els fitxers `ex1_ap_a_100.in`, `ex1_ap_a_1000.in`, 
> `ex1_ap_a_10000.in`.

`make ex1_ap_bcd`, `make ex1_ap_bcd_float` Tots dos compilen i executen els
últims apartats del primer exercici. Però el primer executa amb coma flotant de
doble precissió, mentres que el segón es simple. Es fan amb 100 iteracions.

> En aquesta part s'usa el fitxer `coeficients.dad` per a especificar els
coeficients del polinomi, i s'han d'especificar a l'inversa. Sigui p(x) el
següent polinomi:

> ![](https://dl.dropbox.com/u/9123154/cdn/uni/ICC_P2_polinomi.png)

> El format del fitxer seria:

> ![](https://dl.dropbox.com/u/9123154/cdn/uni/ICC_P2_polinomi_2.png)

> El fitxer d'input utilitzat és `ex1_ap_b_100`

`make ex2_ap_a` El primer apartat del segón exercici. Càlcul del producte 
escalar de dos vectors.

> El fitxer d'input d'aquest executable és `ex2_ap_a`.

`make ex2_ap_b` Semblant a l'anterior, però demana fitxers separats per cada vector 
amb els seus valors corresponents.

> El fitxer d'input és `ex2_ap_b`, i depen de `x` i `y`.

`make tots` Compila i executa tots els programes.