# Kafka to Elasticsearch Consumer

Сервис для потоковой передачи сообщений из Apache Kafka в Elasticsearch.

## Описание

Приложение подключается к Kafka топику, читает сообщения в режиме реального времени и индексирует их в Elasticsearch. Поддерживает обработку сообщений в формате JSON и автоматическое создание индексов.

## Требования

- Python 3.8+
- Apache Kafka 2.0+
- Elasticsearch 7.x или 8.x

## Установка

Клонируйте репозиторий и установите зависимости:

```bash
git clone <repository-url>
cd kafka-elasticsearch-consumer
pip install -r requirements.txt
```

### Зависимости

```txt
kafka-python==2.0.2
elasticsearch==8.11.0
python-dotenv==1.0.0
```

## Конфигурация

Создайте файл `.env` в корне проекта:

```env
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_TOPIC=my-topic
KAFKA_GROUP_ID=elasticsearch-consumer-group
ELASTICSEARCH_HOSTS=http://localhost:9200
ELASTICSEARCH_INDEX=kafka-messages
ELASTICSEARCH_USERNAME=elastic
ELASTICSEARCH_PASSWORD=changeme
```

## Использование

Запустите сервис:

```bash
python main.py
```

Сервис начнет читать сообщения из указанного Kafka топика и отправлять их в Elasticsearch.

## Структура проекта

```
.
├── main.py              # Точка входа приложения
├── consumer.py          # Kafka consumer
├── indexer.py           # Elasticsearch indexer
├── config.py            # Конфигурация
├── requirements.txt     # Зависимости
├── .env.example         # Пример конфигурации
└── README.md
```

## Пример кода

```python
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json

consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

es = Elasticsearch(['http://localhost:9200'])

for message in consumer:
    es.index(index='kafka-messages', document=message.value)
```

## Обработка ошибок

- При потере соединения с Kafka сервис автоматически переподключается
- Неудачные попытки индексации логируются и пропускаются
- При критических ошибках сервис корректно завершает работу

## Производительность

Для увеличения производительности можно настроить:

- Batch size для пакетной индексации
- Количество consumer threads
- Параметры буферизации Kafka

## Docker

Запуск через Docker Compose:

```bash
docker-compose up -d
```