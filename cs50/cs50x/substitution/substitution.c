// This program takes a key from the cli and uses it to encrypet a message

#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Declaring all functions that will be used in this program
string sub(string text, string key);
bool key_length(string key);
bool check_key(string key);
bool repeats(string key);

// Main function takes checks for errors using other functions
// Gets input from user and outputs to console
int main(int argc, string argv[])
{
    // checks if program is run correctly from command line
    if (argc != 2)
    {
        printf("Usage: ./subsitution key\n");
        return 1;
    }

    string key = argv[1];

    // exits program using return 1
    if (!key_length(key))
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }

    // checks both at once as the error message will be same
    if (!check_key(key) || !repeats(key))
    {
        printf("Key is Invalid\n");
        return 1;
    }

    string text = get_string("plaintext: ");
    printf("ciphertext: %s\n", sub(text, key));
    return 0;

}

// Does the actual subsitution function
string sub(string text, string key)
{
    string abc_lower = "abcdefghijklmnopqrstuvwxyz";
    string abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char letter;

    for (int i = 0; i < strlen(text); i++)
    {
        letter = text[i];

        // checks if input char is upper or lower case to make correct adjustment
        for (int j = 0; j < 26; j++)
        {
            if (letter >= 'a' && letter <= 'z')
            {
                if (text[i] == abc_lower[j])
                {
                    text[i] = tolower(key[j]);
                    break;
                }
            }
            else if (letter >= 'A' && letter <= 'Z')
            {
                if (text[i] == abc_upper[j])
                {
                    text[i] = toupper(key[j]);
                    break;
                }
            }
        }
    }
    return text;
}

// checks if length of key provided is 26
bool key_length(string key)
{
    if (strlen(key) != 26)
    {
        return false;
    }
    return true;
}

// checks if the key has any non aplha characters
bool check_key(string key)
{
    int len = strlen(key);

    for (int i = 0; i < len; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }
    }

    return true;
}

// checks if any letters in the key are reused
bool repeats(string key)
{
    for (int i = 0; i < strlen(key); i++)
    {
        for (int j = i + 1; j < strlen(key); j++)
        {
            if (key[i] == key[j])
            {
                return false;
            }
        }
    }
    return true;
}