def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


def perfect(nums):
    x = []
    for i in nums:
        summa = 1
        for j in range(2, i ** 0.5 + 1):
            if i % j == 0:
                summa += j
                summa += i // j
        if i == summa:
            x.append(i)
    return x


def simple(nums):
    x = []
    for i in nums:
        z = False
        for j in range(2, i ** 0.5 + 1):
            if i % j == 0:
                z = True
        if not z:
            x.append(i)
    return x


def not_simple(nums):
    x = []
    for i in nums:
        z = False
        for j in range(2, i ** 0.5 + 1):
            if i % j == 0:
                z = True
        if z:
            x.append(i)
    return x
