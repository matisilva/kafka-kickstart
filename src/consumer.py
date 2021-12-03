import json
from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "my-topic",
    bootstrap_servers="localhost:9093",
    value_deserializer=lambda x: json.loads(x.decode())
)

for msg in consumer:
    print(msg.value)
