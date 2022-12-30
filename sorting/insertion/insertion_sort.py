def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        j = i - 1
        current = a_list[i]

        while j >= 0 and current < a_list[j]:
            a_list[j + 1] = a_list[j]
            j -= 1

        a_list[j + 1] = current

    return a_list
