def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = count_letters(text)
    sorted_dict = sort_occurrences(letter_count)
    print("--- Begin report of books/frankenstein.txt")
    print(f"{num_words} words found in the document")
    #print(f"These are the letters and their occurences: {letter_count}")
    print()
    for letter in sorted_dict.keys():
        if letter.isalpha():
            print(f"The \"{letter}\" character was found {sorted_dict[letter]} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(book_text):
    new_dict = {}
    text_lower = book_text.lower()
    for letter in text_lower:
        if letter not in new_dict:
            new_dict[letter] = 1
        else:
            new_dict[letter] += 1
    return new_dict

#bubble sort algorithm
def sort_occurrences(letter_count):
    items = list(letter_count.items())
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return dict(items)


main()



