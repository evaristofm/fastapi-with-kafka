import json
from confluent_kafka import Producer

from app.settings import producer_settings_json
from app.callback import on_delivery_json


class Kafka(object):

    @staticmethod
    def json_producer(broker, payload, kafka_topic):
        p = Producer(producer_settings_json(broker))
        try:
            p.poll(0)
            p.produce(
                topic=kafka_topic,
                value=json.dumps(payload).encode('utf-8'),
                callback=on_delivery_json
            )
        except (BufferError, ValueError, KeyboardInterrupt) as error:
            raise error

        p.flush()
