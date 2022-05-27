#include <stdlib.h>
#include <stdio.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    node *list = NULL; // Point to the ground so it won't be quantum
    if (list == NULL)
    {
        printf("List is NULL\n");
    }

    node *n = malloc(sizeof(node)); // Allocate individual nodes which have enough space for a number and a node

    // Check if the n is NULL
    if (n == NULL)
    {
        return 1;
    }


    n->number = 4; // Same thing as (*n).number = 4;
    n->next = NULL;

    list = n;

    n = malloc(sizeof(node));

    if (n == NULL)
    {
        free(list);
        return 1;
    }

    n->number = 5;
    n->next = NULL;

    list->next = n;

    n = malloc(sizeof(node));

    if (n == NULL)
    {
        free(list->next);
        free(list);
        return 1;
    }

    n->number = 6;
    n->next = NULL;

    list->next->next = n;

    n = malloc(sizeof(node));

    if (n == NULL)
    {
        // free(list->next->next);
        free(list->next);
        free(list);
        return 1;
    }

    n->number = 7;
    n->next = NULL;

    for (node *tmp = list; tmp != NULL; tmp = tmp->next) // Is the equivalent as list->next->next->next
    {
        printf("%i\n", tmp->number);
    }

    // Free the whole list
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list); // Frees the first node
        list = tmp;
    }
}