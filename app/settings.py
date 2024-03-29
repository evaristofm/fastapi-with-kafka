
def producer_settings_json(broker):
    json = {
        "client.id": 'live-python-app-producer',
        "bootstrap.servers": broker,
        "enable.idempotence": "true",
        "acks": "all",
        "linger.ms": 100,
        "batch.size": 100,
        "compression.type": "gzip",
        "max.in.flight.requests.per.connection": 5
    }
    return dict(json)


def consumer_settings_json(broker):
    json = {
        "bootstrap.servers": broker,
        "group.id": "python-app-consumer",
        "auto.commit.interval.ms": 6000,
        "auto.offset.reset": "latest"
    }
    return dict(json)

