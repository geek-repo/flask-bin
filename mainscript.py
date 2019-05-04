import base64
from elasticsearch import Elasticsearch
import re
import datetime

es=Elasticsearch([{'host': 'localhost', 'port': 9200}])

def hashit(data):
    encoded = base64.b64encode(data.encode())
    return (encoded.decode())

def dehash(data):
    decoded=data = base64.b64decode(data)
    return (decoded.decode())

def transfer(data,date):

    f=re.findall("[0-9].",date)
    if f[0]<="60":
        hour,minutes=timer(f[0])
    else:
        f[0]="10"
        hour,minutes=timer(f[0])

    body={

    'data':hashit(data),
    'hour':hour,
    'minutes':minutes,
    }
    try:
        resh=es.index(index='storage',doc_type='dbs',body=body)
        send="https://79b986f8.ngrok.io/{}".format(resh['_id'])
        return(send)
    except:
        return("Error in Database")


def timer(min):

    now=datetime.datetime.now()
    hour=now.hour
    if min=="60":
        hour=now.hour+1
        minutes=now.minute

    else:
        minutes=now.minute+int(min)
        if minutes>60:
            hour=now.hour+1
            minutes=minutes-60


    return hour,minutes




def showdata(data):

    try:
        res=es.get(index='storage',doc_type='dbs',id=data)
    except:
        return ("I think the paste was deleted or never created ...otherwise check your url")
    out=dehash(res['_source']['data'])
    return (out)
