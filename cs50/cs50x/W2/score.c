#include <stdio.h>
#include <cs50.h>

const int N = 3;
float average(int array[]);

int main(void)
{
    /*
    int score1 = 72;
    int score2 = 73;
    int score3 = 33;
    */

    // store it in an array

    int scores[N];

    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score: ");
    }

    printf("Avg: %f\n", average(scores));

}

float average(int array[])
{
    int sum = 0;

    for (int i = 0; i < N; i++)
    {
        sum += array[i];
    }

    return sum / (float) N;
}