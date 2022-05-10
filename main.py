import json
import os
from kafka import KafkaConsumer, KafkaProducer

if __name__ == '__main__':
    print("Run checker")
    CONSUMER_TOPIC_NAME = "point-checking-queue"
    PRODUCER_TOPIC_NAME = "point-status-queue"
    KAFKA_SERVER = os.environ.get("KAFKA_SERVER", "localhost:9092")

    consumer = KafkaConsumer(CONSUMER_TOPIC_NAME,
                             bootstrap_servers=[KAFKA_SERVER],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                             )
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                              value_serializer=lambda m: (json.dumps(m, ensure_ascii=False).encode('utf8')))

    for msg in consumer:
        response = msg.value
        response['checked'] = True
        producer.send(PRODUCER_TOPIC_NAME, response)
