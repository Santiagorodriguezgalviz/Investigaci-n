import matplotlib.pyplot as plt
import pandas as pd

# Datos de la tendencia histórica de puntajes de ranking (2013-2024)
years = list(range(2013, 2025))
rank_scores = [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52]

# Crear la gráfica de tendencia histórica
plt.figure(figsize=(8, 5))
plt.plot(years, rank_scores, marker='o', linestyle='-', color='b', label="Ranking Scores (%)")
plt.title('Tendencia Histórica de Ranking Scores (2013-2024)')
plt.xlabel('Año')
plt.ylabel('Ranking (%)')
plt.grid(True)
plt.legend()
plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()

# Datos de la distribución de licencias comerciales vs código abierto (2024)
labels = ['Comercial', 'Código Abierto']
sizes = [50.4, 49.6]  # Porcentajes de popularidad en septiembre de 2024
colors = ['#ff9999','#66b3ff']

# Crear la gráfica de pastel para la distribución de licencias
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Distribución de Licencias en 2024')
plt.axis('equal')  # Asegura que el gráfico sea un círculo.
plt.show()

# Datos de sistemas top por licencia en 2024
commercial_data = {
    'System': ['Oracle', 'Microsoft SQL Server', 'Snowflake', 'IBM Db2', 'Microsoft Access'],
    'Score': [1287, 808, 134, 123, 94]
}

open_source_data = {
    'System': ['MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'Elasticsearch'],
    'Score': [1029, 644, 410, 149, 129]
}

df_commercial = pd.DataFrame(commercial_data)
df_open_source = pd.DataFrame(open_source_data)

# Gráfico de barras para los sistemas con licencia comercial
plt.figure(figsize=(10, 6))
plt.barh(df_commercial['System'], df_commercial['Score'], color='#ff9999')
plt.title('Top Sistemas por Licencia Comercial (2024)')
plt.xlabel('Puntaje')
plt.ylabel('Sistema')
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# Gráfico de barras para los sistemas de código abierto
plt.figure(figsize=(10, 6))
plt.barh(df_open_source['System'], df_open_source['Score'], color='#66b3ff')
plt.title('Top Sistemas por Licencia Código Abierto (2024)')
plt.xlabel('Puntaje')
plt.ylabel('Sistema')
plt.grid(axis='x')
plt.tight_layout()
plt.show()
