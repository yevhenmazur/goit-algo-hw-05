import os
import timeit
import requests
from algorithms import kmp_search, boyer_moore_search, rabin_karp_search

def get_document(url: str) -> str:
    '''Get the text document from the url and return his content as a string'''
    response = requests.get(url)
    response.raise_for_status()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, ".tmp.txt")

    # Збереження документа на диск, бо я щось не розібрався як його без цього перекодувати
    with open(file_path, "wb") as file:
        file.write(response.content)

    # Зчитування вмісту документа
    with open(file_path, "r", encoding="cp1251") as file:
        return file.read()

def measure_execution_time(algorithm: str, text: str, pattern: str) -> float:
    '''
    Take a function name, some text in str format and substring in str format.
    Call the function with these two arguments and measure the execution time
    '''
    stmt = f'{algorithm}(content, pattern)'
    setup = f'from __main__ import {algorithm}; content = {repr(text)}; pattern = {repr(pattern)}'
    execution_time = timeit.timeit(stmt, setup=setup, number=1)

    return execution_time

def main():

    URL1 = "https://drive.usercontent.google.com/download?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh&export=download&authuser=0"
    URL2 = "https://drive.usercontent.google.com/download?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ&export=download&authuser=0"
    PATTERN_EXIST = "Електронний ресурс"
    PATTERN_DOES_NOT_EXIST = "Мама мила раму"
    ALGORITHMS = ["kmp_search", "boyer_moore_search", "rabin_karp_search"]

    results = {alg: [0, 0, 0, 0] for alg in ALGORITHMS}

    for algorithm in ALGORITHMS:
        for url_index, url in enumerate([URL1, URL2]):
            content = get_document(url)
            for pattern_index, pattern in enumerate([PATTERN_EXIST, PATTERN_DOES_NOT_EXIST]):
                execution_time = measure_execution_time(algorithm, content, pattern)
                results[algorithm][url_index * 2 + pattern_index] = execution_time

    # Виведення результатів у вигляді таблиці
    print("Алгоритм             Стаття 1 (+)        Стаття 1 (-)          Стаття 2 (+)         Стаття 2 (-)")
    for algorithm, times in results.items():
        print(f"{algorithm:<20} {times[0]:<20.6f} {times[1]:<20.6f} {times[2]:<20.6f} {times[3]:<20.6f}")

if __name__ == "__main__":
    main()
