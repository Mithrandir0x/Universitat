/*
 */

int main(void)
{
    int n, m, p;
    float **A = NULL, **B = NULL, **C = NULL, **D = NULL;

    scanf("%d %d %d", &n, &m, &p);

    A = llegir_matriu(n, p);
    B = llegir_matriu(p, m);

    C = producte_matriu_matriu(n, p, p, m, A, B);
    D = producte_matriu_matriu(p, m, n, p, B, A); /* D sera NULL! */

    return 0;
}
