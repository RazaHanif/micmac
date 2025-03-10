#include <stdio.h>

int main(void)
{
    int x;
    printf("X: ");
    scanf("%i", &x);
    printf("X is %i\n", x);

    char *s = NULL;
    printf("S: ");
    scanf("%s", s);
    printf("S is %s\n", s);
}