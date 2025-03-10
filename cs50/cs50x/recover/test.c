#include <stdio.h>

int main ()
{
	int value;
    char filename[8];

	printf ("Enter an integer value: ");
	scanf ("%d", &value);
	printf ("always 3 digits: %03d\n", value);
    sprintf(filename, "%03d.jpg", value);
    printf("%s\n", filename);

}