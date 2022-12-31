def merge_sort(a_list):
    if len(a_list) > 1:
        midpoint = len(a_list) // 2
        left_list = a_list[:midpoint]
        right_list = a_list[midpoint:]

        merge_sort(left_list)

        merge_sort(right_list)

        merge(left_list, right_list, a_list)

    return a_list


def merge(left_list, right_list, a_list):
    left_index = 0
    right_index = 0
    index = 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            a_list[index] = left_list[left_index]
            left_index += 1
        else:
            a_list[index] = right_list[right_index]
            right_index += 1
        index += 1

    while left_index < len(left_list):
        a_list[index] = left_list[left_index]
        left_index += 1
        index += 1

    while right_index < len(right_list):
        a_list[index] = right_list[right_index]
        right_index += 1
        index += 1
