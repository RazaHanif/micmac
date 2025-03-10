#include <stdio.h>

int main(void)
{
    // bug in code where i <= 3, in for loop i should only be less than
    for (int i =0; i <= 3; i++)
    {
        printf("#\n");
    }
}
