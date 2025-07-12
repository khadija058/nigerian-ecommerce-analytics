import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Testing libraries...")
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)
print("All libraries work!")

# Create simple data
data = {'sales': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)
print(df)
