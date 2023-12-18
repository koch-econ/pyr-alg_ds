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
# %%   из книги Грокаем алгоритмы


# %%
## еще одна реализация с первым элементом в роли опорного (pivot)
def partition(my_list, first_index, last_index):
    pivot = my_list[first_index]
    left_pointer = first_index + 1
    right_pointer = last_index

    while True:
        # Iterate until the value pointed by left_pointer
        # is greater than pivot or left_pointer is greater than last_index
        while my_list[left_pointer] < pivot and left_pointer < last_index:
            left_pointer += 1

        while my_list[right_pointer] > pivot and right_pointer >= first_index:
            right_pointer -= 1
        if left_pointer >= right_pointer:
            break
        # Swap the values for the elements located at the left_pointer and right_pointer
        my_list[left_pointer], my_list[right_pointer] = (
            my_list[right_pointer],
            my_list[left_pointer],
        )

    my_list[first_index], my_list[right_pointer] = (
        my_list[right_pointer],
        my_list[first_index],
    )
    return right_pointer


# %%
def quicksort(my_list, first_index, last_index):
    if first_index < last_index:
        # Call the partition() function with the appropriate parameters
        partition_index = partition(my_list, first_index, last_index)
        # Call quicksort() on the elements to the left of the partition
        quicksort(my_list, first_index, partition_index - 1)
        quicksort(my_list, partition_index + 1, last_index)


my_list = [6, 2, 9, 7]
quicksort(my_list, 0, len(my_list) - 1)
print(my_list)

# %%
# из книги Грокаем алгоритмы (python 2.x->3)
def quicksort_g ( array ) :
    if len ( array ) < 2 :
        return array
    else:
        pivot = array[ 0 ]
        less = [ i for i in array [ 1 : ] if i <= pivot]
        greater = [ i for i in array [ 1: ] if i > pivot]
    return quicksort_g ( less ) + [ pivot ] + quicksort_g( greater )
print (quicksort_g ( [ 10, 5 , 2 , 3 ] ))
# %%
