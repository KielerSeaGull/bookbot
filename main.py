from stats import *
import sys

if not sys.argv[1]:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path: str = sys.argv[1]

def get_book_text(path: str) -> str:
    with open(path) as f:
        file_content: str = f.read()
    return file_content

def main():
    
    #wandelt text in ein dic char -> count um, um dieses dann in eine Liste aus 2er-Dict (nur Buchstaben) Char: char, Num: num umzuwandeln
    li_letters = tran_dict_to_list_of_dict(get_symbols_count(get_book_text(path)))
    print_report(path, get_book_text(path), li_letters)

    #num_words: int = get_num_words(get_book_text("books/frankenstein.txt"))
    #num_symbols: dict[str, int] = get_symbols_count(get_book_text("books/frankenstein.txt"))
    #print(f"Found {num_words} total words")
    #print(num_symbols)

main()
