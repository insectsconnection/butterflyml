import streamlit as st
import matplotlib as plt 
import matplotlib.pyplot as plt
import seaborn as sns
import sqlalchemy as sa
import urllib
import numpy as np

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                 "SERVER=localhost\SQLEXPRESS;"
                                 "DATABASE=master;"
                                 "Trusted_Connection=yes")

## Connect using the specified parameters
engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

## Query to pull data
timeSeries_query = """
SELECT 
	InvoiceDate, 
	Description,
	ROUND(SUM(Quantity * UnitPrice), 2) AS Total_Sale_Amt  
FROM 
	OnlineRetail
WHERE InvoiceDate BETWEEN '2010-12-01' AND '2011-01-01'
	AND Description IN ('CHOCOLATE HOT WATER BOTTLE', 'GREY HEART HOT WATER BOTTLE')
GROUP BY InvoiceDate, Description
ORDER BY InvoiceDate
"""
## Pull data using pandas
df_series = pd.read_sql(timeSeries_query, engine)
df_series['InvoiceDate'] = pd.to_datetime(df_series['InvoiceDate'])

plt.rc('figure', figsize=(10, 5))
fig, ax = plt.subplots()

sns.lineplot(data=df_series, x='InvoiceDate', y='Total_Sale_Amt', hue='Description', style='Description',
             linewidth=0.8, marker='o')
start, end = ax.get_xlim()
plt.xticks(ticks=np.arange(start, end, 2),  # 2 days apart
           rotation=45, ha='right')

plt.show()

st.title("Online Retail")
## !!! date options
date = st.sidebar.selectbox(
    "Select a Invoice Date Range",
    [
        "'2010-12-01' and '2011-01-01'",
        "'2010-12-01' and '2010-12-15'"
    ])
## !!! product options
product = st.sidebar.selectbox(
    "Select a Product",
    [
        'CHOCOLATE HOT WATER BOTTLE',
        'GREY HEART HOT WATER BOTTLE',
        'JUMBO BAG PINK POLKADOT',
        'WHITE METAL LANTERN'
    ])

## Take in the query
df_series = pd.read_sql(timeSeries_query, engine)
df_series['InvoiceDate'] = pd.to_datetime(df_series['InvoiceDate'])

## Line chart
plt.rc('figure', figsize=(10, 5))
fig, ax = plt.subplots()

sns.lineplot(data=df_series, x='InvoiceDate', y='Total_Sale_Amt', hue='Description', style='Description',
             linewidth=0.8, marker='o')
start, end = ax.get_xlim()
plt.xticks(ticks=np.arange(start, end, 2),  # 2 days apart
           rotation=45, ha='right')
