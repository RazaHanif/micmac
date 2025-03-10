#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string i = get_string("i: ");
    string j = get_string("j: ");

    if (strcmp(i, j) == 0)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}