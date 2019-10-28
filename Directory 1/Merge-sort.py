# merge sort

l = []  # declaring list l

n = int(input("Enter number of elements in the list: "))  # taking value from user

for i in range(n):
    temp = int(input("Enter element" + str(i + 1) + ': '))
    l += [temp]


def merge_sort(L):
    mid = int((len(L) - 1) / 2)  # calculate the value of middle index of array

    if len(L) > mid + 2:  # this loop will run when length of array is greater than 2
        a = merge_sort(L[0:mid])  # a is initialised with left side of the array taking reference as middle index
        b = merge_sort(L[mid:len(L)])  # b is initialised with right side of the array taking reference as middle index

    elif len(L) == 2:  # this loop will when length of array is equal to 2
        a = [L[0]]  # a is initiliased with the first element of array
        b = [L[1]]  # b is initiliased with the second element of array
    else:
        return L

    i = 0
    j = 0
    new = []

             