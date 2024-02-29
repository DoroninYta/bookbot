import os
import sys

def _get_part_text(text : str, start : int, page_size : int):
    array_end = [",", ".", "!", ":", ";", "?"]
    end_num = min(start + page_size, len(text))
    if end_num != len(text):
        if text[end_num] in array_end and text[end_num - 1] in array_end:
            while text[end_num - 1] in array_end:
                end_num -= 1
    while text[end_num - 1] not in array_end:
        end_num -= 1
    return text[start : end_num], end_num - start

book: dict[int : str] = {}
PAGE_SIZE = 100
BOOK_PATH = ".\\books\\book.txt"

def open_file(path : str):
    file = open(path, encoding="utf8")
    content = file.read()
    return content


def prepare_book(path : str):
    file = open(path, encoding="utf8")
    content = file.read()
    text = content.lstrip()
    
    text_len = len(text)
    start_page_elem = 0
    current_page = 1
    
    while start_page_elem < text_len - 1:
        texttt, last_len = _get_part_text(text, start_page_elem, PAGE_SIZE)
        book[current_page] = texttt.lstrip()
        start_page_elem = start_page_elem + last_len + 1
        current_page += 1

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
