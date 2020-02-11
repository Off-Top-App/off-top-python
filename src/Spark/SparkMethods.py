from pyspark import SparkContext

class SparkMethods:
    def count_words(self, lines):
        words = lines.flatMap(lambda line: line.split(" "))
        pairs = words.map(lambda word: (word, 1))
        wordCounts = pairs.reduceByKey(lambda x, y: x + y)
        wordCounts.pprint()