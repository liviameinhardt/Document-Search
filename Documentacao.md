# Recuperação de Documentos



## Execução
Os passos a seguir permitem executar o programa criado para a alternativa 1.

1. Instalar e configurar o [Elastic Search](https://phoenixnap.com/kb/how-to-install-elk-stack-on-ubuntu). 


2. Iniciar o Elastic Search
```
sudo systemctl start elasticsearch.service
```

3. Instalar biblioteca do ElasticSearch para Python
```
pip install elasticsearch
```

4. Executar o script configure_elastic.py para indexar os conteúdo do DHBB no ELK
```
python3 Modules/configure_elastic.py
```

5. Instalar o [Streamlit](streamlit.io), utilizado para construir a interface:
```
pip install streamlit
```

6. Iniciar a interface:
```
streamlit run index.py
```

O último comando abrirá a interface do programa desenvolvido no browser:

![pagina inicial](img/paginainicial.png)

## Funcionamento 

### Busca de texto
A barra de pesquisa permite fazer buscas no texto dos documentos. Nas configurações, você pode selecionar a opção de busca "OR" ou a opção "AND" para as palavras passadas nesse campo. 

####  Exemplo
Selecionando "OR" e pesquisando por "presidente ontem", a busca retornará os textos que contém presidente OU ontem. Ou seja, não necessáriamente ambas as palavras estão presentes nos textos. ALternativamente, selecionando "AND" ambas as palavras estarão presentes nos resultados.

### Filtros
Os campos de filtro podem ser utilizados para filtras os resultados da busca de texto, explicada anteriormente ou de forma independente, filtrando, assim, todos os textos disponíveis. 


## Organização do Repositório
### data
Esta pasta contem os dados do DHBB, em formato json, utilizados para a indexação dos textos. Esse arquivo foi criado a partir do script yaml_to_json.py em Modules.

### Modules
Esta pasta contém scripts utilizados para a execução do programa, o que inclui as configurações do backend, o pré-processamento dos arquivos e a conexão da interface com o elastic search.

### img
Esta pasta contém imagens utilizadas na documentação e na interface.

### .streamlit
Essa pasta contém somente algumas configurações de design da interface. 