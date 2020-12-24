from pyspark import SparkContext, SparkConf
import configparser

if __name__ == "__main__":
    # get application name and master node url from config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    master_url = config['spark']['master_url']
    app_name = config['spark']['app_name']
    print(f"Creating Spark context to {master_url}...")

    conf = SparkConf().setAppName(app_name).setMaster(master_url)
    sc = SparkContext(conf=conf)

    # logger
    log4jLogger = sc._jvm.org.apache.log4j
    log = log4jLogger.LogManager.getLogger(__name__)
    log.warn("Count sample code with config1")

    inputWords = ["Java", "python", "C++", "scala", "Java", "python", "pyspark"]

    wordRdd = sc.parallelize(inputWords)
    print("Count: {}".format(wordRdd.count()))

    worldCountByValue = wordRdd.countByValue()
    print("CountByValue: ")
    for word, count in worldCountByValue.items():
        print("{} : {}".format(word, count))