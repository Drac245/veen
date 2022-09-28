import numpy as np
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

# punto A
D = {45,20,60,55}
B = {15,100,40,55}
F = {50,100,80,55}

interseccion_D_B = ((D & B) ^ F)

print(interseccion_D_B)

venn2(subsets = (80,50,100), set_labels = ('conjunto D’', 'conjunto B’', 'conjunto F’'), set_colors=('deeppink', 'lawngreen'), alpha=0.9)
plt.title("Diagrama de Venn Punto A")
plt.show()

#punto B
E={0,40,70,55}
A={30,50,0}

union_A_E = A | E
print(union_A_E) 
#{0, 50, 70, 55, 40, 30}
venn2(subsets = (3, 14, 30), set_labels = ('conjunto A unido E’', 'conjunto A unido E’'), set_colors=('lawngreen', 'lawngreen'), alpha=0.9)
plt.title("Diagrama de Venn Punto B    {0, 50, 70, 55, 40, 30}")
plt.show()