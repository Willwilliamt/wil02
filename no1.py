import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
order_items = pd.read_csv('order_items_dataset.csv')
orders = pd.read_csv('orders_dataset.csv')
products = pd.read_csv('products_dataset.csv')
customers = pd.read_csv('customers_dataset.csv')

orders_items_merged = pd.merge(orders, order_items, on='order_id')
full_data = pd.merge(orders_items_merged, customers, on='customer_id')
full_data_with_products = pd.merge(full_data, products, on='product_id')
top_products = full_data_with_products.groupby('product_id')['price'].sum().reset_index()
top_products = pd.merge(top_products, products[['product_id', 'product_category_name']], on='product_id')
top_products = top_products.sort_values(by='price', ascending=False).head(10)
print(top_products)
st.title('Dashboard Analisis E-Commerce')
st.header('10 Produk dengan Harga Tertinggi')
st.dataframe(top_products)
plt.figure(figsize=(10,6))
sns.barplot(x='product_category_name', y='price', data=top_products)
plt.xticks(rotation=90)
plt.title('10 Produk dengan Harga Tertinggi')
st.pyplot(plt)
