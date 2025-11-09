import pandas as pd

customers=pd.read_csv("../customers.csv")

products=pd.read_csv("../products.csv")
orders=pd.read_csv("../orders.csv")

print('Customers: \n',customers.head())
print('products: \n',products.head())
print('orders: \n',orders.head())


customers['name']=customers['name'].str.title()
customers['city']=customers['city'].str.title()
customers['join_date']=pd.to_datetime(customers['join_date'])


orders['order_date']=pd.to_datetime(orders['order_date'])

orders['avg_price_per_item']=orders['total_amount']/orders['quantity']

orders=orders.merge(products[['product_id','category']], on='product_id',how='left')


print('Customers: \n',customers.head())
print('products: \n',products.head())
print('orders: \n',orders.head())

from google.cloud import bigquery

client=bigquery.Client(project="prismatic-smoke-477503-d0")

customer_table="prismatic-smoke-477503-d0.ecommerce_data.customers"
product_table="prismatic-smoke-477503-d0.ecommerce_data.products"
order_table="prismatic-smoke-477503-d0.ecommerce_data.orders"


client.load_table_from_dataframe(customer_table,customer_table).result()
client.load_table_from_dataframe(product_table,product_table).result()
client.load_table_from_dataframe(order_table,order_table).result()

print("Data loaded successfully into BigQuery.")