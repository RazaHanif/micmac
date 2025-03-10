#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Asking user for input and printing out message
    string name = get_string("What is your name? ");
    printf("Hello, %s\n", name);
}