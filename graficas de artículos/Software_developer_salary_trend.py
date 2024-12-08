import matplotlib.pyplot as plt
import pandas as pd

# Datos de porcentaje de uso de lenguajes de programación
data_share = {
    'Language': ['Scala', 'Go', 'Kotlin', 'C++', 'Rust', 'C', 'Shell scripting', 'Java', 'Python', 'SQL', 'Swift', 'Dart', 'TypeScript', 'JavaScript', 'C#', 'PHP', 'HTML/CSS'],
    'Share (%)': [60, 50, 41, 40, 40, 38, 38, 37, 36, 33, 32, 32, 32, 28, 28, 25, 24]
}

# Datos de tendencia de crecimiento en el último año (ficticios para mantener la estructura)
data_trend = {
    'Language': ['Scala', 'Go', 'Kotlin', 'C++', 'Rust', 'C', 'Shell scripting', 'Java', 'Python', 'SQL', 'Swift', 'Dart', 'TypeScript', 'JavaScript', 'C#', 'PHP', 'HTML/CSS'],
    '1-year Trend (%)': [2.1, 1.8, 1.5, 0.5, 1.0, 0.2, 0.3, -0.1, 1.6, 0.5, 0.4, 0.2, 0.1, -0.5, 0.3, -0.3, -0.2]
}

df_share = pd.DataFrame(data_share)
df_trend = pd.DataFrame(data_trend)

# Gráfico de participación de lenguajes
plt.figure(figsize=(10, 8))
plt.barh(df_share['Language'], df_share['Share (%)'], color='skyblue')
plt.xlabel('Share (%)')
plt.title('Participación de lenguajes de programación')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Gráfico de tendencias de crecimiento en un año
plt.figure(figsize=(10, 8))
plt.barh(df_trend['Language'], df_trend['1-year Trend (%)'], color='lightgreen')
plt.xlabel('Cambio en un año (%)')
plt.title('Tendencias de crecimiento de lenguajes de programación (último año)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
