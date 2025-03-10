// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// N = max char in a word, M = alphabet
const unsigned int N = LENGTH;
const unsigned int M = 26;

// Global var to keep track of num of words in dict
int word_count = 0;

// Hash table, row = length of word, column = first letter of the word
node *table[N][M];


// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Use hash function to get place in table
    int row = strlen(word);
    int column = hash(word);
    char *check;

    // go to that place and loop through the list strcasecmp each word
    for (node *ptr = table[row][column]; ptr != NULL; ptr = ptr->next)
    {
        check = ptr->word;
        if (!strcasecmp(check, word))
        {
            return true;
        }
    }
    return false;
}


// Hashes word to a number
unsigned int hash(const char *word)
{
    // Check the length of the word and the first letter in the word
    return (tolower(word[0])) - 'a';

}


// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open file
    FILE *infile = fopen(dictionary, "r");
    if (infile == NULL)
    {
        printf("Could not create %s.\n", dictionary);
        return false;
    }

    // declare vars for use in while loop
    char line[N + 1];
    int row;
    int column;

    // Loop through file, and get hash for each word
    while (fgets(line, N + 2, infile))
    {
        line[strcspn(line, "\n")] = 0;
        row = strlen(line);
        column = hash(line);

        // get enough mem for new node
        node *new = malloc(sizeof(node));
        if (new == NULL)
        {
            printf("Could not allocate mem.\n");
            return false;
        }

        // assign value to word & next for new node
        strcpy(new -> word, line);
        new -> next = NULL;

        // link node to table
        new -> next = table[row][column];
        table[row][column] = new;
        word_count++;
    }

    // Close file
    if (fclose(infile))
    {
        printf("Could not close %s.\n", dictionary);
        return false;
    }

    // if all goes good return true
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // initalzie var for unloading
    node *ptr = NULL;
    node *tmp = NULL;

    // nested for loop to free each pointer
    for (int row = 0; row < N; row++)
    {
        for (int column = 0; column < M; column++)
        {
            ptr = table[row][column];
            while (ptr != NULL)
            {
                tmp = ptr -> next;
                free(ptr);
                ptr = tmp;
            }
        }
    }

    return true;
}
