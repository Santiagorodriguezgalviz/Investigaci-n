import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar el estilo y tema de los gráficos
sns.set_theme(style="darkgrid")  # Define un estilo de fondo oscuro con líneas de cuadrícula.

# Datos de uso de lenguajes de programación más populares entre 2017 y 2023
# Basados en fuentes como GitHub, Stack Overflow y el índice TIOBE
data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023] * 7,  # Repetir los años 7 veces (uno por cada lenguaje).
    'Language': ['Python'] * 7 + ['JavaScript'] * 7 + ['Java'] * 7 + 
                ['C++'] * 7 + ['PHP'] * 7 + ['Ruby'] * 7 + ['Swift'] * 7,
    # Lista con los porcentajes de uso de cada lenguaje para cada año.
    'Usage_Percentage': [
        # Python
        32.2, 35.7, 39.4, 44.1, 48.2, 48.07, 49.3,
        # JavaScript
        62.5, 69.8, 67.8, 63.1, 64.9, 65.6, 63.8,
        # Java
        45.3, 45.3, 41.1, 38.4, 35.35, 33.27, 30.5,
        # C++
        34.2, 34.4, 31.0, 31.4, 27.86, 27.98, 27.7,
        # PHP
        28.1, 30.7, 26.4, 25.8, 21.98, 20.87, 20.1,
        # Ruby
        10.5, 10.1, 8.4, 7.1, 6.75, 6.05, 5.8,
        # Swift
        8.1, 8.3, 8.1, 5.9, 5.1, 4.91, 4.7
    ]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)  # Estructura tabular que organiza los datos.

# Crear un gráfico de líneas
sns.lineplot(data=df, x='Year', y='Usage_Percentage', hue='Language', marker='o', linewidth=2.5)
# - `data=df`: Usar los datos del DataFrame.
# - `x='Year'`: El eje X representará los años.
# - `y='Usage_Percentage'`: El eje Y representará los porcentajes de uso.
# - `hue='Language'`: Diferenciar las líneas por el lenguaje de programación.
# - `marker='o'`: Colocar un marcador circular en cada punto de los datos.
# - `linewidth=2.5`: Ajustar el grosor de las líneas.

# Personalizar el gráfico
plt.title('Programming Languages Usage Trends (2017-2023)', fontsize=16, pad=20)  # Título del gráfico
plt.xlabel('Year', fontsize=12)  # Etiqueta del eje X
plt.ylabel('Usage Percentage (%)', fontsize=12)  # Etiqueta del eje Y
plt.grid(True, linestyle='--', alpha=0.7)  # Mostrar una cuadrícula con líneas punteadas y opacidad reducida.
plt.legend(title='Programming Language', title_fontsize=12, fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
# - `title`: Título de la leyenda.
# - `bbox_to_anchor`: Posicionar la leyenda fuera del gráfico.
# - `loc='upper left'`: Colocar la leyenda en la parte superior izquierda.

# Añadir proyecciones para el año 2024
plt.axvline(x=2023, color='gray', linestyle='--', alpha=0.5)  # Línea vertical que indica el año 2023.
plt.text(2023.1, 50, 'Proyecciones 2024:', fontsize=10)  # Texto explicativo para las proyecciones.
plt.text(2023.1, 47, '• Python: Crecimiento continuo en IA/ML', fontsize=9)
plt.text(2023.1, 44, '• JavaScript: Dominio estable en desarrollo web', fontsize=9)
plt.text(2023.1, 41, '• Java: Declive gradual pero sigue siendo esencial', fontsize=9)
plt.text(2023.1, 38, '• C++: Estable en programación de sistemas', fontsize=9)

# Ajustar el diseño para evitar cortes de texto
plt.tight_layout()  # Asegurarse de que los elementos gráficos no se superpongan.

# Guardar el gráfico en un archivo
plt.savefig('programming_languages_trends.png', bbox_inches='tight', dpi=300)  # Guardar el gráfico con alta resolución.
plt.show()  # Mostrar el gráfico en pantalla.

# Mostrar conclusiones en consola
print("\nConclusiones Principales:")
print("1. Python muestra un crecimiento constante, impulsado por la adopción en IA/ML")
print("2. JavaScript mantiene su posición como el lenguaje más utilizado")
print("3. Java muestra un declive gradual pero sigue siendo importante")
print("4. Los lenguajes más nuevos como Swift muestran tasas de adopción más lentas")

# Mostrar predicciones para 2024 en consola
print("\nPredicciones 2024:")
print("- Python: Se espera que continúe creciendo debido a la demanda de IA/ML")
print("- JavaScript: Mantendrá el liderazgo en desarrollo web")
print("- Java: Puede estabilizarse debido a aplicaciones empresariales")
print("- C++: Seguirá siendo crucial para la programación de sistemas")
