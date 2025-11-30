from typing import Any

def get_num_words(text: str) -> int:
    return len(text.split())

def get_symbols_count(text:str) -> dict[str, int]:
    wordcount: dict[str, int] = {}
    lower_text: str = text.lower()

    for letter in lower_text:
        if not letter in wordcount:
            wordcount[letter] = 1
        else:
            wordcount[letter] += 1
   # print(f"{wordcount=}")
    return wordcount

def sort_on(item: dict[str, int]) -> int:
    return item["num"]

def tran_dict_to_list_of_dict(symbol_count: dict[str, int]) -> list[dict[str, Any]]:
   # print(f"{symbol_count=}")
    list_of_dicts: list[dict[str, Any]] = []
    for char, num in symbol_count.items():
        if char.isalpha():
            item = {"char": char, "num": num}
            list_of_dicts.append(item) 
    list_of_dicts.sort(reverse = True, key = sort_on)  
    return list_of_dicts

def print_report(booktext: str, list_of_dict: list[dict[str, Any]]) -> None:
    num_words: int = get_num_words(booktext)
    #print(f"{list_of_dict=}")
    #num_symbols: dict[str, int] = get_symbols_count(get_book_text(path_to_book): str)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list_of_dict:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")
            


