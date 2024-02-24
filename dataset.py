import pandas as pd
import numpy as np

# Read the first two rows of the CSV file
lines = pd.read_csv(r"C:\Malayalam_Char_Gabor.csv", nrows=2)

lines = lines.apply(pd.to_numeric, errors='coerce')

# Calculate mean of each row
mean1 = np.mean(lines.iloc[0])
mean2 = np.mean(lines.iloc[1])

# Calculate standard deviation of both rows
std = np.std(lines)

print("Mean of the first row of the csv file is:", mean1)
print("Mean of the second row of the csv file is:", mean2)
print("Standard deviation of the rows of the csv file are:", std)
