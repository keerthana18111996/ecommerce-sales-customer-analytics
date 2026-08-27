#project on E-commerce in sales and customer analytics
import pandas as pd
import random
from datetime import datetime,timedelta
categories=["electronics","clothing","home","beauty","sports"]
products=["laptop","headphone","T-shirt","shoes","mixer","face cream","cricket ball","smartphone"]
customer_names=["ananya","priya","rahul","arun","kavya","sneha","vijay","divya","karthik","meena"]
cities=["chennai","banglore","mumbai","hyderabad","delhi","coimbatore"]
states=["tamilnadu","karnataka","maharastra","telangana","delhi"]
payment_method=["UPI","credit card","debit card","cash on delivery","net banking"]
order_status=["delivered","cancelled","returned"]
start_date=datetime(2025,1,1)
num_orders=1000
data=[]
for i in range(num_orders):
    order_id="ORD"+str(1001+i)
    order_date= start_date+timedelta(days=random.randint(0,364))
    customer_id="CUST"+str(random.randint(101,110))
    customer_name=random.choice(customer_names)
    category=random.choice(categories)
    product=random.choice(products)
    quantity=random.randint(1,5)
    unit_price=random.randint(500,50000)
    city=random.choice(cities)
    state=random.choice(states)
    payment_method=random.choice(payment_method)
    order_status=random.choice(order_status)
    discount=random.choice([0,0.05,0.10,0.15])
    sales_amount=quantity*unit_price*(1-discount)
    data.append([order_id,order_date,customer_id,customer_name,category,product,quantity,unit_price,discount,sales_amount,city,state,payment_method,order_status])
df=pd.DataFrame(data,columns=["order_ID","order_date","customer_ID","customer name","category","product","quantity","unit_price","discount","sales_amount","city",
                                  "state","payment_method","order_status"])
