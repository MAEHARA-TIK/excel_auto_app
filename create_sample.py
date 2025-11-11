import os

import pandas as pd

os.makedirs("input", exist_ok=True)

data1 = {"支店": ["東京", "大阪", "東京"], "売上": [100, 200, 150]}
data2 = {"支店": ["大阪", "大阪", "大阪"], "売上": [300, 400, 250]}

pd.DataFrame(data1).to_excel("input/sales_tokyo.xlsx", index=False)
pd.DataFrame(data2).to_excel("input/sales_osaka.xlsx", index=False)

print("サンプルExcelファイルを作成しました。")
