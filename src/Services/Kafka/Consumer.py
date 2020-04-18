from kafka import KafkaConsumer
from json import loads
import json
from datetime import datetime


consumer = KafkaConsumer(
    'Food',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
    )
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('utf-8')))

def as_payload(message):
    return KafkaConsumer(message['user_id'])

for incoming_message in consumer:
    incoming_message = incoming_message.value
    print("{}".format(incoming_message.decode('utf-8')) )
    print(datetime.now())
   

