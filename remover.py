from elasticsearch import Elasticsearch
import datetime
import time


es=Elasticsearch([{'host': 'localhost', 'port': 9200}])


def remover():
    now=datetime.datetime.now()
    cur_hour=now.hour
    cur_min=now.minute

    q={
        "query": { "bool": {"must": [
          {"match": {
            "hour": cur_hour
          }},{"match": {
            "minutes": cur_min
          }}]}}}

    out=es.search(index="storage", body=q)
    if out['hits']['total']==0:
        pass
    else:
        for i in out['hits']['hits']:
            es.delete(index="storage",doc_type="dbs",id=i['_id'])



while True:
    remover()
    time.sleep(60) 
