
from pyspark.sql import SparkSession
from pyspark import rdd
import findspark
from pyspark.context import SparkContext, xrange
import json
sc = SparkContext('local[2]', 'countWords')  


def split_words_service(values): 
    spark = SparkSession.builder.appName("PushAndPop").getOrCreate()
    rdd = spark.sparkContext.parallelize(
        values.split(" ")
    )
    vals = rdd.map(lambda word: word).collect()
    spark.stop()
    return json.dumps(vals)

def produce_pi_service(scale):
  spark = SparkSession.builder.appName("PythonPi").getOrCreate()
  n = 100000 * scale

  def f(_):
      from random import random
      x = random()
      y = random()
      return 1 if x ** 2 + y ** 2 <= 1 else 0

  count = spark.sparkContext.parallelize(
      xrange(1, n + 1), scale).map(f).reduce(lambda x, y: x + y)
  spark.stop()
  pi = 4.0 * count / n
  return pi
