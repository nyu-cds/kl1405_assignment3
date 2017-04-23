import unittest
import parallel_sorter
import numpy as np

class test_function(unittest.TestCase):
	'''this is a test function for parallel_sorter.py'''
    
    def test_parallel_sorter(self):
    	data = np.random.randint(0, 10000, size = 10000)
    	merged = parallel_sorter.para_sort()
    	# test if there are 10000 elements in data
    	self.assertEqual(len(data), 10000)
    	# test if the final result 'merged' is sorted
        self.assertEqual(merged, sorted(merged))



if __name__ =='__main__':
    unittest.main()