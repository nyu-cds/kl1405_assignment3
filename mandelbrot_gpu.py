# 
# A CUDA version to calculate the Mandelbrot set
#
from numba import cuda
import numpy as np
from pylab import imshow, show

@cuda.jit(device=True)
def mandel(x, y, max_iters):
    '''
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the 
    Mandelbrot set given a fixed number of iterations.
    '''
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i

    return max_iters

@cuda.jit
def compute_mandel(min_x, max_x, min_y, max_y, image, iters):
    '''
    tx,ty: thread index, 
    bx,by: block index,
    bw,bh: size and shape of block
    each thread in a kernel will compute one element of an array
    '''
    height = image.shape[0]
    width = image.shape[1]
    
    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    # for a 2-dimensional grid
    # from lecture: https://nyu-cds.github.io/python-gpu/02-cuda/
    tx = cuda.threadIdx.y
    ty = cuda.threadIdx.x
    bx = cuda.blockIdx.y
    by = cuda.blockIdx.x
    bw = cuda.blockDim.y
    bh = cuda.blockDim.x
    x = tx + bx * bw
    y = ty + by * bh

    real = min_x + x * pixel_size_x
    imag = min_y + y * pixel_size_y
    image[y, x] = mandel(real, imag, iters)
    
if __name__ == '__main__':
    image = np.zeros((1024, 1536), dtype = np.uint8)
    blockdim = (32, 8)
    griddim = (32, 16)
    
    image_global_mem = cuda.to_device(image)
    compute_mandel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, image_global_mem, 20) 
    image_global_mem.copy_to_host()
    imshow(image)
    show()