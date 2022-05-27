#include <stdio.h>
#include <cs50.h>
#include <string.h>

// argc stands for argument counter
// argv stands for argument vector, that is a list of words
int main(int argc, string argv[])
{
  if (argc == 2)
  {
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
      printf("%c\n", argv[1][i]);
    }
  }
}