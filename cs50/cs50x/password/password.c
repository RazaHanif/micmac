// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    string check = password;
    int x = strlen(check);
    bool lower = false;
    bool upper = false;
    bool number = false;
    bool special = false;


    for (int i = 0; i < x; i++)
    {
        if (check[i] >= 'a' && check[i] <= 'z')
        {
            lower = true;
        }
        if (check[i] >= 'A' && check[i] <= 'Z')
        {
            upper = true;
        }
        if (check[i] >= '0' && check[i] <= '9')
        {
            number = true;
        }
        if (check[i] >= 21 && check[i] <= 47)
        {
            special = true;
        }
        if (check[i] >= 58 && check[i] <= 64)
        {
            special = true;
        }
        if (check[i] >= 91 && check[i] <= 96)
        {
            special = true;
        }
        if (check[i] >= 123 && check[i] <= 126)
        {
            special = true;
        }

    }

    if (upper && lower && number && special)
    {
        return true;
    }

    return false;
}
