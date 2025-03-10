// Program that takes a cli input from the user when starting the program
// Takes a input from user
// Outputs an encrypted message using the cli args value as key
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string input);
char rotate(char letter, int key);

int main(int argc, string argv[])
{
    // check if cli args are present
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        // check if cli arg is a number
        string key = argv[1];
        bool isNumber = only_digits(key);
        if (isNumber)
        {
            // atoi(s) turns string to int
            // iterate through string and convert each char value
            int k = atoi(key);
            string input = get_string("plaintext:  ");
            string output = input;
            int len = strlen(input);
            for (int i = 0; i < len; i++)
            {
                output[i] = rotate(input[i], k);
            }
            printf("ciphertext: %s\n", output);
        }
        else
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

}

// check if args are numbers, if not output error
bool only_digits(string input)
{
    string key = input;
    int length = strlen(key);
    bool isDigit = false;

    // iterates through and checks ASCII to check if its a numerical char
    for (int i = 0; i < length; i++)
    {
        if (key[i] <= 57 && key[i] >= 48)
        {
            isDigit = true;
        }
        else
        {
            isDigit = false;
            break;
        }
    }

    return isDigit;
}

// run rotate algorithm to encrypt message
char rotate(char letter, int key)
{
    char l = letter;
    int k = key;
    char c;

    // checks separately for lower and upper case
    if (l >= 'a' && l <= 'z')
    {
        c = l + k % 26;
        if (c > 122 || c < 0)
        {
            c -= 26;
        }
    }
    else if (l >= 'A' && l <= 'Z')
    {
        c = l + k % 26;
        if (c > 90)
        {
            c -= 26;
        }
    }
    // disregards all non letters
    else
    {
        c = l;
    }
    return c;
}