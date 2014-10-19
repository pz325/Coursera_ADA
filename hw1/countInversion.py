'''
count inversion
'''

# indent = 0
def countInversion(a):
    # global indent
    # indent += 1
    # print('='*indent, len(a), a)
    if len(a) == 1:
        # indent -= 1
        # print('<==')
        return a, 0
    else:
        half = len(a) / 2
        # print(' '*indent, 'first half', half, a[:half])
        # print(' '*indent, 'second half', half, a[half:])        
        sortedFirstHalf, x = countInversion(a[:half])
        sortedSecondHalf, y = countInversion(a[half:])
        sortedAll, z = mergeAndCountInversion(sortedFirstHalf, sortedSecondHalf);
        return sortedAll, x + y + z


def mergeAndCountInversion(sortedFirstHalf, sortedSecondHalf):
    # print('merge', sortedFirstHalf, sortedSecondHalf)
    i, j = 0, 0
    sortedAll = []
    numInversion = 0
    for k in xrange(0, len(sortedFirstHalf)+len(sortedSecondHalf)):
        if sortedFirstHalf[i] < sortedSecondHalf[j]:
            sortedAll.append(sortedFirstHalf[i])
            i += 1
            if i == len(sortedFirstHalf):
                sortedAll = sortedAll + sortedSecondHalf[j:]
                break
        else:
            sortedAll.append(sortedSecondHalf[j])
            j += 1
            numInversion += len(sortedFirstHalf[i:])
            if j == len(sortedSecondHalf):
                sortedAll = sortedAll + sortedFirstHalf[i:]
                break
    # print('<==', sortedAll, numInversion)
    return sortedAll, numInversion


def main():
    a = [int(l.strip()) for l in open('IntegerArray.txt').readlines()]
    # a = [1, 3, 5, 2, 4, 6]
    sortedAll, numInversion = countInversion(a)
    print(numInversion)

if __name__ == '__main__':
    main()
