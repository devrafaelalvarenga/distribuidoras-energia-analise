import pandas as pd

# Exemplo de leitura
url_usinas = "https://dadosabertos.aneel.gov.br/dataset/283a0172-3966-49e7-ae45-d2885ad17b03/resource/20ef769f-a072-489d-9df4-c834529f8a78/download/agentes-geracao-energia-eletrica.csv"
url_tarifas = "https://dadosabertos.aneel.gov.br/dataset/5a583f3e-1646-4f67-bf0f-69db4203e89e/resource/fcf2906c-7c32-4b9b-a637-054e7a5234f4/download/tarifas-homologadas-distribuidoras-energia-eletrica.csv"
url_indicadores = "https://dadosabertos.aneel.gov.br/dataset/d5f0712e-62f6-4736-8dff-9991f10758a7/resource/4493985c-baea-429c-9df5-3030422c71d7/download/indicadores-continuidade-coletivos-2020-2029.csv"

df = pd.read_csv(url_tarifas, encoding="latin1", sep=";")
print(df.head())
print(df.columns)
print(df.info())

"""
agentes-geracao-energia-eletrica
URL: https://dadosabertos.aneel.gov.br/dataset/283a0172-3966-49e7-ae45-d2885ad17b03/resource/20ef769f-a072-489d-9df4-c834529f8a78/download/agentes-geracao-energia-eletrica.csv
Lista de Agentes de Geração de Energia Elétrica relacionando as Usinas e seus respectivos CEGs, CNPJ e Percentual de Participação por agente na propriedade do empreendimento e o regime de exploração do mesmo em relação a este empreendimento.

tarifas-homologadas-distribuidoras-energia-eletrica.csv
URL: https://dadosabertos.aneel.gov.br/dataset/5a583f3e-1646-4f67-bf0f-69db4203e89e/resource/fcf2906c-7c32-4b9b-a637-054e7a5234f4/download/tarifas-homologadas-distribuidoras-energia-eletrica.csv
Dataset description:
Apresenta os valores das Tarifas de Energia - TE e das Tarifas de Uso do Sistema de Distribuição - TUSD, resultantes dos processos de reajustes tarifários das distribuidoras de energia...

indicadores-continuidade-coletivos-2020-2029
URL: https://dadosabertos.aneel.gov.br/dataset/d5f0712e-62f6-4736-8dff-9991f10758a7/resource/4493985c-baea-429c-9df5-3030422c71d7/download/indicadores-continuidade-coletivos-2020-2029.csv
O conjunto de dados apresenta os valores apurados dos indicadores coletivos de continuidade DEC (Duração Equivalente de Interrupção por Unidade Consumidora), expresso em horas e centésimos de horas, e FEC (Frequência Equivalente de Interrupção por Unidade Consumidora), expresso em número de interrupções e centésimos do número de interrupções. Também são fornecidas as parcelas desagregadas dos indicadores.
"""
