# producer.py

import time

from kafka import SimpleProducer, KafkaClient

#  connect to Kafka
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)

# Assign a topic
topic = 'kafka-logger'


def kafka_producer():

    print("Start emitting....")

    with open("LOGS/test_logs-2017-Oct-29-23-59-06.log", "r") as f:
        for log in f:
            producer.send_messages(topic, log)
            # To reduce CPU usage create sleep time of 0.2sec
            time.sleep(0.2)
            print("done emitting....")


kafka_producer()
