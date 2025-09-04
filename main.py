from stats import word_count
from stats import get_book_text
from stats import letter_count
from stats import sorted_letter_count

def main(relative_path):

    print(get_book_text(relative_path))
    

letters_counted = letter_count(get_book_text("books/frankenstein.txt"))

letters_counted_and_sorted = sorted_letter_count(letters_counted)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
word_count("books/frankenstein.txt")
print("--------- Character Count -------")
for obj in letters_counted_and_sorted:
    print(obj[0] + ": " + str(obj[1]))
print("============= END ===============")




