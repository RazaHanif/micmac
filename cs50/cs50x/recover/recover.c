#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

// block size in bytes
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    // Check for invalid usage
    if (argc != 2)
    {
        printf("Usage: recover [file ...]\n");
        return 1;
    }

    // open input file, includes error check
    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("Could not create %s.\n", argv[1]);
        return 1;
    }

    // declare default value for img count
    int img = 0;

    // create a var for the output file with enough space
    char outfile_name[8];
    FILE *outfile = NULL;

    // create a buffer
    uint8_t *buffer = malloc(BLOCK_SIZE);

    while (fread(buffer, BLOCK_SIZE, 1, infile) > 0)
    {
        // check if the block starts with a jpeg header
        if (buffer[0] == 0xff
            && buffer[1] == 0xd8
            && buffer[2] == 0xff
            && (buffer[3] & 0xf0) == 0xe0)
        {
            // if this isnt first file close the previous file and increase the image count
            if (outfile != NULL)
            {
                fclose(outfile);
                img++;
            }

            // open the outfile with the correct format ###.jpg, includes error check
            sprintf(outfile_name, "%03i.jpg", img);
            outfile = fopen(outfile_name, "wb");
            if (outfile == NULL)
            {
                fclose(infile);
                printf("Could not create %s.\n", outfile_name);
                return 1;
            }
        }

        // if a file is already open, write the current buffer
        if ((outfile != NULL))
        {
            fwrite(buffer, BLOCK_SIZE, 1, outfile);
        }
    }

    // close and free everything to avoid mem leaks
    fclose(infile);
    fclose(outfile);
    free(buffer);
}