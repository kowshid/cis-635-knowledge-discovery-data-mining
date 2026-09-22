import numpy as np

FILE = "matrix.bin"

# First 16 bytes = n_cells + n_genes
# Remaining bytes = matrix data
matrix = np.fromfile(FILE, dtype=np.uint64, offset=16)

nonzero = matrix[matrix != 0]

print(f"Total data elements : {matrix.size:,}")
print(f"Non-zero            : {nonzero.size:,}")
print(f"Zero                : {matrix.size - nonzero.size:,}")
print(f"Min non-zero        : {nonzero.min()}")
print(f"Max non-zero        : {nonzero.max()}")

# print("\nNon-zero values:")
# for value in nonzero:
#     print(value)