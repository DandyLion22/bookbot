import string

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def word_count(filepath):

    book_str = get_book_text(filepath)
    words = book_str.split()

    print("Found {num_words} total words".format(num_words=len(words)))

def letter_count(book_text):

    letters_dict = {letter: 0 for letter in string.ascii_lowercase}
    for letter in book_text:
        if letter.lower() in letters_dict:
            letters_dict[letter.lower()] += 1
    
    return letters_dict

def sorted_letter_count(letter_dict):

    sorted_dict = sorted(letter_dict.items(), key=lambda x: -x[1])

    return sorted_dict

