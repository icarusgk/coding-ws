#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char alpha = get_char("Input: ");

    if (isalpha(alpha))
    {
        printf("Your input is alphabetical.\n");
    }
    else
    {
        printf("Your input is not alphabetical.\n");
    }
}