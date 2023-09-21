# importa a biblioteca urllib
from urllib.request import urlopen

# importa a biblioteca json
import json

# importa a biblioteca streamlit e aponta sua inicializacao
import streamlit as st

# importa a biblioteca pandas e aponta sua inicializacao
import pandas as pd

# armazena o endereço da consulta
url = "https://raw.githubusercontent.com/caiormaximo/json/main/json.json"

# armazena o retorno do endereço da consulta
response = urlopen(url)

# armazena o retorno da fonte de dados em JSON
# de um endereço para dados a serem tratados
data_dict = json.loads(response.read())

# verifica a quantidade total de elementos agrupados
total = len(data_dict)

# cria uma classe para identificacao dos lancamentos
# a serem tratados
class Lancamento:
    def __init__(self, data, lancamento1, lancamento2):
        self.data = data
        self.lancamento1 = lancamento1
        self.lancamento2 = lancamento2

# incializacao de lista para armazenar
#lancamentos procurados
lista = []

# iteracao para identificar lancamentos que
# atendem as premissas do cliente
for i in range(total):

                    # povoamento de novo objeto com lancamentos com valores absolutos
                    novoLancamento = Lancamento ((data_dict[i]["dataEfetiva"]), (data_dict[i]["valor"]),((data_dict[i]["valor"]).replace('-', '')))

                    # identificacao de lancamentos procurados
                    if novoLancamento.lancamento1 != novoLancamento.lancamento2:
                        matchLancamento = (novoLancamento.data,novoLancamento.lancamento1,novoLancamento.lancamento2)
                        lista.append(matchLancamento)

# criamos o data frame com pandas para povoar com os dados que queremos
df = pd.DataFrame.from_records (lista, columns=["Data Efetiva","Débito", "Crédito"])

# utilizando a biblioteca streamlit personalizamos a pagina web para entregar o resultado final
st.title('Selecao')
st.subheader('Lancamentos passíveis de tratamento')
st.markdown('Esta pagina irá retornar os lançamentos para tratamento '
            'atendendo aos parametros pre-definidos')
st.dataframe(df)
