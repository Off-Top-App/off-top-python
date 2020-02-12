from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from SparkMethods import SparkMethods

class SparkConfig(object):
    def __init__(self, threads, spark_name, spark_domain, spark_port):
        self.spark_threads = threads
        self.spark_name = spark_name
        self.spark_domain = spark_domain
        self.spark_port = spark_port
        self.methods = SparkMethods()

    def init_spark(self):
        self.sc = SparkContext(self.spark_threads, self.spark_name)
        self.ssc = StreamingContext(self.sc, 1)
        return self.ssc.socketTextStream(self.spark_domain, self.spark_port)

    def terminate_spark(self):
        self.ssc.start()
        self.ssc.awaitTermination()
        
    def start_spark(self):
        lines = self.init_spark()
        # add methods here
        self.methods.count_words(lines)
        self.terminate_spark()
    
def main():
    spark = SparkConfig("local[2]", "NetworkWordCount", "localhost", 9999)
    spark.start_spark()

if __name__ == "__main__":
    main()