def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        # k - индекс целевого списка
        # i - индекс левой половины
        # j - индекс правой половины
        i = j = k = 0
        # из двух списков копируем сначала меньшие
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1
        # из оставшихся циклов сработает один
        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1


# %%
my_list = [35, 22, 100, 4, 500, 20, 30, 40, 1]
merge_sort(my_list)
print(my_list)
# %% [markdown]
# ### Hoar's QuickSort
#
#   https://www.geeksforgeeks.org/quick-sort/?ref=header_search
#
# Python3 implementation of QuickSort

# %%


# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)


# Driver code
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    N = len(array)

    # Function call
    quicksort(array, 0, N - 1)
    print("Sorted array:")
    for x in array:
        print(x, end=" ")

# This code is contributed by Adnan Aliakbar
#%%
