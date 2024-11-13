# Import pandas as pd
# Open customer list csv file

import pandas as pd

customer_list = pd.read_csv('customer_list_updated.csv')

print(customer_list.head())
print(customer_list.info())


customer_list[['cust_id','date','time','name','email','phone','sms-opt-out']] = customer_list['cust_id|date|time|name|email|phone|sms-opt-out'].str.split('|')
