#!/usr/bin/env python

import logging
import time

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer


def main():
    client = KafkaClient("localhost:9092")
    producer = SimpleProducer(client)

    for i in range(5):
        producer.send_messages('mytopic', "This is my test message, number {0}".format(i))
        time.sleep(1)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.DEBUG
        )
    main()
