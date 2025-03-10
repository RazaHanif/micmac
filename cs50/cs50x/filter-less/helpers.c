#include <math.h>

#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // declare default variables
    RGBTRIPLE pixel = image[0][0];
    double greyValue = 0;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // get average value all colors and apply to each rgbtValue
            greyValue = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;

            image[i][j].rgbtBlue = round(greyValue);
            image[i][j].rgbtGreen = round(greyValue);
            image[i][j].rgbtRed = round(greyValue);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // declare default variables
    RGBTRIPLE pixel = image[0][0];
    double sepiaRed = 0;
    double sepiaGreen = 0;
    double sepiaBlue = 0;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // calculate sepia value for each color
            // if value is greater than 255, cap value a 255 otherwise give new value
            sepiaRed = (0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            sepiaGreen = (0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            sepiaBlue = (0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);

            // do all calc first otherwise core values change
            if (sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = round(sepiaRed);
            }

            if (sepiaGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = round(sepiaGreen);
            }

            if (sepiaBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = round(sepiaBlue);
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // declare default values
    RGBTRIPLE pixel = image[0][0];
    RGBTRIPLE temp[height][width];

    // run for loop to iterate through each pixel and store the value in the temp image with horizon reflected
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][width - (j + 1)].rgbtRed = image[i][j].rgbtRed;
            temp[i][width - (j + 1)].rgbtGreen = image[i][j].rgbtGreen;
            temp[i][width - (j + 1)].rgbtBlue = image[i][j].rgbtBlue;
        }

        // output new values
        for (int k = 0; k < width; k++)
        {
            image[i][k].rgbtRed = temp[i][k].rgbtRed;
            image[i][k].rgbtGreen = temp[i][k].rgbtGreen;
            image[i][k].rgbtBlue = temp[i][k].rgbtBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // declare default values
    RGBTRIPLE pixel = image[0][0];
    RGBTRIPLE temp[height][width];
    int boxR[9] = {0};
    int boxG[9] = {0};
    int boxB[9] = {0};
    double red = 0;
    double green = 0;
    double blue = 0;
    double avg = 0;

    for (int i = 0; i < height; i++)
    {
        // reset all values
        red = 0;
        green = 0;
        blue = 0;
        avg = 0;

        for (int j = 0; j < width; j++)
        {
            // check if index exists on row above, if so get values and increase counter
            if ((i - 1) >= 0)
            {
                if ((j - 1) >= 0)
                {
                    boxR[0] = image[i - 1][j - 1].rgbtRed;
                    boxG[0] = image[i - 1][j - 1].rgbtGreen;
                    boxB[0] = image[i - 1][j - 1].rgbtBlue;
                    avg++;
                }

                boxR[1] = image[i - 1][j].rgbtRed;
                boxG[1] = image[i - 1][j].rgbtGreen;
                boxB[1] = image[i - 1][j].rgbtBlue;
                avg++;

                if ((j + 1) < width)
                {
                    boxR[2] = image[i - 1][j + 1].rgbtRed;
                    boxG[2] = image[i - 1][j + 1].rgbtGreen;
                    boxB[2] = image[i - 1][j + 1].rgbtBlue;
                    avg++;
                }
            }

            // check if index exists on same row, if so get value and add to counter
            if ((j - 1) >= 0)
            {
                boxR[3] = image[i][j - 1].rgbtRed;
                boxG[3] = image[i][j - 1].rgbtGreen;
                boxB[3] = image[i][j - 1].rgbtBlue;
                avg++;
            }

            boxR[4] = image[i][j].rgbtRed;
            boxG[4] = image[i][j].rgbtGreen;
            boxB[4] = image[i][j].rgbtBlue;
            avg++;

            if ((j + 1) < width)
            {
                boxR[5] = image[i][j + 1].rgbtRed;
                boxG[5] = image[i][j + 1].rgbtGreen;
                boxB[5] = image[i][j + 1].rgbtBlue;
                avg++;
            }

            // check if index exists on below row, if so get value and add to counter
            if ((i + 1) < height)
            {
                if ((j - 1) >= 0)
                {
                    boxR[6] = image[i + 1][j - 1].rgbtRed;
                    boxG[6] = image[i + 1][j - 1].rgbtGreen;
                    boxB[6] = image[i + 1][j - 1].rgbtBlue;
                    avg++;
                }

                boxR[7] = image[i + 1][j].rgbtRed;
                boxG[7] = image[i + 1][j].rgbtGreen;
                boxB[7] = image[i + 1][j].rgbtBlue;
                avg++;

                if ((j + 1) < width)
                {
                    boxR[8] = image[i + 1][j + 1].rgbtRed;
                    boxG[8] = image[i + 1][j + 1].rgbtGreen;
                    boxB[8] = image[i + 1][j + 1].rgbtBlue;
                    avg++;
                }
            }

            // record total amount for each color
            for (int k = 0; k < 9; k++)
            {
                red += boxR[k];
                green += boxG[k];
                blue += boxB[k];
                boxR[k] = 0;
                boxG[k] = 0;
                boxB[k] = 0;
            }

            // output new value
            red /= avg;
            green /= avg;
            blue /= avg;

            temp[i][j].rgbtRed = round(red);
            temp[i][j].rgbtGreen = round(green);
            temp[i][j].rgbtBlue = round(blue);

            // reset all values
            red = 0;
            green = 0;
            blue = 0;
            avg = 0;
        }
    }

    // return correct values into oringal image
    for (int l = 0; l < height; l++)
    {
        for (int m = 0; m < width; m++)
        {
            image[l][m].rgbtRed = temp[l][m].rgbtRed;
            image[l][m].rgbtGreen = temp[l][m].rgbtGreen;
            image[l][m].rgbtBlue = temp[l][m].rgbtBlue;
        }
    }
    return;
}
