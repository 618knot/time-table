import pandas as pd
import tabula

dfs = tabula.read_pdf("R４年度シャトルバス時刻表春学期_0606-0610.pdf", lattice=True, pages='all')

for i in range(2):
    dfs[i].to_csv(f"test{i}.csv", index=None)