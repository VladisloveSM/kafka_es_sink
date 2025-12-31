from confluent_kafka import Consumer
from app.config import settings

def create_consumer() -> Consumer:
    conf = {
        "bootstrap.servers": settings.kafka_bootstrap_servers,
        "group.id": settings.kafka_group_id,
        "auto.offset.reset": "earliest",
        "enable.auto.commit": False,
    }
    consumer = Consumer(conf)
    consumer.subscribe([settings.kafka_topic])
    return consumer
