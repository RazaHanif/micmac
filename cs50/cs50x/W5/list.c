#include <stdio.h>
#include <stdlib.h>

// define a struct for linkedlist nodes
typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(int argc, char *argv[])
{

    if (argc <= 1)
    {
        printf("Usage: ./list int int int...\n");
    }

    // define starting node for a list
    node *list = NULL;

    for (int i = 1; i < argc; i++)
    {
        // convert the argv value to an int
        int num = atoi(argv[i]);

        // get enough space from malloc to store a new node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }

        // assign value to number & next for new node
        n -> number = num;
        n -> next = NULL;

        // link node to list (prepends to list)
        n -> next = list;
        list = n;
    }

    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr -> number);
        //ptr = ptr -> next;
    }

    node *ptr = list;
    node *tmp = NULL;
    while (ptr != NULL)
    {
        tmp = ptr -> next;
        free(ptr);
        ptr = tmp;
    }

    // free the memory so theres no leak
    free(list);
    return 0;
}