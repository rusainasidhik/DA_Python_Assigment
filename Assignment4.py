import numpy as np

temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

print(temperatures_w1)

print("Shape:", temperatures_w1.shape)

print("Data type:", temperatures_w1.dtype)

print("Number of elements:", temperatures_w1.size)

fahrenheit = (temperatures_w1 * 9/5) + 32

print("Temperature in Fahrenheit:")
print(fahrenheit)

print("Maximum temperature:", temperatures_w1.max())
print("Minimum temperature:", temperatures_w1.min())
print("Mean temperature:", temperatures_w1.mean())

#First three days   
print("First three days:", temperatures_w1[:3])

#Last two days
print("Weekend:", temperatures_w1[-2:])

#Middle three days
print("Middle three days:", temperatures_w1[2:5])

#create a 2D array 
temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9], #week 1
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1] #week 2
])

print(temperatures)

print("Shape:", temperatures.shape)

print("Data type:", temperatures.dtype)

print("Total number of elements:", temperatures.size)

print("Week 1:", temperatures[0])

print("Week 2:", temperatures[1])

print("Week 1 weekend:", temperatures[0, -2:])

print("Week 2 weekend:", temperatures[1, -2:])

import pandas as pd

marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5']
)

print(marks)

print(marks.iloc[0])
print(marks.loc[['Rank1', 'Rank2', 'Rank3']])
print(marks.iloc[2])
print(marks[marks > 90])

marks['Rank1'] = 100
print(marks)
marks = marks.drop('Rank5')
print(marks)
cgpa = marks / 10
print(cgpa)

import pandas as pd

transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': [
        'Electronics', 'Clothing', 'Electronics', 'Furniture',
        'Clothing', 'Electronics', 'Furniture', 'Clothing',
        'Furniture', 'Electronics'
    ],
    'Region': [
        'North', 'South', 'North', 'East', 'West',
        'North', 'East', 'West', 'South', 'North'
    ],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})

print(transactions)

print(transactions)

print(transactions.head())

print(transactions.tail())

print(transactions.shape)

print(transactions.columns)

print(transactions.dtypes)

transactions.info()

print(transactions[['ProductCategory', 'Amount']])

print(transactions.iloc[:, -3:])

print(transactions[
    (transactions['Region'] == 'North') &
    (transactions['Amount'] > 200)
])

print(transactions['ProductCategory'].value_counts())

print(transactions['Region'].unique())

print(transactions.groupby('Region')['Amount'].mean())

transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165
print(transactions)

transactions['Discount'] = transactions['Amount'] * 0.10
print(transactions)

transactions = transactions[
    transactions['TransactionID'] != 109
]
print(transactions)

transactions = transactions.drop('Discount', axis=1)
print(transactions)