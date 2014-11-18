def findMedian(heap):
    heap = sorted(heap)
    if len(heap) % 2 == 0:
        median = heap[len(heap)/2-1]
    else:
        median = heap[len(heap)/2]
    # print('median: {0} of {1}'.format(median, heap))
    return median


def main():
    filename = 'Median.txt'
    # filename = 'median_testcase_82'
    medianSum = 0
    heap = []
    for l in open(filename):
        heap += [int(l.strip())]
        median = findMedian(heap)
        medianSum += median
        print('median: {0} => sum: {1}'.format(median, medianSum))
    
    print(medianSum%10000)


if __name__ == '__main__':
    main()
