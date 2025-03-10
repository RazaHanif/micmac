#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
void convert(long number);

int main(void)
{
    // Get input from user, and get individual ascii values
    string s = get_string("Message: ");
    int slen = strlen(s);
    char x;
    long num;

    // iterate through string and run function on each character
    for (int i = 0; i < slen; i++)
    {
        x = s[i];
        num = (int) x;
        convert(num);
    }
}

// prints out corresponding emoji to represent binary bits
void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

// converts from decimal to binary
void convert(long number)
{
    int b[BITS_IN_BYTE];
    b[0] = 0;
    b[1] = 0;
    b[2] = 0;
    b[3] = 0;
    b[4] = 0;
    b[5] = 0;
    b[6] = 0;
    b[7] = 0;

    long num = number;

    long check = 0;
    long tempNum = num;

    for (int i = 0; i < BITS_IN_BYTE; i++)
    {
        check = tempNum % 2;
        tempNum = (int)(tempNum / 2);
        b[i] = (int) check;
    }

    // iterates through binary value printing out correct emoji
    // revive through array
    for (int i = 8; i > 0; i--)
    {
        print_bulb(b[(i - 1)]);
    }
    printf("\n");
}
