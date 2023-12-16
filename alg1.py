# %%
def bubble_sort(alist):
    list_length = len(alist)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(list_length - 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                is_sorted = False
        list_length -= 1
    return alist
#%%
import math
N=10000
print(N**2)
print(N*math.log(N))
#%%


print(bubble_sort([5, 7, 9, 1, 4, 2]))
# %%[markdown]
#   $$S(n) = \sum_{i_{1}=1}^n \cdots \sum_{i_{n}=1}^n \left( \frac{1}{i_1+ \ldots +i_n} \right) $$
# %%
# S(2) = ?
N = 2
summa2 = 0
for i1 in range(1, N + 1):
    for i2 in range(1, N + 1):
        denominator = i1 + i2
        summa2 += 1 / denominator
print(summa2)
# %%
# S(3) = ?
N = 3
summa3 = 0

for i1 in range(1, N + 1):
    for i2 in range(1, N + 1):
        for i3 in range(1, N + 1):
            denominator = i1 + i2 + i3
            summa3 += 1 / denominator
print(summa3)


# %%
def rec_summa(n, i_list):
    "решение задачи про N-кратную сумму"
    if len(i_list) == n:
        denominator = sum(i_list)
        return 1 / denominator
    return sum([rec_summa(n, i_list + [i]) for i in range(1, n + 1)])


# %%
rec_summa(3, list())
# %%
rec_summa(2, list())


# %%
def factorial(ch):
    # base case
    if ch in [0, 1]:
        return 1
    else:
        return ch * factorial(ch - 1)


factorial(3)


# %%
def fib_rec(n: int) -> int:
    if n in (0, 1):
        return n
    if n > 1:
        return fib_rec(n - 1) + fib_rec(n - 2)

print(fib_rec(6))
# %%
import queue

fib_q = queue.SimpleQueue()


def fib_rec2(n: int) -> int:
    fib_q.put(n)
    if n in (0, 1):
        return n
    if n > 1:
        return fib_rec2(n - 1) + fib_rec2(n - 2)


print(fib_rec2(10))


def print_q(s_queue: queue.SimpleQueue):
    "деструктивно печатаем содержимое очереди"
    while not s_queue.empty():
        print(s_queue.get(), end=" ")
    print()


print_q(fib_q)
# %%
fib_q = queue.SimpleQueue()
fib_cache = 1000 * [None]


def fib_rec_c(n: int) -> int:
    fib_q.put(n)
    if n in (0, 1):
        return n
    if n > 1:
        if not fib_cache[n]:
            fib_cache[n] = fib_rec_c(n - 1) + fib_rec_c(n - 2)
        return fib_cache[n]


print(fib_rec_c(10))
print_q(fib_q)

# %% [markdown]
#  См. про  декоратор lru_cache из модуля functools
# https://tirinox.ru/lru-cache/
#
#   LRU -- Least Recently Used
#
# при нехватке памяти из кэша вытесняются самые
# малоиспользуемые в настоящий момент элементы

#%%
from functools import lru_cache

@lru_cache(maxsize=4)
def fib_rec2(n: int) -> int:
    fib_q.put(n)
    if n in (0, 1):
        return n
    if n > 1:
        return fib_rec2(n - 1) + fib_rec2(n - 2)

fib_q = queue.SimpleQueue()
print(fib_rec2(10))
print_q(fib_q)
# %%
def print_reverse():
    s=input()
    if s == 'q':
        return
    print_reverse()
    print(s)

# %%
# %%
def binary_search(ordered_list, search_value):
    "поиск в упорядоченном списке"
    first = 0
    last = len(ordered_list) - 1

    while first <= last:
        middle = (first + last) // 2
        # Check whether the search value equals the value in the middle
        if search_value == ordered_list[middle]:
            return True
        # Check whether the search value is smaller than the value in the middle
        elif search_value < ordered_list[middle]:
            # Set last to the value of middle minus one
            last = middle - 1
        else:
            first = middle + 1
    return False


# %%
ord_list = sorted([12, 1, 5, 6, 5, 10])
# %%
binary_search(ord_list, 5)


# %%
def binary_search_recursive(ordered_list, search_value):
    # Define the base case
    if len(ordered_list) == 0:
        return False
    else:
        middle = len(ordered_list) // 2
        # Check whether the search value equals the value in the middle
        if search_value == ordered_list[middle]:
            return True
        elif search_value < ordered_list[middle]:
            # Call recursively with the left half of the list
            return binary_search_recursive(ordered_list[:middle], search_value)
        else:
            # Call recursively with the right half of the list
            return binary_search_recursive(ordered_list[middle + 1 :], search_value)


print(binary_search_recursive([1, 5, 8, 9, 15, 20, 70, 72], 5))
# %%
