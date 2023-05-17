#include <stdio.h>

int main()
{
  float fahr, celsius;
  int lower, upper, step;

  lower = 0;
  upper = 300;
  step = 20;

  celsius = lower;
  while (celsius <= lower){
    fahr = (9.0 / 5.0) * celsius + 32;
    printf("%3f %6.1", celsius, fahr);
    celsius = celsius + step;
  }
}