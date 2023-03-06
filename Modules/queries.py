"""
Cria as estruturas de busca, funcionando como integração da interface com o backend
"""
import streamlit as st
from elasticsearch import Elasticsearch

es = Elasticsearch( "http://localhost:9200")


def print_results(results):
        """
        Imprime os resultados (title + text) na interface
        """ 

        st.subheader(f'Mostrando: {len(results["hits"]["hits"])} resultados')

        for result in results["hits"]["hits"]:
                item = result["_source"]

                with st.expander(item["title"]):
                    st.write(item["text"])


def render_filter_fields(args_dict):
        """
        Renderiza os filtros preenchidos, construindo a lista dos match que serão utilizada pela query
        """        
        query = []

        # select valid fileds
        for key,value in args_dict.items():
                if value != "":
                        query.append({ "match": {key:value}})

        return query
        

def render_search_field(data,operator):
        """
        Renderiza o texto digitado na busca, construindo a query que será utilizada 
        no formato adequado.
        O texto é rederizado conforme o operador selecionado.
        Ref: https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html
        """
        query = []

        if operator == "OR" and data != "":
                query = [{ "match": {"text":data}}]

        elif operator == "AND" and data != "":
                for word in data.split(" "):
                        if word != "":
                                item = {"match": {"text":word}}
                                query.append(item)
        else: return 0

        return query



def query_search(text,data,n_max):
        """
        Realiza a query conforme os campos preenchidos.
        Os parâmetros devem estar pre-formatados.
        Ref: https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html
        """

        if len(data) != 0 and text !=0:
                query = {
                        "bool": {
                "must": text,
                "filter": data
                }}
        elif len(data) != 0:
                query = {
                        "bool": {
                "filter": data
                }}
        elif text !=0:
                 query = {
                        "bool": {
               "must": text,
                }}

        else: return 

        res = es.search(index="dhbb",query=query,size=n_max)
        print_results(res)

       
        

       
                
