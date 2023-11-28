def quicksort(array, begin, end):
    if begin < end:
        p = partition(array, 0, len(array) - 1)
        quicksort(array, begin, p - 1)
        quicksort(array, p + 1, end)

def partition(array, begin, end):
    pivot = array[end]

    i = begin - 1

    for j in range(begin, end):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[end]) = (array[end], array[i + 1])
    return i + 1


def main():
    a = [5, 2, 6, 10, -3]
    quicksort(a, 0, len(a) - 1)
    print(f"{a}")

main()

