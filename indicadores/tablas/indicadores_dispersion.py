

# Tablas
def general_range(data):
    """Calcula el rango"""
    maximo = data.max(numeric_only=True)
    minimo = data.min(numeric_only=True)
    rango = maximo - minimo
    print('Range')
    print('**********************')
    print(rango, '\n')
    print('Maximum')
    print('----------------------')
    print(maximo, '\n')
    print('Minimum')
    print('----------------------')
    print(minimo, '\n')

