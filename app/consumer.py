import time
from confluent_kafka.cimpl import KafkaException, Consumer

from settings import consumer_settings_json


KAFKA_TOPIC = "src-app-py-events-json-000"
KAFKA_BROKER = "localhost:9092"
EXEC_TIME = 100


c = Consumer(consumer_settings_json(KAFKA_BROKER))
c.subscribe([KAFKA_TOPIC])

timeout = time.time() + int(EXEC_TIME)

try:
    while timeout >= time.time():
        events = c.poll(0.1)

        if events is None:
            continue

        if events.error():
            raise KafkaException(events.error())
        response = eval(events.value().decode('utf-8'))
        payload = {
            "id": response["id"],
            "status": "CADASTRADO"
        }
        print(payload)
except KeyboardInterrupt:
    pass

finally:
    c.close()
