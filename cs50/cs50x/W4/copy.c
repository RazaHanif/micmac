#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    string s = get_string("S: ");

    string t = malloc(strlen(s) + 1);

    // strlen(s) + 1 to get the null character at end of string
    for (int i = 0; i < strlen(s) + 1; i++)
    {
        t[i] = s[i];
    }

    // OR  strcpy(t, s);

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);
}