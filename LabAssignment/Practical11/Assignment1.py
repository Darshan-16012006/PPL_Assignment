import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dataset
data = {
    'month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    'facecream': [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    'facewash': [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760],
    'toothpaste': [5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400],
    'bathingsoap': [9200,6100,9550,8870,9960,8100,7890,9320,9010,8900,9100,9800],
    'shampoo': [1200,2100,3550,1870,1560,1890,1780,2100,2300,2400,1800,2200],
    'moisturizer': [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760],
    'total_profit': [211000,183300,224000,258000,240000,223000,230000,245000,260000,280000,300000,320000]
}

df = pd.DataFrame(data)

# -------- a) Line Plot --------
plt.figure(figsize=(8,5))
plt.plot(df['month'], df['total_profit'], marker='o')
plt.title('Total Profit per Month')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.grid(True)
plt.show()

# -------- b) Multiline Plot --------
plt.figure(figsize=(10,6))
plt.plot(df['month'], df['facecream'], label='Face Cream')
plt.plot(df['month'], df['facewash'], label='Face Wash')
plt.plot(df['month'], df['toothpaste'], label='Toothpaste')
plt.plot(df['month'], df['bathingsoap'], label='Bathing Soap')
plt.plot(df['month'], df['shampoo'], label='Shampoo')
plt.plot(df['month'], df['moisturizer'], label='Moisturizer')

plt.title('Product Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

# -------- c) Bar Chart --------
x = np.arange(len(df['month']))
plt.figure(figsize=(10,5))
plt.bar(x - 0.2, df['facecream'], width=0.4, label='Face Cream')
plt.bar(x + 0.2, df['facewash'], width=0.4, label='Face Wash')

plt.xticks(x, df['month'])
plt.title('Face Cream vs Face Wash Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.show()

# -------- d) Pie Chart --------
total_sales = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum(),
    df['moisturizer'].sum()
]

labels = ['Face Cream','Face Wash','Toothpaste','Bathing Soap','Shampoo','Moisturizer']

plt.figure(figsize=(8,8))
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title('Yearly Sales Distribution')
plt.show()