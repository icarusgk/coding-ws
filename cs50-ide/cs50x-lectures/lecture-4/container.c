#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// Prototypes
int count_letters(string);

int main(void)
{
    // Variable initiation
    string text = get_string("Text: ");
    
    int spaces = 0;
    int words = 0;
    int letters = 0;
    int sentences = 0;

    float avg_letters = 0;
    float avg_sentences = 0;
    float index = 0;

    // Call the function for counting letters
    letters = count_letters(text);

    // Loop over the characters in the prompted text
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }

        if (isspace(text[i]))
        {
            spaces++;
        }
    }
    // Asign the number of spaces equal to the amount of words
    words = spaces;

    // Delete whitespace at the end
    if (text[strlen(text) - 1] == ' ')
    {
        spaces--;
        letters--;
    }
    else
    {
        // If there is no whitespace at the end it means there's an extra word.
        words++;
    }

    // Preprocess the average
    avg_letters = (((float) letters  / (float) words) * 100);
    avg_sentences = (((float) sentences / (float) words) * 100);


    // Coleman-Liau index
    // index = 0.0588 * L - 0.296 * S - 15.8

    index = (((0.0588 * avg_letters) - (0.296 * avg_sentences)) - 15.8);

    // Round the grade to the nearest whole number
    int grade = (int) round(index);

    // Print the grade based on the index
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }


}

// Counts the letters in a string
int count_letters(string t)
{
    int letters = 0;
    for (int i = 0, n = strlen(t); i < n; i++)
    {
        if (isalpha(t[i]))
        {
            letters++;
        }
    }
    return letters;
}