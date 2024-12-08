import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
data = {
    'Language': ['JavaScript', 'Python', 'HTML/CSS', 'SQL', 'Java', 'Shell', 'TypeScript', 'C++', 'C#', 'C', 'PHP', 'Go', 
                 'Kotlin', 'Rust', 'Swift', 'Ruby', 'Scala', 'Objective-C'],
    '2017': [65, 32, 60, 42, 47, None, 12, 17, 20, 15, 30, 8, 2, None, 9, 10, 7, 7],
    '2018': [64, 41, 55, 47, 51, 29, 17, 18, 22, 16, 26, 12, 9, 2, 8, 8, 5, 4],
    '2019': [69, 49, 61, 56, 50, 40, 25, 20, 24, 17, 29, 18, 16, 5, 11, 11, 6, 5],
    '2020': [70, 55, 61, 56, 54, 39, 28, 27, 22, 23, 27, 19, 15, 7, 9, 8, 5, 4],
    '2021': [69, 52, 60, 54, 49, 37, 29, 23, 21, 19, 32, 17, 14, 6, 8, 6, 4, 3],
    '2022': [65, 53, 54, 49, 48, 34, 34, 25, 20, 20, 20, 17, 16, 9, 7, 6, 3, 2],
    '2023': [61, 54, 52, 52, 49, 34, 34, 24, 21, 19, 18, 17, 15, 10, 6, 6, 3, 2],
    'Likely to Adopt': [3, 5, 1, 2, 3, 1, 6, 4, 2, 2, 1, 9, 6, 10, 4, 1, 1, 0]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Definir los años
years = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Trazar las tendencias de lenguajes de programación
for language in df['Language']:
    plt.plot(years, df[df['Language'] == language][years].values.flatten(), label=language)

# Estilizar la gráfica
plt.title('Tendencias de Popularidad de Lenguajes de Programación')
plt.xlabel('Año')
plt.ylabel('Popularidad (%)')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
