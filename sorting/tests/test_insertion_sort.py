from insertion.insertion_sort import insertion_sort


def test_insertion_sort():
    actual = insertion_sort([8, 4, 23, 42, 16, 15])
    assert actual == [4, 8, 15, 16, 23, 42]


def test_insertion_sort_empty_list():
    actual = insertion_sort([])
    assert actual == []


def test_insertion_sort_list_with_single_element():
    actual = insertion_sort([1])
    assert actual == [1]


def test_insertion_sort_reverse_sorted():
    actual = insertion_sort([20, 18, 12, 8, 5, -2])
    assert actual == [-2, 5, 8, 12, 18, 20]


def test_insertion_sort_few_uniques():
    actual = insertion_sort([5, 12, 7, 5, 5, 7])
    assert actual == [5, 5, 5, 7, 7, 12]


def test_insertion_sort_nearly_sorted():
    actual = insertion_sort([2, 3, 5, 7, 13, 11])
    assert actual == [2, 3, 5, 7, 11, 13]
