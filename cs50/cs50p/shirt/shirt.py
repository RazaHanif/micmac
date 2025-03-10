import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if check_file(sys.argv[1], sys.argv[2]):
            if is_file(sys.argv[1]):
                read_lines(sys.argv[1], sys.argv[2])

def check_file(file_in, file_out):
    extensions = [".jpg", ".jpeg", ".png"]
    arg1valid = False
    arg2valid = False
    for i in extensions:
        if str(file_in).lower().endswith(i):
            arg1end = i
            arg1valid = True
            break

    for j in extensions:
        if str(file_out).lower().endswith(j):
            arg2end = j
            arg2valid = True
            break

    if arg1valid == True and arg2valid == True:
        if arg1end == arg2end:
            return True
        else:
            sys.exit("Input and output have different extensions")
    elif arg1valid == False:
        sys.exit("Invalid Input")
    elif arg2valid == False:
        sys.exit("Invalid Output")

def is_file(file):
    try:
        text = open(file)
        text.close()
        return True
    except FileNotFoundError:
        sys.exit("File does not exist")

def read_lines(file_in, file_out):

    # open files
    shirt = Image.open("shirt.png")
    image = Image.open(file_in)

    # edit files
    image = ImageOps.fit(image, shirt.size)
    image.paste(shirt, (0, 0), shirt.convert('RGBA'))

    # save files
    image.save(file_out)

if __name__ == "__main__":
    main()