"""
Módulo da interface gráfica
Feito através do Streamlit
"""

import streamlit as st
from datetime import datetime
from Modules.queries import render_filter_fields,render_search_field,query_search
from Modules.options import tipo_list, subtipo_list, cargos_list

# configurações de layout
st.set_page_config(
        page_title="DHBB | Busca",
        page_icon="img/favicon.png",
        layout="wide",
)

# header 
st.image("img/logo.jpg")
st.title("Consulta ao DHBB")
st.write("Consulta ao Dicionario Historico-Biografico Brasileiro (DHBB)")

# campo buscas texto 
general_search =  st.text_input(label="Busca no texto")

# campo para config adicionais
with st.expander("Configurações"):
        max_n = st.slider("Número máximo de resultados",min_value=1,max_value=1000,step=1,value=30)
        operator = st.radio("Operador de busca no texto",("OR","AND"))
       
# campos para outras buscas 
st.sidebar.title("Filtros")
st.sidebar.write("Preencha somente os campos que desejar. A busca será realizada dinamicamente.")

# campos de filtros
nome = st.sidebar.text_input(label="Nome")

autor = st.sidebar.text_input(label="Autor")

birthdate_option = st.sidebar.radio("Filtrar aniversário por:",('Nenhum','Ano'))

if birthdate_option == "Ano":
        birthdate = st.sidebar.number_input("Ano de nascimento",max_value=2021,value=1900,step=1)
else:
        birthdate = ""

birthplace = st.sidebar.text_input("Origem")
cargo = st.sidebar.selectbox(label="Cargo",options=cargos_list)
tipo = st.sidebar.selectbox(label="Tipo",options=tipo_list)
subtipo = st.sidebar.selectbox(label="Subtipo",options=subtipo_list)

natureza = st.sidebar.radio("Natureza",('Todos','biográfico', 'temático'))
if natureza == "Todos": natureza = ""

genero = st.sidebar.radio("Gênero",('Todos','f', 'm'))
if genero == "Todos": genero = ""

# cria um dicionário com os filtros
args_dict ={"name":nome, "autor":autor,
                        "birthdate":birthdate,
                        "birthplace":birthplace,
                        "cargos":cargo,
                        "tipo":tipo,
                        "subtipo":subtipo,
                        "natureza":natureza,
                        "sexo":genero}

# realiza a busca com base nos campos preenchidos
text = render_search_field(general_search,operator) 
args = render_filter_fields(args_dict)
query_search(text,args,max_n)










