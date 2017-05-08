# modified by lecture code: https://nyu-cds.github.io/python-bigdata/03-spark/

from pyspark import SparkContext
from operator import mul

if __name__ == '__main__':
	sc = SparkContext("local", "product")
	# Create an RDD of numbers from 1 to 1,000

	nums = sc.parallelize(range(1, 1001))
	#Use fold method to creat a program that calculates the product of all the numbers from 1 to 1000 	
	#and prints the result.   # https://spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html#fold 
	product = nums.fold(1, mul)

	print(product)

