#%%
import yaml
import json
from datetime import datetime
from os import listdir
from os.path import isfile, join
import re

#Dados do datayaml
#%%
# Lendo os dados do arquivo .yaml do trabalho passado
with open("data/data.yaml", encoding="utf8") as file:
    data = file.read()

# Obtendo a data de hoje
now = datetime.now().strftime("%d/%m/%Y")


def format_date(dictionary:dict):
    """Corrige erros de formatação da data

    Parameters
    ----------
    dictionary : dict
        dicionario com datas nas chaves 'birthdate'
    """
    # Convertendo data para string
    date = str(dictionary['birthdate'])
    # Tentando converter no formato dd/mm/yyyy
    try:
        # Convertendo string para formato date time
        date_object = datetime.strptime(date, "%d/%m/%Y")
        # Convertendo datetime para string, mas com formatação correta
        dictionary["birthdate"] = date_object.strftime("%d/%m/%Y")
    except ValueError:
        # Tentando converter no formato mm/yyyy
        try:
            # 
            date_object = datetime.strptime(date, "%m/%Y")
            dictionary["birthdate"] = date_object.strftime("%m/%Y")
        # Obtendo data no formato yyyy
        except ValueError:
            dictionary["birthdate"] = date


documents = {}
for dictionary in yaml.safe_load_all(data):
    if dictionary is None:
        continue

    dictionary["timestamp"] = now
    
    if "birthdate" in dictionary:
        # print(dictionary["birthdate"])
        format_date(dictionary)

        documents[dictionary["document"]] = dictionary

#%%
def get_files_lists(folder:str)->list:
    # Armazenando em uma lista todos os arquivos
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    return onlyfiles

def get_header_string(file_path:str)->tuple:
    """A partir da localização do text file, retorna o cabeçalho e texto do arquivo separados

    Parameters
    ----------
    file_path : str
        Localização do text file

    Returns
    -------
    tuple
        Cabeçalho e corpo do texto separados
    """
    with open(file_path) as file:
        # Lendo conteudo do texto 
        text = file.read()
        # Regex para obter o cabeçalho que está entre "---"
        header = re.findall("(?s)(?<=---)(.*?)(?=---)", text)[0]
        # Obtendo o texto
        only_text = text.replace(header, "")

    return header, only_text

# Caminho da pasta para o DHBB
mypath ="/home/luiz/Desktop/dhbb/text"
# Obtendo a lista de documentos
onlyfiles = get_files_lists(mypath)

for num, name_file in enumerate(onlyfiles):
    # obtendo o id do documento
    document_id = int(name_file.replace(".text", ""))
    # Reconstruindo o caminho até o arquivo
    file_path = f"{mypath}/{name_file}"
    # obtendo o cabeçalho com informações e o texto
    header, text = get_header_string(file_path)
    # Convertendo as informações do cabeçalho em um dicionário
    header_data = yaml.full_load(header)
    # Adicionando cada informação do cabeçalho ao dicionário de chave correspondente
    for item in header_data.items():
        try:
            documents[document_id][item[0]] = item[1]
        except KeyError:
            # Se o dicionario não possuir a chave, é criado um novo campo com a chave para adicionar as informações
            documents[document_id] = dict()
            documents[document_id][item[0]] = item[1]
    
    # Adicionando o texto a chave correspondente
    documents[document_id]["text"] = text
    


# %%
# Exportando dicionario para o formato .json
with open("data/json_output.json", "w", encoding="utf8") as json_file:
    json.dump(documents, json_file, ensure_ascii=False, indent=4)
