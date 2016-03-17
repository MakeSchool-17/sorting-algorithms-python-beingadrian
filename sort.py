import time

def timed_sort(list, key, algorithm='merge_sort'):
    sort_func = globals()[algorithm]
    start_time   = time.time()
    sorted_list  = sort_func(list, key=key)
    end_time     = time.time()
    elapsed_time = end_time - start_time
    return (sorted_list, elapsed_time)

# ---
# Define your search algorithm functions here!

def insertion(list, key=lambda item: item):
    size = len(list)
    for i in range(1, size):
        for j in range(i, 0, -1):
            compare = list[j - 1]
            current = list[j]
            print(key(current))
            if key(current) < key(compare):
                list[j] = compare
                list[j - 1] = current

    return list

def merge_sort(list, key=lambda item: item):
    size = len(list)

    if size < 2:
        return list

    list_a = list[:size//2]
    list_b = list[size//2+1:]

    list_a_sorted = merge_sort(list_a, key=key)
    list_b_sorted = merge_sort(list_b, key=key)

    return list_a_sorted.extend(list_b_sorted)
