import statistics

data = [1, 8, 27, 64, 125, 256, 343, 512, 729]
data2 = [1, 8, 27, 64, 125, 256, 343, 512, 729, 1000]

x = statistics.median(data)
y = statistics.median(data2)

print("The median of this dataset is:", x)
print("The median of this dataset is:", y)
