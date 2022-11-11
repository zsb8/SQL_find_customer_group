# SQL_find_customer_group
Find the customer group from 8 million data.



# Sample
![image](https://user-images.githubusercontent.com/75282285/201437209-e5c9b0c8-dd56-4b3d-bc69-b19ce47db319.png)

# Firt loop
![image](https://user-images.githubusercontent.com/75282285/201437242-dea269ef-cdbf-456e-b80e-4caa4a58199b.png)

![image](https://user-images.githubusercontent.com/75282285/201437694-2e683e5e-7768-4e3c-8ca9-866db6d0ab39.png)

# Second loop

![image](https://user-images.githubusercontent.com/75282285/201437714-8a840959-0fba-45be-a554-9ecef4d19004.png)

![image](https://user-images.githubusercontent.com/75282285/201437731-73def2d3-d65a-4135-9f19-5eef5bf04034.png)

# Third loop
![image](https://user-images.githubusercontent.com/75282285/201437782-803c570d-1109-48be-a7e7-82e8d42201a4.png)

# Main logic
Group by account_id
~~~~
        with temp as (select account_id, min(group_id) as rk from customer_table group by account_id)
        update customer_table set group_id=rk from temp where temp.account_id=customer_table.account_id;
~~~
Group by customer_id
~~~
        with temp as (select customer_id, min(group_id) as rk from customer_table group by customer_id)
        update customer_table set group_id=rk from temp where temp.customer_id=customer_table.customer_id;
~~~
