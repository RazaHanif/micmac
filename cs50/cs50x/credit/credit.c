#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

string card_check(void);
bool lunhs(long card);

// only runs card_check in main to prompt abstraction
int main(void)
{
    printf("%s\n", card_check());
}


// checks if card length is valid and assigns type, then calls on lunhs() function to check validity of card number
string card_check(void)
{
    long cardNum = get_long("Number: ");
    long num = 0;
    string cardType = "INVALID";

    // if card num is less than 13 or greater than 16 it is invalid and program exits
    if (cardNum < (pow(10, 12) - 1) || cardNum > pow(10, 16))
    {
        return "INVALID";
    }

    // checks card type based on length and starting digits and assigns a card type
    if (cardNum < pow(10, 13) && cardNum > (pow(10, 12) - 1))
    {
        num = cardNum / pow(10, 12);
        if (num == 4)
        {
            cardType = "VISA";
        }
    }
    else if (cardNum < pow(10, 15) && cardNum > (pow(10, 14) - 1))
    {
        num = cardNum / pow(10, 13);
        if (num == 34 || num == 37)
        {
            cardType = "AMEX";
        }
    }
    else if (cardNum < pow(10, 16) && cardNum > (pow(10, 15) - 1))
    {
        num = cardNum / pow(10, 14);
        if (num >= 51 && num <= 55)
        {
            cardType = "MASTERCARD";
        }
        else
        {
            num /= 10;
            if (num == 4)
            {
                cardType = "VISA";
            }
        }
    }
    // if card length is valid but no starting value is correct then card is invalid
    else
    {
        cardType = "INVALID";
    }
    // calls on lunhs function to check if card num is valid, if valid returns card type to console, otherwise returns invalid
    if (lunhs(cardNum))
    {
        return cardType;
    }
    else
    {
        return "INVALID";
    }
}

// function checks if lunhs algo is correct
bool lunhs(long card)
{
    long cardNum = card;
    long temp = cardNum;
    long num = 0;
    long value = 0;
    long total = 0;

    // first portion of check, gets sum of digits from every second number from the end multiplied by 2
    do
    {
        temp = cardNum % 100;
        num = trunc(temp / 10) * 2;
        if (num > 9)
        {
            value += (num % 10);
            value += trunc(num / 10);
        }
        else
        {
            value += num;
        }
        cardNum /= 100;
    }
    while (cardNum > 0);

    // Reset values to use again
    cardNum = card;
    temp = cardNum;
    num = 0;

    // gets sum of remaining values
    do
    {
        temp = cardNum % 10;
        total += temp;
        cardNum /= 100;
    }
    while (cardNum > 0);

    // checks if algo is true and returns result
    total += value;
    if (total % 10 == 0)
    {
        return true;
    }
    // else
    return false;


}