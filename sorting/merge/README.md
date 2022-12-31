# Blog Notes: Merge Sort

Merge sort is a sorting algorithm that sorts an array by recursively splitting an array into smaller arrays until the resulting arrays cannot be split anymore (arrays that only have one element). Then, the elements in the arrays are put back into the larger arrays with smallest element being put back first, and so on; this merging process also happens recursively until the original array is produced in a sorted manner.

## Pseudocode

```md
MergeSort(int[] arr)
    IF arr.length > 1
        int midpoint = arr.length // 2
        int[] left_arr = arr[0:midpoint]
        int[] right_arr = arr[midpoint:arr.length]
        <!-- Sort the left side -->
        MergeSort(left_arr)
        <!-- Sort the right side -->
        MergeSort(right_arr)
        <!-- Merge the left side and the right side -->
        Merge(left_arr, right_arr, arr)

Merge(int[] left_arr, int[] right_arr, int[] arr)
    int left_index = 0
    int right_index = 0
    int index = 0

    <!-- Until the end of either left_arr or right_arr is reached, pick the smaller elements between the two and put them in the arr -->
    WHILE left_index < left_arr.length && right_index < right_arr.length
        IF left_arr[left_index] <= right_arr[right_index]
            arr[index] = left_arr[left_index]
            left_index = left_index + 1
        ELSE
            arr[index] = right_arr[right_index]
            right_index = right_index + 1
        index = index + 1

    <!-- Put the remaining elements in either left_arr or right_arr into the arr -->
    WHILE left_index < left_arr.length
        arr[index] = left_arr[left_index]
        left_index = left_index + 1
        index = index + 1

    WHILE right_index < right_arr.length
        arr[index] = right_arr[right_index]
        right_index = right_index + 1
        index = index + 1
```

## Solution

To run the tests for this code challenge, make sure you cd into the `sorting` directory first.

```bash
python3 -m venv .venv
```

Then activate the virtual environment:

```bash
source .venv/bin/activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

To run the tests for this code challenge:

```bash
pytest -v tests/test_merge_sort.py
```

To deactivate the virtual environment:

```bash
deactivate
```

## Link to Code

[Link to Code](merge_sort.py)
