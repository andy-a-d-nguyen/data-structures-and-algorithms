from sorting_comparisons.movies import movies
from sorting_comparisons.sorting import sort_by_year, sort_by_title
from sorting_comparisons.test import expected1, expected2


def test_sort_by_year():
    movies_sorted_by_year = sort_by_year(movies)
    assert movies_sorted_by_year == expected1


def test_sort_by_title():
    movies_sorted_by_title = sort_by_title(movies)
    assert movies_sorted_by_title == expected2
