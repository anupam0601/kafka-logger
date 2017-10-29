from kafka import KafkaConsumer

# connect to Kafka server and pass the topic we want to consume

consumer = KafkaConsumer('kafka-logger', bootstrap_servers=['0.0.0.0:9092'])

for msg in consumer:
    print msg
