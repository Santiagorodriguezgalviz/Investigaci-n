import matplotlib.pyplot as plt
import pandas as pd

# Datos de participación de lenguajes de programación
data_share = {
    'Language': ['Python', 'Java', 'JavaScript', 'C#', 'C/C++', 'R', 'PHP', 'TypeScript', 'Swift', 'Rust', 'Objective-C', 'Go', 'Kotlin', 'Matlab', 'Ruby',
                 'VBA', 'Powershell', 'Ada', 'Dart', 'Lua', 'Abap', 'Scala', 'Visual Basic', 'Julia', 'Groovy', 'Cobol', 'Perl', 'Delphi/Pascal', 'Haskell'],
    'Share (%)': [29.66, 15.64, 8.3, 6.64, 6.46, 4.66, 4.35, 2.96, 2.69, 2.65, 2.45, 2.08, 1.95, 1.45, 0.99, 0.97, 0.96, 0.96, 0.94, 0.69, 0.59, 0.57, 
                  0.47, 0.29, 0.23, 0.21, 0.08, 0.07, 0.06]
}

# Datos de tendencia de los lenguajes en el último año
data_trend = {
    'Language': ['Python', 'Java', 'JavaScript', 'C#', 'C/C++', 'R', 'PHP', 'TypeScript', 'Swift', 'Rust', 'Objective-C', 'Go', 'Kotlin', 'Matlab', 'Ruby', 
                 'VBA', 'Powershell', 'Ada', 'Dart', 'Lua', 'Abap', 'Scala', 'Visual Basic', 'Julia', 'Groovy', 'Cobol', 'Perl', 'Delphi/Pascal', 'Haskell'],
    '1-year Trend (%)': [1.6, -0.2, -1.0, -0.1, -0.2, 0.2, -0.5, -0.0, 0.0, 0.6, 0.2, 0.2, 0.2, -0.1, -0.1, 0.0, 0.1, -0.1, -0.0, 0.1, -0.0, -0.1, -0.1, 
                         -0.1, -0.1, -0.0, -0.2, -0.1, -0.2]
}

df_share = pd.DataFrame(data_share)
df_trend = pd.DataFrame(data_trend)

# Gráfico de participación de lenguajes
plt.figure(figsize=(10, 8))
plt.barh(df_share['Language'], df_share['Share (%)'], color='skyblue')
plt.xlabel('Share (%)')
plt.title('Participación de lenguajes de programación (Sep 2024)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Gráfico de tendencias de crecimiento en un año
plt.figure(figsize=(10, 8))
plt.barh(df_trend['Language'], df_trend['1-year Trend (%)'], color='lightgreen')
plt.xlabel('Cambio en un año (%)')
plt.title('Tendencias de crecimiento de lenguajes de programación (2023 a 2024)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
