# PySpark Sample
- Sample PySpark programs tested in Spark 3.0.1 deployed on Mac
## Run locally
- Run PySpark program locally with as many worker threads as logical core on machine
  - Directly from PyCharm
  - python3 CountExample.py (from command line)
  - spark-submit CountExample.py (from command line)
## Run on standalone cluster in client mode
- Spark supports various cluster managers: Standalone (i.e. built into Spark), Hadoop’s YARN, Mesos, Kubernetes, all of which control how your workload runs on a set of resources.
