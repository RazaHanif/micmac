#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string name = get_string("Whats your name? ");

    int n = 0;
    while (name[n] != '\0')
    {
        n++;
    }

    // or instead of all that

    int x = strlen(name);

    printf("Your name %s is %i letters long\n", name, n);
    printf("Your name %s is %i letters long\n", name, x);
}
