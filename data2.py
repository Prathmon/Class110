import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics as ss
import random

file1 = pd.read_csv('newdata.csv')
data = file1["average"].to_list()
fig = ff.create_distplot([data], ["average"], show_hist = False)
fig.show()

mean = ss.mean(data)
median = ss.median(data)
stDev = ss.stdev(data)

print("Mean = ", mean)
print("Median = ", median)
print("Standard Deviation", stDev)