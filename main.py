import random
from timeit import default_timer as timer
from insertion_sort import InsertionSort
from radix_sort import RadixSort

if __name__ == '__main__':

    # Insertion Sort caso random
    for i in [100, 1000, 10000, 100000]:

        print ("InsertionSort su Array di {} elementi Random".format(i))

        arr = [random.randint(1, 100) for _ in range(0, i)]

        start = timer()
        InsertionSort().insertionsort(arr)
        end = timer()

        print("Tempo di esecuzione: " + str(end - start) + "s")
        print("\n")

    # Insertion Sort caso migliore
    for i in [100, 1000, 10000, 100000]:
        print ("InsertionSort su Array di {} elementi array ordinato".format(i))

        arr = [0 for _ in range(0, i)]
        for i in range(1, i):
            arr[i] = arr[i-1]+1

        start = timer()
        InsertionSort().insertionsort(arr)
        end = timer()

        print("Tempo di esecuzione: " + str(end - start) + "s")
        print("\n")

    # Insertion Sort caso peggiore
    for i in [100, 1000, 10000, 100000]:
        print ("InsertionSort su Array di {} elementi array ordinato al contrario".format(i))

        arr = [0 for _ in range(0, i)]
        for i in range(1, i):
            arr[i] = arr[i-1]-1

        start = timer()
        InsertionSort().insertionsort(arr)
        end = timer()

        print("Tempo di esecuzione: " + str(end - start) + "s")
        print("\n")

    # Radix Sort
    for i in [100, 1000, 10000, 100000]:

        print ("RadixSort su Array di {} elementi Random".format(i))

        arr = [random.randint(1, 100) for _ in range(0, i)]

        start = timer()
        RadixSort().radixSort(arr)
        end = timer()

        print("Tempo di esecuzione: " + str(end - start) + "s")
        print("\n")

    # Radix Sort
    for i in [100, 1000, 10000, 100000]:
        print ("RadixSort su Array di {} elementi array ordinato".format(i))

        arr = [0 for _ in range(0, i)]
        for i in range(1, i):
            arr[i] = arr[i - 1] + 1

        start = timer()
        RadixSort().radixSort(arr)
        end = timer()

        print("Tempo di esecuzione: " + str(end - start) + "s")
        print("\n")

    # Radix Sort
    for i in [100, 1000, 10000, 100000]:
        print ("RadixSort su Array di {} elementi array ordinato al contrario".format(i))

        arr = [0 for _ in range(0, i)]
        for i in range(1, i):
            arr[i] = arr[i - 1] - 1

        start = timer()
        RadixSort().radixSort(arr)
        end = timer()

        print("Tempo di esecuzione: " + str(end - start) + "s")
        print("\n")