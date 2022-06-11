import time, list_generator, list_sorter, list_verifier, sys

sys.setrecursionlimit(10**6)

def main():
   for i in range(1,16):
        arr = list_generator.A_shape_list(970 * i)

        starttime = time.time()
        #list_sorter.insertion_sort(arr)
        list_sorter.quick_sort_midpivot(arr, 0, len(arr)-1)
        lasttime = time.time()

        totaltime = int((lasttime - starttime) * 1000)

        print(str(i) + '. ' + str(totaltime) + 'ms' + ' --> ' + str(list_verifier.verify(arr)))

if __name__=="__main__":
    main()