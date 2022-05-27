#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = 12345;

    while(x)
    {
        printf("%d\n", x % 10);
        x = x / 10;
    }
}