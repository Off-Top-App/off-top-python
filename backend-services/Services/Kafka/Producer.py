from kafka import KafkaProducer,future
from datetime import datetime
from json import dumps
import json
import random 
from time import sleep
import logging


def Producer():
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],   
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

    def generate_random_int():
        rand = random.randint(1,10)
        if(rand % 2 ==0):
            return True
        else:
            return False
    
    data ={'user_id': 3  }

    while True:
        data['analyzed_at'] = str(datetime.utcnow())
        data['focus_score'] = generate_random_int()

        load_data = json.dumps(data)
        producer.send('outgoingFocusScore',load_data)
        producer.flush()
        print(load_data)
        sleep(2)
     
def main():
    Producer()

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:' +
               '%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
