from stats import countbook
from stats import countletters
from stats import sortedletters
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


with open(sys.argv[1]) as f:
    file_contents =f.read()
    countwords = countbook(file_contents)
    letters = countletters(file_contents)
    sort = sortedletters(letters)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {countwords} total words")
    print("--------- Character Count -------")
    for dictionary in sort:
        if dictionary["char"].isalpha():
            print(f"{dictionary['char']}: {dictionary['num']}")
    print("============= END ===============")