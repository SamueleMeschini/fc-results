import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [pd.read_excel("results_fc.xlsx", sheet_name=i) for i in range(9)]
print(data)
