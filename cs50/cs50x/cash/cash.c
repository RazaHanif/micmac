#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    // Asks user for inital value
    int change;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 0);
    return change;
}

int calculate_quarters(int cents)
{
    int change = cents;
    int count = 0;

    if (cents >= 25)
    {
        do
        {
            change -= 25;
            count++;
        }
        while (change >= 25);
    }
    else
    {
        count = 0;
    }

    printf("25: %i\n", count);
    return count;
}

int calculate_dimes(int cents)
{
    int change = cents;
    int count = 0;

    if (cents >= 10)
    {
        do
        {
            change -= 10;
            count++;
        }
        while (change >= 10);
    }
    else
    {
        count = 0;
    }

    printf("10: %i\n", count);
    return count;
}

int calculate_nickels(int cents)
{
    int change = cents;
    int count = 0;

    if (cents >= 5)
    {
        do
        {
            change -= 5;
            count++;
        }
        while (change >= 5);
    }
    else
    {
        count = 0;
    }

    printf("05: %i\n", count);
    return count;
}

int calculate_pennies(int cents)
{
    int change = cents;
    int count = 0;


    if (cents >= 1)
    {
        do
        {
            change -= 1;
            count++;
        }
        while (change >= 1);
    }
    else
    {
        count = 0;
    }

    printf("01: %i\n", count);
    return count;
}
