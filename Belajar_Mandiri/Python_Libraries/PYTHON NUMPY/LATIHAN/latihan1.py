import numpy as np

matriks = np.array([[4, 7],[2, 6]])
print(matriks)

det = np.linalg.det(matriks)
print(f"\ndeterminannya adalah {det}")