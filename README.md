# 🎬 Proyecto DataOps – Disney+ ETL Pipeline

Este proyecto implementa un pipeline ETL automatizado para procesar y analizar datos de títulos disponibles en la plataforma Disney+, utilizando Python, Docker, Git y Jenkins como parte de una solución basada en DataOps.

## 📌 Objetivo

Extraer datos desde una base de datos **PostgreSQL** con información de películas y series de Disney+, transformarlos en distintos reportes analíticos y exportarlos automáticamente a un archivo Excel estructurado. 

---

## ⚙️ Tecnologías Utilizadas

- 🐍 Python 3 (ETL)
- 🐳 Docker (Contenerización)
- 🛠️ Jenkins (Automatización CI/CD)
- 🗄️ PostgreSQL (Fuente de datos)
- 🧪 Pandas / OpenPyXL
- 🗃️ Git + GitHub (Control de versiones)

---

## 🔄 Flujo ETL

### 1. Extracción
Se conecta a una base de datos PostgreSQL y se extrae la tabla `movies`.

### 2. Transformación
Se realizan limpiezas y transformaciones para obtener:

- `df_country_top`: Top 10 países con más contenido.
- `df_added_by_year`: Cantidad de títulos agregados por año.
- `df_rating_count`: Conteo de títulos por clasificación.
- `df_top_directors`: Directores con más títulos.
- `df_top_cast`: Actores y actrices más frecuentes.

### 3. Carga
Se exportan todos los resultados a un archivo Excel llamado `disney_data_summary.xlsx`, con cada reporte en una hoja diferente.

---