#include <stdio.h>
#include <cs50.h>

int get_size(void);
void print_grid(int num);

int main(void)
{
    //Get size of grid
    int n = get_size();

    //Produce the grid
    print_grid(n);
}




int get_size(void)
{
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1);
    return n;
}

void print_grid(int num)
{
    for (int i = 0; i < num; i++)
    {
        for (int k = 0; k < num; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}
