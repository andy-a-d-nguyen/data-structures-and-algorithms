from merge.merge_sort import merge_sort


def test_merge_sort():
    actual = merge_sort([8, 4, 23, 42, 16, 15])
    assert actual == [4, 8, 15, 16, 23, 42]


def test_merge_sort_empty_list():
    actual = merge_sort([])
    assert actual == []


def test_merge_sort_list_with_single_element():
    actual = merge_sort([1])
    assert actual == [1]


def test_merge_sort_reverse_sorted():
    actual = merge_sort([20, 18, 12, 8, 5, -2])
    assert actual == [-2, 5, 8, 12, 18, 20]


def test_merge_sort_few_uniques():
    actual = merge_sort([5, 12, 7, 5, 5, 7])
    assert actual == [5, 5, 5, 7, 7, 12]


def test_merge_sort_nearly_sorted():
    actual = merge_sort([2, 3, 5, 7, 13, 11])
    assert actual == [2, 3, 5, 7, 11, 13]
