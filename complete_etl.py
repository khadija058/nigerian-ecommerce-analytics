import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

print("🚀 Nigerian E-Commerce Complete ETL Pipeline")
print("=" * 50)

# 1. EXTRACT
print("📥 STEP 1: EXTRACTING DATA...")
try:
    df = pd.read_excel('Nigerian E-Commerce Dataset.xlsx')
    print(f"✅ Data extracted from current directory")
except FileNotFoundError:
    df = pd.read_excel('data/Nigerian E-Commerce Dataset.xlsx')
    print(f"✅ Data extracted from data directory")

print(f"📊 Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")

# ... (rest of the Python code)
