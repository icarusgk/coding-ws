#include <stdio.h>
#include <stdlib.h>

// Similar to how propotypes of functions work
typedef struct node
{
    int number;
    struct node *next; // So that the compiler knows what a node is
}
node;

int main(void)
{
    // We set it to NULL in case it has a garbage value
    node *list = NULL;
    
    node *n = malloc(sizeof(node)); // sizeof() tells us how many bytes large any data type is
    
    // Checking if its a valid addres somewhere in the computer's memory
    if (n != NULL)
    {
        (*n).number = 1;  // The same thing as n->number = 1;
        n->NULL;
    }
    
}

