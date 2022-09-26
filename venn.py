import matplotlib.pyplot as plt
from matplotlib_venn import venn2

venn2(subsets = (30, 110, 20), set_labels = ('grupo 1', 'grupo 2'), set-colors=('deeppink', 'lawngreen'), alpha=0.9)
plt.title("Diagrama de Venn")
plt.show()