from stats import get_num_words, get_char_count, dict_of_dict
import sys

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) < 2:
        sys.exit(1)
    directory = sys.argv[1]
    book = get_book_text(directory)
    num_words = get_num_words(book)
    character_list = get_char_count(book)
    org_list = dict_of_dict(character_list)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {directory}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in org_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    return

main()
