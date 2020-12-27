# PySpark Sample
- Sample PySpark programs tested in Spark 3.0.1 installed on Mac
## Run locally
- Run PySpark program locally with as many worker threads as logical core on machine
- Use either
  - PyCharm to run the program
  - *python3 CountExample.py* (from command line)
  - *spark-submit CountExample.py* (from command line)
## Run on standalone cluster in client mode
- Spark supports various cluster managers: Standalone (i.e. built into Spark), Hadoop’s YARN, Mesos, Kubernetes, all of which control how your workload runs on a set of resources.
- spark-submit is the only interface that works consistently with all cluster managers.
- In client mode, driver Python program will run on the same host where spark-submit runs.In cluster mode, your driver Python program and dependencies will be uploaded to and run from some worker node.
- Pre-requisite: Install and start Spark
- Use either
  - Spark-submit
    - *spark-submit CountExample_cluster.py*
  - Python3
    - *export PYSPARK_PYTHON=/usr/local/bin/python3.9*
    - *python3 CountExample_cluster.py*
