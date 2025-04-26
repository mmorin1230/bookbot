from stats import get_word_count
from stats import character_counter
from stats import report_generator
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]
# word_count = get_word_count("./books/frankenstein.txt")
# print(f"{word_count} words found in the document")

# char_ctr = character_counter("./books/frankenstein.txt")
# print(char_ctr)

chart = report_generator(filepath)
print(chart)
