from kafka import KafkaConsumer
from json import loads
import json
from datetime import datetime
import logging
import sys
import scipy.io.wavfile
import numpy as np



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
            consumed_value = json.loads(incoming_message.value)
            # print("SUBSCRIBING TO TOPIC: IncomingAudioEvent:\nMessage=", consumed_value)
            audioBytes= json.dumps(consumed_value['audioData'])
            print(consumed_value)
            parseAudioBytes = bytes(audioBytes.encode())
            # byteArr = bytearray()
            # byteArr.extend(va.encode())
            # make file
            # newFile = open("filename.txt", "wb")
            # write to file
            # for byte in bytes(va):
                # newFile.write(byte.to_bytes(1, byteorder='big'))
           
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
