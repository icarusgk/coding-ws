#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start_size;
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    // TODO: Prompt for end size
    int end_size;
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);

    // TODO: Calculate number of years until we reach threshold

    int llamas_born;
    int llamas_pass;

    int years = 0;

    while (start_size < end_size)
    {
        llamas_born = (int) start_size / 3;
        llamas_pass = (int) start_size / 4;

        int new_llamas = (start_size + (llamas_born - llamas_pass));

        start_size = new_llamas;
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}