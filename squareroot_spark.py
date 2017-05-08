
from pyspark import SparkContext
from operator import add
from math import sqrt

if __name__ == '__main__':

    sc = SparkContext("local", "average_sqrt")
    # Create an RDD of numbers from 1 to 1,000
    nums = sc.parallelize(range(1,1001))

    # map to take square root for each
    take_sqrt = nums.map(sqrt)

    # fold to sum square roots of all numebrs, then divided by 1000
    average_sqrt = take_sqrt.fold(0, add) / 1000

    print(average_sqrt)