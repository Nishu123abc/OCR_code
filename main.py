
# MOBILE

# new_phones = []
#
# for i in l1:
#     val = i.replace(" ","").replace("-","")
#     if len(val)>10:
#         if val.startswith("91"):
#             y = val.split("91",1)[1]
#             new_phones.append(y)
#     else:
#         new_phones.append(val)
# print(new_phones)

# No country codes, No garbage values, Only 10 digits

import pandas as pd
l1 = ["12345 67890","91234-12345","91- 912341-2345"]
df = pd.DataFrame(l1,columns=['Mobile_No'])
new_df = df['Mobile_No'].apply(lambda x: x.replace(" ","").replace("-",""))

new_df = new_df.apply(lambda x: x.split("91",1)[1] if len(x) > 10 and x.startswith("91") else x)
print(new_df)


# select orederstatus from (select Order status, danse_rank() over(partition by OrderId orderby(OrderDate) desc) rnk from table where rnk = 1);