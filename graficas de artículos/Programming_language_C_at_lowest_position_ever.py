import matplotlib.pyplot as plt
import pandas as pd

# Datos de Rankings y Ratings en 2024
data = {
    'Rank (Sep 2024)': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'Rank (Sep 2023)': [1, 3, 4, 2, 5, 6, 7, 12, 10, 11, 15, 13, 8, 17, 18, 19, 14, 20, 21, 16],
    'Programming Language': ['Python', 'C++', 'Java', 'C', 'C#', 'JavaScript', 'Visual Basic', 'Go', 'SQL', 'Fortran', 
                             'Delphi/Object Pascal', 'MATLAB', 'PHP', 'Rust', 'R', 'Ruby', 'Scratch', 'Kotlin', 'COBOL', 'Swift'],
    'Rating (Sep 2024)': [20.17, 10.75, 9.45, 8.89, 6.08, 3.92, 2.70, 2.35, 1.94, 1.78, 1.77, 1.47, 1.46, 1.32, 1.20, 
                          1.13, 1.11, 1.10, 1.09, 1.08],
    'Change (Rating)': [6.01, 0.09, -0.04, -2.38, -1.22, 0.62, 0.48, 1.16, 0.50, 0.49, 0.75, 0.28, -0.09, 0.35, 0.23, 
                        0.18, 0.03, 0.20, 0.22, 0.09]
}

df = pd.DataFrame(data)

# Gráfico de Rankings en 2024 comparado con 2023
plt.figure(figsize=(10, 6))
plt.barh(df['Programming Language'], df['Rank (Sep 2023)'], color='lightgray', label='Rank (Sep 2023)')
plt.barh(df['Programming Language'], df['Rank (Sep 2024)'], color='skyblue', label='Rank (Sep 2024)')
plt.xlabel('Ranking')
plt.title('Comparación de Ranking de Lenguajes de Programación (2023 vs 2024)')
plt.gca().invert_yaxis()
plt.legend()
plt.tight_layout()
plt.show()

# Gráfico de cambios en Rating (%) entre 2023 y 2024
plt.figure(figsize=(10, 6))
plt.barh(df['Programming Language'], df['Change (Rating)'], color='lightgreen')
plt.xlabel('Cambio en Rating (%)')
plt.title('Cambio en Rating (%) de Lenguajes de Programación (2023 a 2024)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