df.to_csv("ecommerce_sales.csv",index=False)
print("dataset created successfully!")
#data inspection
print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print("duplicate rows:",df.duplicated().sum())
#data cleaning
print("missing values:")
print(df.isnull().sum())
print("duplicate rows:")
print(df.duplicated().sum())
#check data types
print("data types:")
print(df.dtypes)
#To identify invalid or unwanted state values
valid_states=["tamilnadu","karnataka","maharastra","telangana"]
print(df[~df["state"].isin(valid_states)])
#To identify invalid or unwanted values in category column
valid_categories=["electronics","clothing","home","beauty"]
print(df[~df["category"].isin (valid_categories)])
# data analysis
# overall sales analysis(total sales)
print("total sales:",df["sales_amount"].sum())
# total orders
total_orders=df["order_ID"].nunique()
print("total orders:",total_orders)
#average order value
average_order_value=df["sales_amount"].mean()
print("average order value:",average_order_value)
#total quantity sold
total_quantity=df["quantity"].sum()
print("total quantity sold:",total_quantity)
#sales by category
sales_by_category=df.groupby("category")["sales_amount"].sum()
print("sales by category:")
print(sales_by_category)
#category has highest sales
highest_category=sales_by_category.idxmax()
highest_sales=sales_by_category.max()
print("highest sales category:",highest_category)
print("sales:",highest_sales)
#category has lowest sales
lowest_category=sales_by_category.idxmin()
lowest_sales= sales_by_category.min()
print("lowest sales category:",lowest_category)
print("sales:",lowest_sales)
#sales by state
sales_by_state=df.groupby("state")["sales_amount"].sum()
print("sales by state:")
print(sales_by_state)
#highest sales in state
highest_state=sales_by_state.idxmax()
highest_sales=sales_by_state.max()
print("highest sales state:",highest_state)
print("sales:",highest_sales)
#lowest sales in state
lowest_state=sales_by_state.idxmin()
lowest_sales=sales_by_state.min()
print("lowest sales state:",lowest_state)
print("sales:",lowest_sales)
# monthly sales 
monthly_sales=df.groupby(df["order_date"].dt.month)["sales_amount"].sum()
print("monthly sales:")
print(monthly_sales)
#total sales in monthwise
df["date"]=pd.to_datetime(df["order_date"])
monthly_sales=df.groupby(df["order_date"].dt.month)["sales_amount"].sum()
print("total sales month_wise:")
print(monthly_sales)
#identify best and worst sales months
best_month=monthly_sales.idxmax()
best_sales=monthly_sales.max()
worst_month=monthly_sales.idxmin()
worst_sales=monthly_sales.min()
print("best sales month:",best_month)
print("best sales:",best_sales)
print("worst sales month:",worst_month)
print("worst sales:",worst_sales)
#product analysis
#sales by product
product_sales=df.groupby("product")["sales_amount"].sum(numeric_only=True)
print("sales by product:")
print(product_sales)
#top 10 products by sales
product_sales=df.groupby("product")["sales_amount"].sum()
top_10_products=product_sales.sort_values(ascending=False).head(10)
print("top10 products by sales:")
print(top_10_products)
#top 10 products by quantity sold
top_10_products=(df.groupby("product")["quantity"].sum().sort_values(ascending =False).head(10))
print(top_10_products)
#customer analysis
# number of unique customer
unique_customers=df["customer_ID"].nunique()
print("number of unique customers:",unique_customers)
#top customers by spending
customer_spending=df.groupby("customer_ID")["sales_amount"].sum()
top_customers=customer_spending.sort_values(ascending=False).head(10)
print("top10 customers by spending:")
print(top_customers)
#average customer spending
customer_spending=df.groupby("customer_ID")["sales_amount"].sum()
average_customer_spending=customer_spending.mean()
print("average customer spending:",average_customer_spending)
# payment analysis
#total sales by payment method
payment_sales=df.groupby("payment_method")["sales_amount"].sum()
print(payment_sales)
#most commonly used payment method
most_used_payment=df["payment_method"].value_counts().idxmax()
print("most used payment method:",most_used_payment)
#discount analysis
#average discount
average_discount=df["discount"].mean()
print("average discount:",average_discount)
#sales with and without discount analysis
sales_with_discount=df[df["discount"]>0]["sales_amount"].sum()
sales_without_discount=df[df["discount"]==0]["sales_amount"].sum()
print("sales with discount:",sales_with_discount)
print("sales without discount:",sales_without_discount)
#relationship between discount and sales
discount_sales_correlation=df["discount"].corr(df["sales_amount"])
print("correlation between discount and sales:",discount_sales_correlation)
#visualization
#monthly sales trend
import matplotlib.pyplot as plt
monthly_sales.plot(kind='line',marker='o')
plt.title("monthly sales trend")
plt.xlabel("month")
plt.ylabel("total sales")
plt.show()
#category sales by bar chart
category_sales=df.groupby('category')['sales_amount'].sum().sort_values(ascending=False)
category_sales.plot(kind='bar')
plt.title('sales by category')
plt.xlabel('category')
plt.ylabel('total sales')
plt.xticks(rotation=45)
plt.show()
#state sales by bar chart
state_sales=df.groupby('state')['sales_amount'].sum().sort_values(ascending=False)
state_sales.plot(kind='bar')
plt.title('sales by state')
plt.xlabel('state')
plt.ylabel('total sales')
plt.xticks(rotation=45)
plt.show()
#top products bar chart
top_products=df.groupby('product')['sales_amount'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar')
plt.title('top 10 products by sales')
plt.xlabel('product')
plt.ylabel('total sales')
plt.xticks(rotation=45)
plt.show()
#payment_method chart
payment_method=df['payment_method'].value_counts()
payment_method.plot(kind='bar')
plt.title('orders by payment method')
plt.xlabel('payment method')
plt.ylabel('number of orders')
plt.xticks(rotation=45)
plt.show()
#insights
#category has highest sales
category_sales=df.groupby("category")["sales_amount"].sum()
highest_category=category_sales.idxmax()
highest_sales=category_sales.max()
print("highest sales category:",highest_category)
print("highest sales:",highest_sales)
#insight
print("insight:",highest_category,"is the highest_selling category,indicating strong customer demand.")
#state has highest sales
state_sales=df.groupby("state")["sales_amount"].sum()
highest_sales=state_sales.idxmax()
highest_sales=state_sales.max()
print("state with highest sales:",highest_state)
print("highest sales:",highest_sales)
#insight
print("insight:",highest_state,"has the highest sales with total sales of",highest_state)
#product sell the most
product_quantity=df.groupby("product")["quantity"].sum()
top_product=product_quantity.idxmax()
top_quantity=product_quantity.max()
print("product that sells the most:",top_product)
print("quantity sold:",top_quantity)
#insight
print("insight:", top_product, "is the best-selling product with",top_quantity,"units sold.")
#payment method is most used
payment_count=df["payment_method"].value_counts()
most_used_payment=payment_count.idxmax()
highest_count=payment_count.max()
print("most used payment method:",most_used_payment)
print("number of orders;",highest_count)
#insight code
print("insight:",most_used_payment,"is the most used payment method.")
#the month has highest and lowest sales
highest_sales=df["sales_amount"].max()
lowest_sales=df["sales_amount"].min()
print("highest sales:",highest_sales)
print("lowest sales:",lowest_sales)
#insight code
print("insight: the highest sales value is",highest_sales)
print("insight: the lowest sales value is",lowest_sales)
#conclusion
print("conclusion")
print("The e-commerce sales analysis provided useful insights into overall sales performance and customer purchasing patterns.")
print("The analysis identified the highest-performing state, best-selling products, successful categories, and most-used payment method.")
print("It also helped identify the highest and lowest sales values and understand sales trends.")
print("These findings can help the business improve sales performance and make better business decisions.")
#recommendations
print("RECOMMENDATIONS")
print("1.focus more on the best-performing products and categories.")
print("2.increase marketing efforts in states with high sales potential.")
print("3.promote the most preferred payment methods for easier customer purchases.")
print("4.analyse low-performing products and categories to improve their sales.")
print("5.use customer purchasing patterns to create targeted offers and discounts.")





















             
             



      

        
