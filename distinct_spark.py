# modified from lecture code

from pyspark import SparkContext
import re

def splitter(line):
    line = re.sub(r'^\W+|\W+$', '', line)
    return map(str.lower, re.split(r'\W+', line))

if __name__ == '__main__':
	sc = SparkContext("local", "wordcount_distinct")
	
	text = sc.textFile('pg2701.txt')
	words = text.flatMap(splitter)
	# words_mapped = words.map(lambda x: (x,1))
	# sorted_map = words_mapped.sortByKey()
	distinct = worlds.distinct().count()
	print(distinct)