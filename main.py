from stats import get_num_words, amount_each_letter, sort_dict
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = amount_each_letter(text)
    sorted_list = sort_dict(num_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()