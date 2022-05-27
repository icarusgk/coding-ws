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

    int parameters[4];
    float avg[2];
    float index = 0;

    // Call the function for counting letters
    parameters[2] = count_letters(text);

    // Loop over the characters in the prompted text
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            // Sentences
            parameters[3]++;
        }

        if (isspace(text[i]))
        {
            // Spaces
            parameters[0]++;
        }
    }
    // Asign the number of spaces equal to the amount of words
    // Words
    parameters[1] = parameters[0];

    // Delete whitespace at the end
    if (text[strlen(text) - 1] == ' ')
    {
        // Spaces
        parameters[0]--;
        // Letters
        parameters[2]--;
    }
    else
    {
        // If there is no whitespace at the end it means there's an extra word.
        parameters[2]++;
    }

    // Preprocess the average
    avg[0] = (((float) parameters[2]  / (float) parameters[1]) * 100);
    avg[1] = (((float) parameters[3] / (float) parameters[1]) * 100);


    // Coleman-Liau index
    // index = 0.0588 * L - 0.296 * S - 15.8

    index = (((0.0588 * avg[0]) - (0.296 * avg[1])) - 15.8);

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