#include <stdio.h>
#include <stdlib.h>

int main(void)
{

    int *list = malloc(3 * sizeof(int)); // Returns a contiguous chunk of memory back to back

    if (list == NULL)
    {
        return 1;
    }

    // Treat that chunk of array as an 'array'
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    int *tmp = realloc(list, 4 * sizeof(int)); // Reallocate the chunk of memory
    // realloc will also copy the elements too

    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    tmp[3] = 4;
    list = tmp;

    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    free(list);

}