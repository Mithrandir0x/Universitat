
typedef double (*M_F_PTR_D)(double);

double horner_d(int g, double x, double *P)
{
    int i = g - 1;
    double r = P[g];

    for ( ; i >= 0 ; i-- )
    {
        r = ( r * x ) + P[i];
    }
    return r;
}

M_F_PTR_D polinomi_d(int g, double *P)
{
    double p(double x)
    {
        return horner_d(g, x, P);
    }

    return &p;
}

int main()
{
    double coeficients[3] = { -1, 0, 1 };
    M_F_PTR_D P = polinomi_d(2, coeficients);

    P(0);
    P(1); /* SEGFAULT! */

    return 0;
}
