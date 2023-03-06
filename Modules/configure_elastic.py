"""
Back-end: configurações do elastic search
"""

from elasticsearch import Elasticsearch
import sys, json, os, requests

def configure_elastic():
    """
    configura o elastic search e cria o indice a partir do json pré processado
    """
    elastic = Elasticsearch("http://localhost:9200")

    f = open("data/json_output.json",encoding='utf-8')
    content = json.loads(f.read())
    f.close()

    # create dhbb index in elasticsearch db and insert data
    for num, value in enumerate(content.values()):
        elastic.index(
            index="dhbb",
            doc_type='text',
            id=num,
            body=value # this is deprecated, but the new parameter returns an error
        )

        if num == 12175:
            break

configure_elastic()

