def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    i = 0

    while low <= high:
        i += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (i, arr[mid])

    # якщо елемент не знайдений, перевіряю ліворуч він чи праворуч від mid
    if x < arr[mid]:
        pos = mid
    elif x > arr[mid] and x < arr[-1]:
        pos = high + 1

    # якщо елемент більший за останній елемент масиву, вертаю None
    else:
        return None

    return (i, arr[pos])


ARR = [2.3, 3.1, 4.9, 10.5, 40.1, 40.2, 40.3, 50]
X = 10

result = binary_search(ARR, X)

if result is not None:
    print(f"{X} is located before {result[1]} at the array. It took {
          result[0]} iteration(s) to find it.")
else:
    print(f"The element {X} is out of range")
