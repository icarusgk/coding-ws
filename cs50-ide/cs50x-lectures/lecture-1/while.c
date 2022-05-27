#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int i = 0;
    // While true
    while (i < 50)
    {
        printf("%i%s", i, " hello, world\n");
        i++;
    }
}