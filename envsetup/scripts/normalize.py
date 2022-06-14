import os
import json
import pandas as pd
import numpy as np
from pandas import json_normalize


actual_dir = os.getcwd()
file_a = actual_dir + "/dataa.json"
file_b = actual_dir + "/databx1.json"
with open(file_a, encoding="utf8") as encoded_a:
    json_a = json.load(encoded_a)
    encoded_a.close()
    data_a = [v for (k,v) in json_a.items() ]

with open(file_b, encoding="utf8") as encoded_b:
    json_b = json.load(encoded_b)
    encoded_b.close()
    data_b = [v for (k,v) in json_b.items() ]

def diff_pd(df1, df2):
    """Identify differences between two pandas DataFrames"""
    assert (df1.columns == df2.columns).all(), \
        "DataFrame column names are different"
    if any(df1.dtypes != df2.dtypes):
        "Data Types are different, trying to convert"
        df2 = df2.astype(df1.dtypes)
    if df1.equals(df2):
        return None
    else:
        # need to account for np.nan != np.nan returning True
        diff_mask = (df1 != df2) & ~(df1.isnull() & df2.isnull())
        ne_stacked = diff_mask.stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ['id', 'col']
        difference_locations = np.where(diff_mask)
        changed_from = df1.values[difference_locations]
        changed_to = df2.values[difference_locations]
        pd_result = pd.DataFrame({'from': changed_from, 'to': changed_to},
                            index=changed.index)
        print("##### values #####")
        #print("pd_result:",pd_result)
        print("index_name:",pd_result.index)
        print("from:", pd_result['from'])
        print("##### ne_stacked #####")
        print(ne_stacked)
        print("##### changed #####")
        print(changed)
        print(changed.values)
        print(changed.index[0])
        print("##### values #####")
        return {'index': changed.index, 'from': changed_from, 'to': changed_to}


result_a = json_normalize(data_a, 'counties', ['state', 'shortname',['info', 'governor']])
print("##### result a #####")
print(result_a)

result_b = json_normalize(data_b, 'counties', ['state', 'shortname',['info', 'governor']])
print("##### result b #####")
print(result_b)

print("##### diff #####")
print(diff_pd(result_a, result_b))
