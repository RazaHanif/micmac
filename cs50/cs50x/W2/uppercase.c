#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After: :");

    for (int i = 0; i < strlen(s); i++)
    {
        /* if (s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c", s[i] - 32);
        }
        else printf("%c", s[i]); */

        printf("%c", toupper(s[i]));
    }
    printf("\n");
}