import pandas as pd
import matplotlib.pyplot as plt

# Datos del CSV proporcionado
data = {
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'DBMS': ['Oracle', 'MySQL', 'Microsoft SQL Server', 'PostgreSQL', 'MongoDB', 'Redis', 'Snowflake', 'Elasticsearch', 
             'IBM Db2', 'SQLite', 'Apache Cassandra', 'Microsoft Access', 'Splunk', 'Databricks', 'MariaDB', 
             'Microsoft Azure SQL Database', 'Amazon DynamoDB', 'Apache Hive', 'Google BigQuery', 'FileMaker'],
    'Score': [1286.59, 1029.49, 807.76, 644.36, 410.24, 149.43, 133.72, 128.79, 123.05, 103.35, 98.94, 93.76, 
              93.02, 84.24, 83.44, 72.95, 70.06, 53.07, 52.67, 45.20],
    'Change_Sep_2024_Aug_2024': [28.11, 2.63, -7.41, 6.97, -10.74, -3.28, -2.25, -1.04, 0.04, -1.44, 1.94, 
                                 -2.61, -3.08, -0.22, -3.09, -2.08, 1.15, -2.17, -2.86, -1.47],
    'Change_Sep_2024_Sep_2023': [45.72, -82.00, -94.45, 23.61, -29.18, -14.26, 12.83, -10.20, -13.67, -25.85, 
                                 -11.11, -34.81, 1.63, 9.06, -17.01, -9.78, -10.85, -18.76, -3.80, -8.40]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Trazar la columna de cambio en Score
plt.plot(df['DBMS'], df['Change_Sep_2024_Sep_2023'], marker='o', label='Cambio (Sep 2024 - Sep 2023)')
plt.plot(df['DBMS'], df['Change_Sep_2024_Aug_2024'], marker='x', label='Cambio (Sep 2024 - Aug 2024)')

# Estilizar la gráfica
plt.title('Tendencia de DBMS por Cambios en Puntuación')
plt.xlabel('DBMS')
plt.ylabel('Cambio en Puntuación')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
