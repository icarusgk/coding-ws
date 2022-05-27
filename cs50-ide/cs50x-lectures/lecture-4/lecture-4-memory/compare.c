#include <stdio.h>

int main(void)
{
    int x;
    
    // Prompt the user for input
    printf("x: ");
    scanf("%i", &x);
    // So that scanf can go to that address and put the integer from
    // the user's keyboard there.
    
    printf("x is %i\n", x);
}