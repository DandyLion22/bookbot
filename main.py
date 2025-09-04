from stats import word_count
from stats import get_book_text
from stats import letter_count

def main(relative_path):

    print(get_book_text(relative_path))
    
word_count("books/frankenstein.txt")

letters_counted = letter_count(get_book_text("books/frankenstein.txt"))
print(letters_counted)




