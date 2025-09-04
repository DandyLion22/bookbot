import string

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def word_count(filepath):

    book_str = get_book_text(filepath)
    words = book_str.split()

    print("{num_words} words found in the document".format(num_words=len(words)))

def letter_count(book_text):

    letters_dict = {letter: 0 for letter in string.ascii_lowercase}
    for letter in book_text:
        if letter.lower() in letters_dict:
            letters_dict[letter.lower()] += 1
    
    return letters_dict
