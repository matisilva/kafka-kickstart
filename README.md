# Kafka kickstart

A set of commands to get introduced to Kafka using kafka-cli and a kafka python 
client.

## Run Kafka cluster
To run the Kafka cluster you need to have _docker_ and _docker-compose_ installed,
then you just simple run 
```sh
docker-compose -f docker/docker-compose.yml up -d
```

You can check the status of each container with
```sh
docker ps
```
or with
```sh
docker-compose -f docker/docker-compose.yml ps
```

## Test you cluster with kafka-cli
Since the Kafka cluster is running in docker container we need to execute the 
commands within the docker container. In order to get us inside the container 
we need to run
```sh
docker exec -it broker bash
```
or 
```sh
docker-compose -f docker/docker-compose.yml exec broker bash
```

- Creating a new topic
```sh
/bin/kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 13 --topic my-topic
```
- List topics
```sh
/bin/kafka-topics --list --zookeeper zookeeper:2181
```
- Produce messages into a topic
```sh
/bin/kafka-console-producear --broker-list broker:9092 --topic my-topic
```
- Consumer messages in a topic (from beginning)
```sh
/bin/kafka-console-consumer --bootstrap-server broker:9092 --topic my-topic --from-beginning
```
- Consumer (groups)
```sh
/bin/kafka-console-consumer --bootstrap-server broker:9092 --topic my-topic --group my-first-group
```

## Using Kafka from Python

We can find several kafka clients for Python, in this case we will use 
`kafka-python`

```sh
pip3 install kafka-python
```

- Kafka Producer
```Python
import json
from kafka import KafkaProducer

topic_name = "my-topic"
producer = KafkaProducer(
  bootstrap_servers="localhost:9093",
  value_serializer=lambda x: json.dumps(x).encode()
)

producer.send(topic_name, value={"key": "value"})
producer.flush()
```

- Kafka Consumer
```Python
import json
from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "my-topic",
    bootstrap_servers="localhost:9093",
    value_deserializer=lambda x: json.loads(x.decode())
)

for msg in consumer:
    print(msg.value)
```

