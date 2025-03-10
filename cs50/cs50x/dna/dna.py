import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("USAGE: dna.py ___.csv ___.txt")

    # Read database file into a variable
    people = []
    csv_file = csv.DictReader(open(sys.argv[1]))
    for row in csv_file:
        people.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as dna_file:
        test_dna = dna_file.read()

    # Find longest match of each STR in DNA sequence
    longest = {}
    for index in range(len(people)):
        for key in people[index]:
            if key != "name":
                l = longest_match(test_dna, key)
                longest.update({key: l})
    total = len(longest)

    # Check database for matching profiles
    for index in range(len(people)):
        count = 0
        for key in longest:
            dna_str = longest[key]
            person_str = int(people[index][key])
            if dna_str == person_str:
                count += 1
                if count == total:
                    sys.exit(people[index]["name"])
    return sys.exit("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
