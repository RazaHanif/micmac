#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string fName = get_string("What is your first name? ");
    string lName = get_string("What is your last name? ");
    printf("Hello, %s %s!\n", fName, lName);
}