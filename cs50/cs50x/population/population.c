#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Start program
    printf("Population Growth Program.\n");

    //Prompt for start size, min 9
    int start;
    do
    {
        start = get_int("What is the starting size? ");
    }
    while (start < 9);

    //Prompt for end size, greaterThan start size
    int end;
    do
    {
        end = get_int("What is the ending size? ");
    }
    while (end < start);



    //Calculate number of years until we reach threshold
    int population = start;
    int born;
    int died;
    int years = 0;

    do
    {
        born = population / 3;
        died = population / 4;
        population = population + born - died;

        years++;
    }
    while (population < end);

    if (end == start)
    {
        years = 0;
    }

    //Print number of years
    printf("Years: %i\n", years);
}
