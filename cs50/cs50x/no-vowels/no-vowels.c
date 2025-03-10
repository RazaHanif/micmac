// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string word);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Invalid Arguments\n");
        return 1;
    }
    else
    {
       string b = replace(argv[1]);
       printf("%s\n", b);
    }
}

string replace(string word)
{
    string words = word;
    int x = strlen(word);
    string s = word;


    for (int i = 0; i < x; i++)
    {

        switch (words[i])
        {
            case 'a' | 'A':
                s[i] = '6';
                break;

            case 'e' | 'E':
                s[i] = '3';
                break;

            case 'i' | 'I':
                s[i] = '1';
                break;

            case 'o' | 'O':
                s[i] = '0';
                break;

            default:
                s[i] = words[i];
        }
    }
    return s;
}