import signal
from app.consumer import create_consumer
from app.es import bulk_insert
from app.processor import process_message

running = True

def shutdown(sig, frame):
    global running
    running = False

signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)

def main():
    consumer = create_consumer()
    buffer = []

    while running:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(msg.error())
            continue

        buffer.append(process_message(msg.value()))

        if len(buffer) >= 500:
            bulk_insert(buffer)
            consumer.commit()
            buffer.clear()

    # graceful shutdown
    if buffer:
        bulk_insert(buffer)
        consumer.commit()
    consumer.close()

if __name__ == "__main__":
    main()
