import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('DDos.csv')
size_of_attack_data = df["size_of_attack"]
percentage_data = df["percentage"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0)  
plt.pie(percentage_data, labels=size_of_attack_data, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Size of DDoS attacks in year 2018")
plt.show()
