import sys
from stats import word_count
from stats import get_book_text
from stats import letter_count
from stats import sorted_letter_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main(relative_path):

    letters_counted = letter_count(get_book_text(relative_path))

    letters_counted_and_sorted = sorted_letter_count(letters_counted)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + str(relative_path) + "...")
    print("----------- Word Count ----------")
    word_count(relative_path)
    print("--------- Character Count -------")
    for obj in letters_counted_and_sorted:
        print(obj[0] + ": " + str(obj[1]))
    print("============= END ===============")

main(sys.argv[1])




