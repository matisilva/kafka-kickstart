# kafka-kickstart
Just jupyter notebooks to get introduced to kafka through python clients.


## How to setup our own Kafka cluster (Linux)?
- Install java8
- Download kafka https://kafka.apache.org/downloads
- (Optional) add kafka PATH to your bashrc
- Make data folder for persistent data 
- Make zookeeper and kafka folder inside data
- Setup zookeper.properties (dataDir field) and server.properties (logs.dirs field) with created folders respectively.
- Start zookeeper
```
	./bin/zookeeper-server-start.sh config/zookeeper.properties
```
- Then start kafka
```
	kafka-server-start.sh config/server.properties
```

## Test our cluster with kafka-cli
- Create topic
```
kafka-topics.sh --create \
  --zookeeper localhost:2181 \
  --replication-factor 1 --partitions 13 \
  --topic my-topic
```
- List topics
```
kafka/bin/kafka-topics.sh --list \
    --zookeeper localhost:2181
```

- Producer
```
kafka/bin/kafka-console-producer.sh \
    --broker-list localhost:9092 \
    --topic my-topic
```

- Consumer (from beginning)
```
kafka/bin/kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic my-topic \
    --from-beginning
```

- Consumer (groups)
```
kafka/bin/kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic my-topic \
    --group my-first-group
```

## How to install jupyter notebooks?
```
	pip install jupyterlab
```

## How to test our notebooks?
Get zookeeper and kafka running and start notebooks and run cells
```
	jupyter notebook
```

