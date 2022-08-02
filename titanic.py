import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('titanic.csv')
#df.to_csv('titanicone.csv', index=False)
print(df.describe())

