#include <stdio.h>

int main(void)
{
    int amount, num20, num10, num5, num;
    #define DOLLAR20 20
    #define DOLLAR10 10
    #define DOLLAR5 5
    #define DOLLAR 1

    printf("Enter a dollar amount: ");
    scanf("%d", &amount);
    num20 = amount / DOLLAR20;
    num10 = (amount - num20 * 20) / DOLLAR10;
    num5 = (amount - num20 * 20 - num10 * 10) / DOLLAR5;
    num = amount - num20 * 20 - num10 * 10 - num5 * 5;
    printf("$20 bills: %d \n", num20);
    printf("$10 bills: %d \n", num10);
    printf("$5 bills: %d \n", num5);
    printf("$1 bills: %d \n", num);
    return 0;
}