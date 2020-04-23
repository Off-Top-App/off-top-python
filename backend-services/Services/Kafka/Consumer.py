from kafka import KafkaConsumer
from json import loads
import json
from datetime import datetime
import logging
import sys


<<<<<<< HEAD:src/Services/Kafka/Consumer.py

def Consumer():
    consumer = KafkaConsumer(
        'IncomingAudioEvent',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group'
=======
consumer = KafkaConsumer(
    'IncomingAudioEvent',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
>>>>>>> master:backend-services/Services/Kafka/Consumer.py
    )
    KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    try:
        for incoming_message in consumer:
            print ("%s: value=%s" % (incoming_message.topic, incoming_message.value.decode('utf-8')))
    
    except KeyboardInterrupt:
        sys.exit()

def main():
    Consumer()

<<<<<<< HEAD:src/Services/Kafka/Consumer.py
=======
for incoming_message in consumer:
    incoming_message = incoming_message.value
    decoded_message = json.loads(incoming_message.decode('utf-8'))
    print('\nINCOMING MESSAGE: ', decoded_message)
   
>>>>>>> master:backend-services/Services/Kafka/Consumer.py

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
