def get_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_list = file_contents.split()
        word_count = len(word_list)
    return word_count

def character_counter(filepath):
    character_counter = {}
    with open(filepath) as f:
        book_contents = f.read()
        for character in book_contents:
            if character.lower() not in character_counter:
                character_counter[character.lower()] = 1
            else:
                character_counter[character.lower()] += 1
    return character_counter

def sort_on(dict):
    return dict["num"]

def report_generator(filepath):
    char_dict = character_counter(filepath)
    dict_list = []
    wc = get_word_count(filepath)
    for char in char_dict:
        if char.isalpha():
            char_num = int(char_dict[char])
            d = {f"char": char, "num": char_num}
            dict_list.append(d)
    dict_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {filepath}\n" \
    "----------- Word Count ----------\n" \
    f"Found {wc} total words\n" \
    f"--------- Character Count -------\n" \
    )
    for dict in dict_list:
        char = dict["char"]
        num = dict["num"]
        print(f"{char}: {num}")