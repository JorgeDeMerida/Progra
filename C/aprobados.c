#include <stdio.h>

int main(void)
{
    float suspensos, aprobados, notables, sobresalientes, total_alumnos;
    float porcentaje_sus, porcentaje_aprob, porcentaje_notables, porcentaje_sobresalientes;

    printf("Numero de suspensos: ");
    scanf("%d", &suspensos);
    printf("Numero de aprobados: ");
    scanf("%d", &aprobados);
    printf("Numero de notables: ");
    scanf("%d", &notables);
    printf("Numero de sobresalientes: ");
    scanf("%d", &sobresalientes);

    total_alumnos = suspensos + aprobados + notables + sobresalientes;

    printf("Han superado la asignatura %.2f%%\n", (total_alumnos - suspensos) / total_alumnos * 100);    
    printf("Han suspendido la asignatura el %.2f%%\n", suspensos / total_alumnos * 100);
    printf("Han aprobado la asignatura el %.2f%%\n", aprobados / total_alumnos * 100);
    printf("Han sido notables el %.2f%%\n", notables / total_alumnos * 100);
    printf("Han sido sobresalientes el %.2f%%\n", sobresalientes / total_alumnos * 100);
    
}