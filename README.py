# Análise de Dados com Python
# Usado Jupyter


import pandas as pd

# Passo 1: Importar Base de Dados
tabela= pd.read_csv("telecom_users.csv")

# Passo 2: Vizualizar Base de Dados
# - Entender as informações que você tem disponibilidade
# - Descobrir as Cagadas/erros da base de dados
# axis -> 0 = linha; axis - > 1 = Coluna

tabela= tabela.drop("Unnamed: 0", axis=1)
display(tabela)

# Passo 3: Tratamento de Dados 
#resolver valores que estão sendo reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],errors="coerce")

# resolver valores vazios 

# coluna que TODOS os valores forem vazios eu vou excluir
# axis -> 0 = linha; axis - > 1 = Coluna
tabela = tabela.dropna(how= "all", axis= 1)

# linhas que tem PELO MENOS 1 valor vazio (que possuem ALGUM valor vazio)
tabela = tabela.dropna(how="any", axis= 0)

print(tabela.info())

# Passo 4: Análise Inicial do Problema
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Análise Detalhada - Descobrir as Causas do Cancelamento
# comparar cada coluna da base de dados com a coluna Churn
import plotly.express as px

# cria o gráfico
for coluna in tabela.columns:
    # para cada coluna da tabela, criar um gráfico
    grafico = px.histogram(tabela,x=coluna, color="Churn", text_auto=True)
    # exibe o gráfico
    grafico.show()
    
    
