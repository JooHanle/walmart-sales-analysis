import pandas as pd

# Charger le fichier
file_path = "C:/Users/teo11/PROJETS/walmart-sales-analysis/data/Walmart_Sales.csv"
df = pd.read_csv(file_path)

# Afficher les premières lignes pour inspection
df.head()

# Vérification des valeurs manquantes
missing_values = df.isnull().sum()

# Vérification des doublons
duplicate_rows = df.duplicated().sum()

# Conversion de la colonne Date en format datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Standardisation des noms de colonnes
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Résumé des corrections effectuées
missing_values, duplicate_rows, df.dtypes

# Définir le chemin du fichier nettoyé
cleaned_file_path = "C:/Users/teo11/PROJETS/walmart-sales-analysis/data/Walmart_Sales_Cleaned.csv"

# Exporter le DataFrame nettoyé
df.to_csv(cleaned_file_path, index=False)

# Retourner le chemin du fichier
cleaned_file_path

import plotly.express as px

# Recharger le fichier nettoyé pour garantir que nous utilisons les bonnes données
df_cleaned = pd.read_csv("C:/Users/teo11/PROJETS/walmart-sales-analysis/data/Walmart_Sales_Cleaned.csv")

# Vérifier que la colonne date est bien en datetime
df_cleaned["date"] = pd.to_datetime(df_cleaned["date"])

# Afficher les premières lignes pour confirmer que tout est correct
df_cleaned.head()

import plotly.graph_objects as go

# 1. Évolution des ventes au fil du temps (tendance globale)
fig_sales_trend = px.line(df_cleaned.groupby("date")["weekly_sales"].sum().reset_index(),
                          x="date", y="weekly_sales",
                          title="Évolution des ventes hebdomadaires",
                          labels={"weekly_sales": "Ventes hebdomadaires", "date": "Date"},
                          template="plotly_dark")

# 2. Comparaison des ventes entre les magasins (moyenne des ventes par magasin)
fig_store_sales = px.bar(df_cleaned.groupby("store")["weekly_sales"].mean().reset_index(),
                         x="store", y="weekly_sales",
                         title="Moyenne des ventes par magasin",
                         labels={"weekly_sales": "Ventes moyennes", "store": "Magasin"},
                         template="plotly_dark")

# 3. Impact des jours fériés sur les ventes
fig_holiday_sales = px.box(df_cleaned, x="holiday_flag", y="weekly_sales",
                           title="Impact des jours fériés sur les ventes",
                           labels={"holiday_flag": "Jour Férié (0 = Non, 1 = Oui)", "weekly_sales": "Ventes hebdomadaires"},
                           template="plotly_dark")

# 4. Relation entre température et ventes
fig_temp_sales = px.scatter(df_cleaned, x="temperature", y="weekly_sales",
                            title="Influence de la température sur les ventes",
                            labels={"temperature": "Température (°F)", "weekly_sales": "Ventes hebdomadaires"},
                            template="plotly_dark", trendline="ols")

# 5. Influence du prix du carburant sur les ventes
fig_fuel_sales = px.scatter(df_cleaned, x="fuel_price", y="weekly_sales",
                            title="Impact du prix du carburant sur les ventes",
                            labels={"fuel_price": "Prix du carburant ($)", "weekly_sales": "Ventes hebdomadaires"},
                            template="plotly_dark", trendline="ols")

# Affichage des graphiques
fig_sales_trend.show()
fig_store_sales.show()
fig_holiday_sales.show()
fig_temp_sales.show()
fig_fuel_sales.show()
