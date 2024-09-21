import matplotlib.pyplot as plt

# Datos para el Artículo 20
bad_smells = ['Código Duplicado', 'Acoplamiento Elevado', 'Clases Grandes', 'Métodos Largos']
valores = [35, 30, 20, 15]  # Proporción de bad smells

plt.figure(figsize=(10, 6))
plt.bar(bad_smells, valores, color=['#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
plt.xlabel('Bad Smells en MVC')
plt.ylabel('Proporción')
plt.title('Artículo 20: Caracterización y Detección Automática de Bad Smells MVC')
plt.show()
