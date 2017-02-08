# MapReduce
* Install hadoop single node cluster in EC2
* Transfer the Crimes.csv file to /home/ubuntu in ec2
* Start Hadoop using start-all.sh
* /usr/local/hadoop/bin/hadoop dfs -copyFromLocal Crime.csv
* run the map-reduce job using: /usr/local/hadoop$ bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -file /home/hduser/python/mapper.py -mapper /home/hduser/python/mapper.py -file /home/hduser/python/reducer.py -reducer /home/hduser/python/reducer.py -input /user/hduser/Crime.csv -output /user/hduser/output
* Get the output from /user/hduser/output
* Copy the results to CrimeResults.csv
* Open index.html which has CrimeResults.csv in the same directory
