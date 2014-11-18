import time

def main():
    filename = 'algo1-programming_prob-2sum.txt'
    # filename = '2sum_testcase_6'
    integers = dict()
    startTime = time.time()
    for l in open(filename):
        integers[(int(l.strip()))] = 0
    print("--- Load takes {0} seconds ---".format(time.time() - startTime))

    results = []
    for t in range(-10000, 10001):
        startTime = time.time()
        for x in integers.keys():
            if t-x in integers and t-x != x:
                print('{0}+{1}={2}'.format(x, t-x, t))
                results.append(t)
                break
        print("--- check {0} takes {1} seconds ---".format(t, time.time() - startTime))
    print(len(results))


if __name__ == '__main__':
    main()
