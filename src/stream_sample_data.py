#!/usr/bin/env python

from faker import Faker
import time
import json
from kafka import KafkaProducer
import logging


def create_sample_date(faker: Faker, id: int):
    return {
        "id": id,
        "name": faker.unique.name(),
        "address": faker.unique.address(),
        "timestamp": faker.iso8601(),
    }


def send_to_kafka(producer: KafkaProducer, topic_name: str, data):
    try:
        producer.send(topic_name, json.dumps(data))
    except Exception as e:
        logging.error(f"Error while sending data to topic {topic_name}")
        logging.error(str(e))


if __name__ == "__main__":
    faker = Faker()
    producer = KafkaProducer(bootstrap_servers=["localhost:29092"])

    for i in range(0, 10):
        send_to_kafka(producer, "user_entry", (create_sample_date(faker, i)))
        time.sleep(5)
