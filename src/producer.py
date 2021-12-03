import json
import random
from kafka import KafkaProducer

topic_name = "my-topic"
producer = KafkaProducer(
  bootstrap_servers="localhost:9093",
  value_serializer=lambda x: json.dumps(x).encode()
)

random_value = random.random()
data = {"key": f"value {random_value}"}
producer.send(topic_name, value=data)
producer.flush()
