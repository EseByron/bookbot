import sys

from stats import *


def get_book_text(file_path):
    with open(file_path) as book:
        content = book.read()
    return content

def main():
    try:
        book_input = sys.argv[1] # Gets the path to the book
        book_text = get_book_text(book_input)
    except IndexError:
        with open("README.md") as readme:
            msg = readme.read()
            print(msg)
            sys.exit(1)
    except FileNotFoundError:
        print("404 The file not been found.")
        sys.exit(1)


    num_words = count_words(book_text)
    char_dict = character_count(book_text)
    list_of_char = char_n_count(char_dict)
    list_of_char.sort(reverse=True, key=sort_by)
    show_report(book_input, num_words, list_of_char)
    
    
    exit()


# RUNTIME

main()