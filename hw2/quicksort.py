def chooseFirstElementAsPivot(A, l, r):
    return A[l]


def chooseLastElementAsPivot(A, l, r):
    tmp = A[l]
    A[l] = A[r]
    A[r] = tmp
    return A[l]


def chooseMedianOfThreeAsPivot(A, l, r):
    if r - l == 1:
        return chooseFirstElementAsPivot(A, l, r)
    mid = (r - l) / 2 + l
    # print(l, mid, r)
    # print(A[l], A[mid], A[r])
    if (A[mid]-A[l])*(A[mid]-A[r]) < 0:
        tmp = A[l]
        A[l] = A[mid]
        A[mid] = tmp
    if (A[r]-A[l])*(A[r]-A[mid]) < 0:
        tmp = A[l]
        A[l] = A[r]
        A[r] = tmp
    return A[l]


def quicksort(A, l, r, choosePivot):
    # print('========')
    # print('before sort', A)
    compares = r - l
    if r - l <= 0: return 0
    pivot = choosePivot(A, l, r)
    # print('pivot', pivot)
    # print('choose pivot', A)
    l1, r1, l2, r2 = partition(A, l, r, pivot)
    # print(A[l1:r1+1], A[l2:r2+1])
    # print('after partition', A)
    compares += quicksort(A, l1, r1, choosePivot)
    # print('sort 1st part', A)
    compares += quicksort(A, l2, r2, choosePivot)
    # print('sort 2nd part', A)
    return compares


def partition(A, l, r, pivot):
    i = l + 1
    for j in range(l+1, r+1):
        if A[j] < pivot:
            tmp = A[j]
            A[j] = A[i]
            A[i] = tmp
            i += 1
    tmp = A[l]
    A[l] = A[i-1]
    A[i-1] = tmp
    l1 = l
    r1 = i-2
    l2 = i
    r2 = r
    return l1, r1, l2, r2


def test():
    A = [3, 8, 2, 5, 1, 4, 7, 6]
    compares = quicksort(A, 0, 7, chooseFirstElementAsPivot)
    print(compares)

    solution('10.txt')
    solution('100.txt')
    solution('1000.txt')


def solution(source):
    print(source)
    A = [int(l.strip()) for l in open(source).readlines()]
    compares = quicksort(A, 0, len(A)-1, chooseFirstElementAsPivot)
    print('choose 1st element', compares)

    A = [int(l.strip()) for l in open(source).readlines()]
    compares = quicksort(A, 0, len(A)-1, chooseLastElementAsPivot)
    print('choose last element', compares)

    A = [int(l.strip()) for l in open(source).readlines()]
    compares = quicksort(A, 0, len(A)-1, chooseMedianOfThreeAsPivot)
    print('choose median of three', compares)


def main():
    test()
    solution('QuickSort.txt')    


if __name__ == '__main__':
    main()