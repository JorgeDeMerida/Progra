#include <stdio.h>

int main(void)
{
    int num_boca_jam, num_boca_queso, num_patatas, num_refrescos, num_cervezas;
    float total;

    #define COST_BOC_JAM 25
    #define COST_BOC_QUE 20
    #define COST_PATATAS 10
    #define COST_REFRESCO 17.5f
    #define COST_CERVEZA 22.5f

    printf("Ingrese el numero de bocadillos de jamon que consumio: ");
    scanf("%d", &num_boca_jam);
    printf("Ingrese el numero de bocadillos de queso que consumio: ");
    scanf("%d", &num_boca_queso);
    printf("Ingrese el numero de ordenes de patatas que consumio: ");
    scanf("%d", &num_patatas);
    printf("Ingrese el numero de refrescos que consumio: ");
    scanf("%d", &num_refrescos);
    printf("Ingrese el numero de cervazas que consumio: ");
    scanf("%d", &num_cervezas);

    total = num_boca_jam * COST_BOC_JAM + num_boca_queso * COST_BOC_QUE + num_patatas * COST_PATATAS + num_refrescos * COST_REFRESCO + num_cervezas * COST_CERVEZA;

    printf("El total es: %.2f", total);
    return 0;
}