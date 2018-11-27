def merge_sort(array):
    if len(array) > 2:
        a = array[:len(array)//2]
        b = array[len(array)//2:]
        c = merge(merge_sort(a), merge_sort(b))
        return c
    elif len(array) == 1:
        return array
    else:
        if array[0] > array[1]:
            return array[::-1]
        else:
            return array


def merge(a, b):
    c = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    if i < len(a):
        c.extend(a[i:])

    if j < len(b):
        c.extend(b[j:])
    
    return c

if __name__ == "__main__":
    array = input("Enter array to be sorted: ").strip().split()
    try:
        array = [int(el) for el in array]
    except:
        raise ValueError("All elements of array must be integers.")
    print(f'Before sorting: {array}')
    print(f'Merge sorted: {merge_sort(array)}')