#include <stdio.h>
#include <stdlib.h>

bool search(node *tree, int number);

typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;

int main(void)
{
    //bruh
}

bool search(node *tree, int number)
{
    if (tree == NULL)
    {
        return false;
    }
    else if (number < tree->number)
    {
        return search(tree->left, number);
    }
    else if (number > tree->number)
    {
        return search(tree->right, number);
    }
    else // if (number == tree->number)
    {
        return true;
    }
}