from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("Word Count").setMaster("local[*]")
    sc = SparkContext(conf = conf)
    
    inputWords = ["Java", "python", "C++", "scala", "Java", "python", "pyspark"]
    
    wordRdd = sc.parallelize(inputWords)
    print("Count: {}".format(wordRdd.count()))
    
    worldCountByValue = wordRdd.countByValue()
    print("CountByValue: ")
    for word, count in worldCountByValue.items():
        print("{} : {}".format(word, count))

