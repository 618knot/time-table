import pandas as pd
import tabula
import datetime
gb = ['Go', 'Back']

dtn = datetime.datetime.now()
dtn = dtn.strftime('%Y-%m-%d')

dfs = tabula.read_pdf("R４年度シャトルバス時刻表春学期_0606-0610.pdf", lattice=True, pages='all')
for i in range(2):

    dfs[i] = dfs[i].drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2'], axis = 1)
    dfs[i].to_csv(f"timeTable{gb[i]}_{dtn}.csv", index=None)
