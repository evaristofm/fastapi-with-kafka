def on_delivery_json(err, msg):
    if err is not None:
        print(f"msg delivery failed: {err}")
    print(f"msg sucessfully produced to {msg.topic()}")


def on_delivery_avro(err, msg, obj):
    if err is not None:
        print(f"msg {obj} delivery failed")
    print(f"msg {obj} sucessfully produced to {obj} -> {msg.topic()}")
