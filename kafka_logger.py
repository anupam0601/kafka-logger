import logging
# your choice of Kafka
from kafka import SimpleProducer
from kafka_logger.handler import KafkaLoggingHandler

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
log_producer = SimpleProducer(bootstrap_servers=['0.0.0.0:9092'])
logger.addHandler(KafkaLoggingHandler(log_producer, 'app-log'))

logger.INFO("anupam.....")
