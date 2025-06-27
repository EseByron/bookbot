import sys

from stats import *


def get_book_text(file_path):
    with open(file_path) as book:
        content = book.read()
    return content

def main(): # Runtime
    book_input = sys.argv()
    book_text = get_book_text(book_input)

    num_words = count_words(book_text)
    char_dict = character_count(book_text)
    list_of_char = char_n_count(char_dict)
    list_of_char.sort(reverse=True, key=sort_by)
    show_report(book_input, num_words, list_of_char)
    
    
    exit()


# RUNTIME

main()