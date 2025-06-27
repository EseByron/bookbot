def count_words(text):
    splitted_text = text.split()
    counter = 0
    for word in splitted_text:
        counter += 1
    return counter

def character_count(text):
    text = text.lower()
    character_dict = {}
    counter = 1
    for character in text:
        if character not in character_dict.keys():
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def char_n_count(dictionary): # Creates a list of dictionaries with an inicial dictionary
    char_n_count = []
    for character, count in dictionary.items():
        dictionary = {"char": character, "count": count}
        char_n_count.append(dictionary)
    return char_n_count

def sort_by(items, key="count"):
    return items[key]

def show_report(file_path, num_words, item_list):
    msg = "============ BOOKBOT ============"
    print(msg)
    msg = f"Analyzing book found at {file_path}..."
    print(msg)
    msg = "----------- Word Count ----------"
    print(msg)
    msg = f"Found {num_words} total words"
    print(msg)
    msg = "----------- Word Count ----------"
    print(msg)
    for item in item_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
        




    
