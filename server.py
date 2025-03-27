import os
from fastapi import FastAPI
from elasticsearch import Elasticsearch


app = FastAPI()

host = os.getenv("ELASTICSEARCH_HOST", "http://host.docker.internal:9200")
es = Elasticsearch([host])

index_name = "India"

def c_index():
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body = {
            "mappings": {
                "properties": {
                    "id": {
                        "type": "keyword"
                    },
                    "t": {
                        "type": "text"
                    },
                }
            }
        })
    
c_index()

@app.get("/insert/{q}")

def insert(q: str):
    d_id =  str(hash(q))
    doc = {
        "id": d_id,
        "t": q
    }
    result = es.index(index=index_name, id=d_id, body=doc)
    return {"result": result['result'], "id": d_id}

@app.get("/get/{q}")
def get(q: str):
    result = es.search(index=index_name, body={"query": {"match": {"t": q}}})
    return {"result": result['hits']['hits']}

