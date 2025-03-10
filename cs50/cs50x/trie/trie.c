// Saves popular dog names in a trie
// https://www.dailypaws.com/dogs-puppies/dog-names/common-dog-names

#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE_OF_ALPHABET 26
#define MAXCHAR 20

typedef struct node
{
    bool is_word;
    struct node *children[SIZE_OF_ALPHABET];
}
node;

// Function prototypes
bool check(char *word);
bool unload(void);
void unloader(node *current);
int letterkey(char letter);

// Root of trie
node *root;

// Buffer to read dog names into
char name[MAXCHAR];

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./trie infile\n");
        return 1;
    }

    // File with names
    FILE *infile = fopen(argv[1], "r");
    if (!infile)
    {
        printf("Error opening file!\n");
        return 1;
    }

    // Allocate root of trie
    root = malloc(sizeof(node));

    if (root == NULL)
    {
        return 1;
    }

    root->is_word = false;
    for (int i = 0; i < SIZE_OF_ALPHABET; i++)
    {
        root->children[i] = NULL;
    }

    // Add words to the trie
    while (fscanf(infile, "%s", name) == 1)
    {
        node *cursor = root;

        for (int i = 0, n = strlen(name); i < n; i++)
        {
            int index = tolower(name[i]) - 'a';
            if (cursor->children[index] == NULL)
            {

                // Make node
                node *new = malloc(sizeof(node));
                new->is_word = false;
                for (int j = 0; j < SIZE_OF_ALPHABET; j++)
                {
                    new->children[j] = NULL;
                }
                cursor->children[index] = new;
            }

            // Go to node which we may have just been made
            cursor = cursor->children[index];
        }

        // if we are at the end of the word, mark it as being a word
        cursor->is_word = true;
    }

    if (check(get_string("Check word: ")))
    {
        printf("Found!\n");
    }
    else
    {
        printf("Not Found.\n");
    }

    if (!unload())
    {
        printf("Problem freeing memory!\n");
        return 1;
    }

    fclose(infile);
}

// TODO: Complete the check function, return true if found, false if not found
bool check(char* word)
{
    int size = sizeof(word) - 1;
    node *check = root;
    int letter = 0;

    // check each child index by converting each char to its corresponding int representation
    for (int i = 0; i < size; i++)
    {
        letter = letterkey(word[i]);

        if (check->is_word == true)
        {
            return true;
        }
        else
        {
            check = check -> children[letter];
        }
    }
    return false;
}

// Unload trie from memory
bool unload(void)
{

    // The recursive function handles all of the freeing
    unloader(root);

    return true;
}

void unloader(node* current)
{

    // Iterate over all the children to see if they point to anything and go
    // there if they do point
    for (int i = 0; i < SIZE_OF_ALPHABET; i++)
    {
        if (current->children[i] != NULL)
        {
            unloader(current->children[i]);
        }
    }

    // After we check all the children point to null we can get rid of the node
    // and return to the previous iteration of this function.
    free(current);
}

// abstracrting code to remove such repeated code from main code block
int letterkey(char letter)
{
    if (letter == 'a' || letter == 'A')
    {
        return 0;
    }
    else if (letter == 'b' || letter == 'B')
    {
        return 1;
    }
    else if (letter == 'c' || letter == 'C')
    {
        return 2;
    }
    else if (letter == 'd' || letter == 'D')
    {
        return 3;
    }
    else if (letter == 'e' || letter == 'E')
    {
        return 4;
    }
    else if (letter == 'f' || letter == 'F')
    {
        return 5;
    }
    else if (letter == 'g' || letter == 'G')
    {
        return 6;
    }
    else if (letter == 'h' || letter == 'H')
    {
        return 7;
    }
    else if (letter == 'i' || letter == 'I')
    {
        return 8;
    }
    else if (letter == 'j' || letter == 'J')
    {
        return 9;
    }
    else if (letter == 'k' || letter == 'K')
    {
        return 10;
    }
    else if (letter == 'l' || letter == 'L')
    {
        return 11;
    }
    else if (letter == 'm' || letter == 'M')
    {
        return 12;
    }
    else if (letter == 'n' || letter == 'N')
    {
        return 13;
    }
    else if (letter == 'o' || letter == 'O')
    {
        return 14;
    }
    else if (letter == 'p' || letter == 'P')
    {
        return 15;
    }
    else if (letter == 'q' || letter == 'Q')
    {
        return 16;
    }
    else if (letter == 'r' || letter == 'R')
    {
        return 17;
    }
    else if (letter == 's' || letter == 'S')
    {
        return 18;
    }
    else if (letter == 't' || letter == 'T')
    {
        return 19;
    }
    else if (letter == 'u' || letter == 'U')
    {
        return 20;
    }
    else if (letter == 'v' || letter == 'V')
    {
        return 21;
    }
    else if (letter == 'w' || letter == 'W')
    {
        return 22;
    }
    else if (letter == 'x' || letter == 'X')
    {
        return 23;
    }
    else if (letter == 'y' || letter == 'Y')
    {
        return 24;
    }
    else if (letter == 'z' || letter == 'Z')
    {
        return 25;
    }

    return 0;

}
