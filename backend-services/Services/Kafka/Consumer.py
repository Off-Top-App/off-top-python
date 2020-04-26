from kafka import KafkaConsumer
from json import loads
import json
from datetime import datetime
import logging
import sys



def Consumer():
    consumer = KafkaConsumer(
        'IncomingAudioEvent',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group'
    )
    KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    try:
        for incoming_message in consumer:
            consumed_value = json.loads(incoming_message.value.decode('utf-8'))
            print("SUBSCRIBING TO TOPIC: IncomingAudioEvent:\nMessage=", consumer)
    
    except KeyboardInterrupt:
        sys.exit()

def main():
    Consumer()
   

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
