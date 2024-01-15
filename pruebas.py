import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Datos para los conjuntos
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Crear el diagrama de Venn
venn2([set1, set2], set_labels=('Conjunto 1', 'Conjunto 2'))

# Mostrar el diagrama
plt.show()
