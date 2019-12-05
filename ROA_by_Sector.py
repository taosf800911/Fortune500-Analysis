import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

profits = f500[f500["profits"].notnull()]
assets = f500[f500["assets"].notnull()]
               
roa = profits["profits"] / assets["assets"]
f500["roa"] = roa

top_roa_by_sector = {}
sector = f500["sector"].unique()

for s in sector:
    selected_rows = f500[f500["sector"] == s]
    sorted_rows = selected_rows.sort_values("roa", ascending=False)
    
    top_roa_by_sector[s] = sorted_rows.iloc[0]["company"]