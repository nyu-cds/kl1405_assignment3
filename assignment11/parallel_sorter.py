"""
    Assignment 11 mpi4py
    Kaiwen Liu

"""


from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def para_sort():

    # process a list with 'size' number of lists in it
    process = [[] for i in range(size)]

    # generate data
    if rank == 0:
        data = np.random.randint(0, 10000, size = 10000)
        min_ = min(data)
        max_ = max(data)
        # a slice point
        slice_ = (max_ - min_) / (size-1)

        for i in data:
            # index determines which process the number goes to
            index = int((i-min_)/slice_)
            # append numbers to its index position in process list
            process[index].append(i)

    else:
        process = None  

    # send sliced data to process and gather   
    data_scatter = comm.scatter(process, root=0)
    data_scatter.sort()
    data_sort = comm.gather(data_scatter, root=0)

    return data_sort

if __name__ == '__main__':

    data_sort = para_sort()
    # merge all sorted
    if rank == 0:
        data_sort_merged = []
        for data in data_sort:
            data_sort_merged += data
        print(data_sort_merged)