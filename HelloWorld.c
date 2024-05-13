#include <stdio.h>
#include <stdlib.h>



int Echanger(int l[], int a, int b) {
    int c = l[a];
    l[a] = l[b];
    l[b] = c ;
    return EXIT_SUCCESS ;
}
void commande(bool C[], bool E[], bool P[], bool D[], int n) {
    for (int i = 0; i < n; i++) {
        if (E[i] == false || P[i] == false || D[i] == false) {
            C[i] = false ;
        } else {
        C[i] = true ;
        }
    }
}


int main(void) {
    printf("Hello, World!\n");
    int tab[4]= {1,2,5,4} ;
    Echanger(tab, 1, 2);
    for (int i = 0; i < 4 ; i++) {
        printf("%d",tab[i]);
    }
    bool C[3];
    bool E[3] = {false, true, true};
    bool P[3] = {true, true, false};
    bool D[3] = {false, true, false};
    int n = 3;
    commande(C, E, P, D, n) ;
    for (int i = 0; i < 3 ; i++) {
        printf("\n%d",C[i]);
    }
    return EXIT_SUCCESS;
}

