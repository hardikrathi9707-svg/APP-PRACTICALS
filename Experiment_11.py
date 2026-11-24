import pandas as pd
import numpy as np

# Create a Series with 10 random numbers
ser = pd.Series(np.random.randint(1, 100, 10))

print("Series:")
print(ser)

# Indexing
print("First Element:", ser[0])
print("First Three Elements:")
print(ser[:3])

# Filtering
print("Numbers greater than 50:")
print(ser[ser > 50])

# Statistical Operations
print("Mean:", ser.mean())
print("Median:", ser.median())
print("Minimum:", ser.min())
print("Maximum:", ser.max())