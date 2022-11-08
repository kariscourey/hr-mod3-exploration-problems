def insertion_sort(a):
    i = 1
    while i < len(a):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
        i += 1
