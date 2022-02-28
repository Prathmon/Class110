import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics as ss
import csv
import random

df = pd.read_csv('data.csv')
data = df["temp"].to_list()
fig = ff.create_distplot([data], ["temp"], show_hist = False)
fig.show()

mean = ss.mean(data)
median = ss.median(data)
stanDev = ss.stdev(data)

print("Mean = ", mean)
print("Median = ", median)
print("Standard deviation = ", stanDev)

data_set = []

for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    data_set.append(value)

ranMean = ss.mean(data_set)
ranMedian = ss.median(data_set)
ranStDev = ss.stdev(data_set)

fig2 = ff.create_distplot([data_set], ["temp"], show_hist = False)
fig2.show()

print("Mean of random numbers = ", ranMean)
print("Median of random integers = ", ranMedian)
print("Standard deviation of random integers = ", ranStDev)