import os
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import seaborn as sns

BASE_DIR = os.path.abspath(".")
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
DATA_DIR = os.path.join(BASE_DIR,'data')
SQL_DIR = os.path.join(BASE_DIR, 'src', 'sql')
PYTHON_DIR = os.path.join(BASE_DIR, 'src', 'python')
TABELAS_DIR = os.path.join(BASE_DIR,'tabelas')

str_conn = 'sqlite:///' + os.path.join(DATA_DIR, 'banco.db') + '?check_same_thread=False'
engine = sqlalchemy.create_engine(str_conn)
conn = engine.connect()

nome_query = 'create_abt'
with open( os.path.join(SQL_DIR, f'{nome_query}.sql'), 'rb') as query_file:
        query = query_file.read().decode("UTF-8")

data = pd.read_sql(query, conn)

data = data.dropna()

features = data.columns[2:,]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(data[features])
scaled_features_df = pd.DataFrame(scaled_features, columns=features)


kmeans = KMeans(
     init="random",
     n_clusters=5,
     n_init=10,
     max_iter=300,
     random_state=42
 )

kmeans.fit(scaled_features)

data["Classificacao"] = kmeans.labels_
scaled_features_df["Classificacao"] = kmeans.labels_

features = data.columns[2:,]
#data_impressao = data[features].pivot_table(index = "Classificacao")
data_impressao = scaled_features_df.pivot_table(index = "Classificacao")

#ax = sns.heatmap(data[features], linewidth=0.5)
ax = sns.heatmap(data_impressao)
plt.show()