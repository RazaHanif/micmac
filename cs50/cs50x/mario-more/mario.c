#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_pyramid(int num);

int main(void)
{
    // Get size of pyramid
    int n = get_size();

    // Build pyramid
    print_pyramid(n);
}



// Gets input from user, value must be int 1-8
int get_size(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    return n;
}

// Prints out pyramid
void print_pyramid(int num)
{
    int count;

    for (int i = 0; i < num; i++)
    {
        // Making the pyramid right aligned
        count = (num - (i + 1));
        while (count > 0)
        {
            printf(" ");
            count -= 1;
        }
        // First pyramid
        for (int j = 0; j < (i + 1); j++)
        {
            printf("#");
        }

        //Space inbetween
        printf("  ");

        // Second pyramid
        for (int k = 0; k < (i + 1); k++)
        {
            printf("#");
        }
        printf("\n");
    }

}
