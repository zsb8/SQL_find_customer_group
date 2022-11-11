import pandas as pd
import numpy as np
data = [
    {"account_id": 'A0000001', "customer_id": 'a'},
    {"account_id": 'A0000001', "customer_id": 'b'},
    {"account_id": 'A0000002', "customer_id": 'b'},
    {"account_id": 'A0000002', "customer_id": 'c'},
    {"account_id": 'A0000003', "customer_id": 'c'},
    {"account_id": 'A0000004', "customer_id": 'd'},
      ]
index = [0, 1, 2, 3, 4, 5]
columns = ["account_id", "customer_id"]
df = pd.DataFrame(data, index, columns)


def create_list(n):
    # Create a list which length is n，such as [['A0000546', 'T8670'], ['A0047140', 'T4934'], ['A0027241', 'T2207']]
    result_list = [['A'+str(np.random.randint(1, 1000000-1)).zfill(7),
                     'C'+str(np.random.randint(1, 1000000-1)).zfill(7)]
                    for i in range(n)]
    print(f"This list is ：{result_list[1:20]}")
    return result_list


ap_list = create_list(30)
df_temp = pd.DataFrame(ap_list, columns=['account_id', 'customer_id'])
df = df.append(df_temp, ignore_index=True)
print(f"Data set is:\n{df.head()}")
df.to_csv('d:/clients.csv')
