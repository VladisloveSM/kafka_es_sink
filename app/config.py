from pydantic import BaseSettings

class Settings(BaseSettings):
    kafka_bootstrap_servers: str
    kafka_group_id: str = "kafka-es-sink"
    kafka_topic: str

    es_host: str
    es_index: str

    class Config:
        env_file = ".env"

settings = Settings()
