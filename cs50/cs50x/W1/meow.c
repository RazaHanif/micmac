#include <stdio.h>

#include <cs50.h>

int main(void)
{
    //Get input from user
    int n = get_int("How many times should the cat meow? ");
    int x = get_int("How many times should the dog bark? ");
    int count = 0;

    //Use while loop to run function
    while (count < n)
    {
        printf("meow\n");
        count++;
    }

    for (int i = 0; i < x; i++)
    {
        printf("woof\n");
    }


}