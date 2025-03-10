#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // index = 0.0588 * L - 0.296 * S - 15.8
    // Find Letters, Sentences, & Words
    // L = letters / words * 100
    // S = sentences / words * 100

    string text = get_string("Text: ");

    int letters = count_letters(text);
    //printf("Letters: %i\n", letters);
    int words = count_words(text);
    //printf("Words: %i\n", words);
    int sentences = count_sentences(text);
    //printf("Sentences: %i\n", sentences);

    double l = ((double) letters / (double) words * 100.0);
    //printf("l: %f\n", l);

    double s = ((double) sentences / (double) words * 100.0);
    //printf("s: %f\n", s);

    double index = (0.0588 * l) - (0.296 * s) - 15.8;
    //index = lroundf(index);

    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index <= 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %ld\n", lroundf(index));
    }
}

// find the num of letters in text
int count_letters(string text)
{
    string s = text;
    int size = strlen(s);
    int letters = 0;

    // iterate through string are add up all letters
    for (int i = 0; i < size; i++)
    {

        if (toupper(text[i]) >= 'A' && toupper(text[i]) <= 'Z')
        {
            letters++;
        }
    }

    return letters;
}

int count_words(string text)
{
    // initalize words with 1 as a sentence will contain atleast one word
    string s = text;
    int size = strlen(s);
    int words = 1;

    for (int i = 0; i < size; i++)
    {

        if (text[i] == ' ')
        {
            words++;
        }
    }

    return words;
}

// count num of sentences
int count_sentences(string text)
{
    string s = text;
    int size = strlen(s);
    int sentences = 0;

    for (int i = 0; i < size; i++)
    {

        if (text[i] == '!' || text[i] == '.' || text[i] == '?')
        {
            sentences++;
        }
    }

    return sentences;
}