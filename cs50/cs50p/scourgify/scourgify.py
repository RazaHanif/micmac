import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if check_file(sys.argv[1]):
            if is_file(sys.argv[1]):
                read_lines(sys.argv[1], sys.argv[2])

def check_file(file):
    if str(file).endswith(".csv"):
        return True
    else:
        sys.exit("Not a CSV file")

def is_file(file):
    try:
        text = open(file)
        text.close()
        return True
    except FileNotFoundError:
        sys.exit("File does not exist")

def read_lines(file_in, file_out):
    header = ["first", "last", "house"]
    with open(file_in) as in_doc:
        reader = csv.DictReader(in_doc)
        with open(file_out, "w") as out_doc:
            writer = csv.DictWriter(out_doc, header)
            writer.writeheader()
            for line in reader:
                name = line["name"]
                home = line["house"].strip()
                lname, fname = name.split(",")
                writer.writerow({"first":fname.strip(), "last":lname.strip(), "house":home})

if __name__ == "__main__":
    main()