from stats import *

def get_book_text(path: str) -> str:
    with open(path) as f:
        file_content: str = f.read()
    return file_content

def main():
    #num_words: int = get_num_words(get_book_text("books/frankenstein.txt"))
    #num_symbols: dict[str, int] = get_symbols_count(get_book_text("books/frankenstein.txt"))
    #print(f"Found {num_words} total words")
    #print(num_symbols)

main()