// #include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("int pointer %p\n", p);
    printf("pointer value %i\n", *p);
    printf("\n");

    char *s = "HI!";
    printf("String pointer %p\n", s);
    printf("String value %s\n", s);
    printf("\n");

    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
}