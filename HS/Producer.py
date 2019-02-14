import yaml
from pathlib import Path
import zipfile
import sys
from kafka import KafkaProducer
import argparse
from pprint import pprint
import json
import re




def produce(topic, message):
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
    print topic
    message = json.dumps(message)
    print bytes(message)
    producer.send(topic, bytes(message))
    producer.flush()
    #parser = argparse.ArgumentParser(description='Rides events aggregate.')

    #parser.add_argument('-t', '--topic', metavar='<topic>', type=str,
    #                    required=True,
    #                    help='Kafka topic name.')

    #parser.add_argument('-K', '--kafka_host', metavar='<host>', type=str,
    #                    required=True,
    #                    help='Kafka host list.')

    #args = parser.parse_args()

    #topic = args.topic
    #host = args.kafka_host
    
    #producer = KafkaProducer(bootstrap_servers=host)
    
    

        #message = raw_input("Input message:")
        #response = producer.send(topic, message)
        #print response
