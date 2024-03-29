from fastapi import FastAPI
from random import randint

from app.producer import Kafka


app = FastAPI()


KAFKA_BROKER = "localhost:9092"
users_json_topic = "src-app-py-events-json-000"


@app.post("/")
async def producer_send():
    payload = {
        "id": randint(1, 20),
        "status": "PENDENTE"
    }

    Kafka().json_producer(
        broker=KAFKA_BROKER,
        payload=payload,
        kafka_topic=users_json_topic
    )
    return {"message": "Enviada", "payload": payload}
