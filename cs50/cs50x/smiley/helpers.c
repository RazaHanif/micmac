#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    RGBTRIPLE pixel = image[0][0];

    // iterates through each pixel checking which is black/white
    // black pixels will have a rgbtblue value of 0
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtBlue == 0)
            {
                // in this case changing all the black to blue
                image[i][j].rgbtBlue = 255;
                image[i][j].rgbtGreen = 0;
                image[i][j].rgbtRed = 0;
            }
        }
    }
}
