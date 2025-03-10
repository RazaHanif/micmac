# sys.argv gets CLI input, presented as a list
import sys

def main():
    '''
    try:
        print("Hello, my name is", sys.argv[1])
    except IndexError:
        print("Usage: python name.py [NAME]")
    '''

    #if len(sys.argv) < 2 or len(sys.argv) > 2:
    #    sys.exit("Usage: python name.py [NAME]")
    if len(sys.argv) < 2:
        sys.exit("Usage: python name.py [NAME]")

    # slices use only a range of a list or w.e
    for arg in sys.argv[1:]:
        print("Hello, my name is", arg)


main()