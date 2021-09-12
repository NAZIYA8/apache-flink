# apache-flink

# HASHTAG COUNT

Version: flink-1.13.1
Note : Make sure java is installed into the system.
Start the daemon using the command.

bin/start-cluster.sh

Installation: 
pip install apache-flink

#Trending Hashtags
A very similar example to word count, but different source/sinks. The input data in this case is read off of disk, and the output is written as a csv. The file is generated dynamically at run time.

# code
step 1: Create input file.

Creating a file containing thousands of words which are randomly chosen from a list of predefined hashtags.

step 2: Creating a source.

Getting the input's from the created file using connect() function which basically assigns the file as a source for further operations.

step 3: Creating sink.

It is the output file where the output is written in csv format.

step 4: Map function.

Doing group by on the hashtags name and then the count function generates the total count.
