
"""
    Assignment 10 MPI
    Kaiwen Liu

"""
# part of the code from lecture https://nyu-cds.github.io/python-mpi/02-messagepassing/
# even, print hello, odd, print goodbye

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank % 2 == 0: 
	print('Hello from process' +str(rank))

if rank % 2 == 1:
	print('Goodbye from process'+ str(rank))
