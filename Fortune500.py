import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None

top_employer_by_country ={}
country = f500["country"].unique()

for c in country:
    selected_rows = f500[f500["country"] == c]
    
    sorted_rows = selected_rows.sort_values("employees", ascending=False)
    top_employer_by_country[c] = sorted_rows.iloc[0]["company"]
    