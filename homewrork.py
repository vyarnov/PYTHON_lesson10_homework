import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data["whoAmI"] == "robot"] = 1
data.loc[data["whoAmI"] == "human"] = 0
data.head()

# print(data.head())