import time

"""
sumv1 - computes the sum of the first n integers using a loop
"""
def sumv1(n):
    start = time.time()    #returns the clock time in seconds

    num = 0
    for i in range(1,n+1):
        num += i

    end = time.time()

    taken = end - start

    return "sum = %d : running time required was \t %10.7f seconds"%(num, taken)

"""
sumv2 - computes the sum of the first n integers using a closed equation
        
"""
def sumv2(n):
    start = time.time()    #returns the clock time in seconds

    num = (n*(n+1))/2

    end = time.time()

    taken = end - start

    return "sum = %d : running time required was \t %10.7f seconds"%(num, taken)


def main():
    print(sumv1(10000))
    # add calls for 100,000 and 1,000,000
    print(sumv1(100000))
    print(sumv1(1000000))
    print('------')
    print(sumv2(10000))
    # add calls for 100,000 and 1,000,000
    print(sumv2(100000))
    print(sumv2(1000000))

main()

