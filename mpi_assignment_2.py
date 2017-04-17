# part of code from lecture https://nyu-cds.github.io/python-mpi/02-messagepassing/
"""
    Assignment 10 MPI part 2

    Kaiwen Liu

"""
import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
ranNum = numpy.zeros(1,dtype = numpy.int)

if rank == 0:
       
    try:
        initial_input = input('input integer between 0 and 100:')
                     #check int 
        ranNum[0] = int(initial_input) 
    except ValueError:
        print('invlaid, give a valid input')
        

    # check if it is in range of 0 and 100
    if ranNum < 0: 
        print('invalid input')
    if ranNum > 100: 
        print('invalid input')  

    comm.Send(ranNum, dest=rank+1)
    #comm.Recv(ranNum, source=size-1)
    print('the result process',rank, 'receieved the number:',ranNum[0])

else:
    rec = comm.Irecv(ranNum, source=rank-1)
    rec.Wait()
    print("Process", rank, "received the number", ranNum[0])
    ranNum = ranNum * rank

    # send to process 0
    if rank == size - 1:
        comm.Send(ranNum, dest=0)
        print('Process', rank, 'received the number:',ranNum[0])
    # process i sends the value to process i+1 which multiplies it by i+1.
    elif rank < size - 1:
        comm.Send(ranNum, dest=rank+1)
