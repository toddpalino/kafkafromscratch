#!/usr/bin/env python

import logging

from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer


def main():
    client = KafkaClient("localhost:9092")
    consumer = SimpleConsumer(client, "test-group", "mytopic")

    for message in consumer:
        print(message)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.DEBUG
        )
    main()
