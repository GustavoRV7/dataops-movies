import pandas as pd
import psycopg2

# 1. CONEXIÓN A LA BASE DE DATOS
# 2. CARGA DE DATOS DESDE SQL SERVER
query = "SELECT * FROM movies"
df = pd.read_sql(query, conn)

# 3. LIMPIEZA DE DATOS
df = df[df['date_added'].notnull()]
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna(df['rating'].mode()[0], inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'])

# 4. TRANSFORMACIONES

# a. Conteo por tipo (película o serie)
df_type_count = df['type'].value_counts().reset_index()
df_type_count.columns = ['type', 'count']

# b. Top 10 países con más contenido
df_country_top = (
    df['country']
    .str.split(', ', expand=True)
    .stack()
    .value_counts()
    .head(10)
    .reset_index()
)
df_country_top.columns = ['country', 'count']

# c. Contenido por año de incorporación
df_added_by_year = df['date_added'].dt.year.value_counts().sort_index().reset_index()
df_added_by_year.columns = ['year_added', 'count']

# d. Contenido por clasificación
df_rating_count = df['rating'].value_counts().reset_index()
df_rating_count.columns = ['rating', 'count']

# e. Top 10 directores con más contenido
df_top_directors = df['director'].value_counts().head(10).reset_index()
df_top_directors.columns = ['director', 'count']

# f. Top 10 elencos más frecuentes
df_top_cast = (
    df['cast']
    .str.split(', ', expand=True)
    .stack()
    .value_counts()
    .head(10)
    .reset_index()
)
df_top_cast.columns = ['actor', 'count']

with pd.ExcelWriter("disney_data_summary.xlsx", engine="openpyxl") as writer:
    df_type_count.to_excel(writer, sheet_name="Tipo_Contenido", index=False)
    df_country_top.to_excel(writer, sheet_name="Top_Paises", index=False)
    df_added_by_year.to_excel(writer, sheet_name="Contenido_Por_Año", index=False)
    df_rating_count.to_excel(writer, sheet_name="Clasificaciones", index=False)
    df_top_directors.to_excel(writer, sheet_name="Top_Directores", index=False)
    df_top_cast.to_excel(writer, sheet_name="Top_Actores", index=False)

print("Exportación completa a 'disney_data_summary.xlsx'")
