import locale


def sort_by_year(movies):
    movies_sorted_by_year = merge_sort_by_year(movies)
    result = []
    for movie in movies_sorted_by_year:
        result.append(movie["title"])
    return result


def merge_sort_by_year(movies):
    if len(movies) > 1:
        midpoint = len(movies) // 2
        left_movies_list = movies[:midpoint]
        right_movies_list = movies[midpoint:]

        merge_sort_by_year(left_movies_list)
        merge_sort_by_year(right_movies_list)
        merge_by_year(left_movies_list, right_movies_list, movies)

    return movies


def merge_by_year(left_movies_list, right_movies_list, movies):
    left_index = 0
    right_index = 0
    index = 0

    while left_index < len(left_movies_list) and right_index < len(right_movies_list):
        if left_movies_list[left_index]["year"] > right_movies_list[right_index]["year"]:
            movies[index] = left_movies_list[left_index]
            left_index += 1
        elif left_movies_list[left_index]["year"] == right_movies_list[right_index]["year"]:
            left_movie_title = left_movies_list[left_index]["title"]
            right_movie_title = right_movies_list[right_index]["title"]
            left_movie_title_split = left_movie_title.split()
            right_movie_title_split = right_movie_title.split()

            if left_movie_title_split[0] == "A" or \
                    left_movie_title_split[0] == "An" or \
                    left_movie_title_split[0] == "The":
                actual_left_movie_title = " ".join(left_movie_title_split[1:])
            else:
                actual_left_movie_title = left_movie_title

            if right_movie_title_split[0] == "A" or \
                    right_movie_title_split[0] == "An" or \
                    right_movie_title_split[0] == "The":
                actual_right_movie_title = " ".join(right_movie_title_split[1:])
            else:
                actual_right_movie_title = right_movie_title

            if locale.strcoll(actual_left_movie_title, actual_right_movie_title) >= 0:
                movies[index] = left_movies_list[left_index]
                left_index += 1
            else:
                movies[index] = right_movies_list[right_index]
                right_index += 1
        else:
            movies[index] = right_movies_list[right_index]
            right_index += 1
        index += 1

    while left_index < len(left_movies_list):
        movies[index] = left_movies_list[left_index]
        left_index += 1
        index += 1

    while right_index < len(right_movies_list):
        movies[index] = right_movies_list[right_index]
        right_index += 1
        index += 1


def sort_by_title(movies):
    movies_sorted_by_title = merge_sort_by_title(movies)
    result = []
    for movie in movies_sorted_by_title:
        result.append(movie["title"])
    return result


def merge_sort_by_title(movies):
    if len(movies) > 1:
        midpoint = len(movies) // 2
        left_movies_list = movies[:midpoint]
        right_movies_list = movies[midpoint:]

        merge_sort_by_title(left_movies_list)
        merge_sort_by_title(right_movies_list)
        merge_by_title(left_movies_list, right_movies_list, movies)

    return movies


def merge_by_title(left_movies_list, right_movies_list, movies):
    left_index = 0
    right_index = 0
    index = 0

    while left_index < len(left_movies_list) and right_index < len(right_movies_list):
        left_movie_title = left_movies_list[left_index]["title"]
        right_movie_title = right_movies_list[right_index]["title"]
        left_movie_title_split = left_movie_title.split()
        right_movie_title_split = right_movie_title.split()

        if left_movie_title_split[0] == "A" or \
                left_movie_title_split[0] == "An" or \
                left_movie_title_split[0] == "The":
            actual_left_movie_title = " ".join(left_movie_title_split[1:])
        else:
            actual_left_movie_title = left_movie_title

        if right_movie_title_split[0] == "A" or \
                right_movie_title_split[0] == "An" or \
                right_movie_title_split[0] == "The":
            actual_right_movie_title = " ".join(right_movie_title_split[1:])
        else:
            actual_right_movie_title = right_movie_title

        if locale.strcoll(actual_left_movie_title, actual_right_movie_title) <= 0:
            movies[index] = left_movies_list[left_index]
            left_index += 1
        else:
            movies[index] = right_movies_list[right_index]
            right_index += 1

        index += 1

    while left_index < len(left_movies_list):
        movies[index] = left_movies_list[left_index]
        left_index += 1
        index += 1

    while right_index < len(right_movies_list):
        movies[index] = right_movies_list[right_index]
        right_index += 1
        index += 1
