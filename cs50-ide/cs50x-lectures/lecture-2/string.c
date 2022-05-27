#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
  string s = get_string("Input: ");

  printf("Output: ");

  // How do I know when to stop?
  // s[i] != '\0'
  // strleng()

  for (int i = 0, n = strlen(s); i < n; i++)
  {
    printf("%c", s[i]);
  }

  printf("\n");
}