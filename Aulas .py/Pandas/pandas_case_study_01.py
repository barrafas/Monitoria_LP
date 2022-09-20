import numpy as np
import pandas as pd
pd.options.display.max_columns = 5
pd.options.display.float_format = "{:.2f}".format

print("########################## Leitura ##########################")
df = pd.read_csv("movies.csv", parse_dates= ["release_date"])

print("Dataset: \n", df, sep="")
print("\n\nDataset DESCRIBE: \n", df.describe(), sep="")

print("\n\nPrimeiro Filme - Título: ", df["title"].iloc[0])
print("Primeiro Filme - Diretor: ", df["director"].iloc[0])
print("Primeiro Filme - Cast: ", df["cast"].iloc[0])

print("\nBudget: \n", df["budget_musd"].value_counts(dropna = False).head(20), sep="")
print("\nRevenue: \n", df["revenue_musd"].value_counts(dropna = False).head(20), sep="")
print("\nVote Average: \n", df["vote_average"].value_counts(dropna = False), sep="")
print("\nVote Count: \n", df["vote_count"].value_counts(), sep="")

df_mp = df[["title", "budget_musd", "revenue_musd", "vote_count", "vote_average", "popularity"]].copy()

df_mp["profit_musd"] = df["revenue_musd"].sub(df["budget_musd"])
df_mp["return"] = df["revenue_musd"].div(df["budget_musd"])

df_mp.columns = ["Title", "Budget", "Revenue", "Votes", "Average Rating", "Popularity", "Profit", "ROI"]

df_mp.set_index("Title", inplace = True)
df_mp["Budget"].fillna(0, inplace = True)
df_mp["Revenue"].fillna(0, inplace = True)
df_mp["Votes"].fillna(0, inplace = True)

print("#################################### Dataset: \n", df_mp, sep="")

#Qual o problema aqui?
print("\n\nAverage Rating", df_mp.sort_values(by = "Average Rating", ascending = False), sep="")
print("\n\nROI", df_mp.sort_values(by = "ROI", ascending = False), sep="")

#Corrigindo
print("\n\nAverage Rating - CORRIGIDO", df_mp[df_mp["Votes"] >= 100].sort_values(by = "Average Rating", ascending = False).head(5), sep="")
print("\n\nROI - CORRIGIDO", df_mp.loc[df_mp["Budget"] >= 2].sort_values(by = "ROI", ascending = False).head(5), sep="")

df_mp = df_mp.loc[(df_mp["Budget"] >= 2) & (df_mp["Votes"] >= 100)]
print("#################################### Dataset: \n", df_mp, sep="")

#Para os alunos
"""
Maior e Menor Receita
Maior e Menor Orçamento
Maior e Menor Lucro
Maior e Menor ROI
Melhor e pior Filme
"""

#Desafio: Melhores filmes de ação do Arnold Schwarzenegger
mask_df_genre = df["genres"].str.contains("Action")
mask_df_cast = df["cast"].str.contains("Arnold Schwarzenegger")

result = df.loc[mask_df_genre & mask_df_cast, ["title", "vote_average"]].sort_values(by = "vote_average", ascending = False).head(5)
print("Resultado: \n", result, sep="")

#Desafio: Filmes com mais longos do Steven Spielberg entre 1980 e 2000
mask_df_director = df["director"] == "Steven Spielberg"
mask_df_release = df["release_date"].between("1990-01-01", "2000-12-31")

result = df.loc[mask_df_director & mask_df_release, ["title", "runtime"]].sort_values(by = "runtime", ascending = False).head(5)
print("\n\nResultado: \n", result, sep="")