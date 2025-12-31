from elasticsearch import Elasticsearch, helpers
from app.config import settings

es = Elasticsearch(settings.es_host)

def bulk_insert(docs: list[dict]):
    actions = [
        {
            "_index": settings.es_index,
            "_source": doc,
        }
        for doc in docs
    ]
    helpers.bulk(es, actions)
