import base64
from elasticsearch import Elasticsearch

es=Elasticsearch([{'host': 'localhost', 'port': 9200}])

def hashit(data):
    encoded = base64.b64encode(data.encode())
    return (encoded.decode())

def dehash(data):
    decoded=data = base64.b64decode(data)
    return (decoded.decode())

def transfer(data):


    body={

    'data':hashit(data)

    }

    resh=es.index(index='storage',doc_type='dbs',body=body)
    send="https://79b986f8.ngrok.io/{}".format(resh['_id'])
    return(send)

def showdata(data):

    try:
        res=es.get(index='storage',doc_type='dbs',id=data)
    except:
        return ("I think the paste was deleted or never created ...otherwise check your url")
    out=dehash(res['_source']['data'])
    return (out)
