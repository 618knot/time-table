def toCsv():

    import pathlib
    import pandas as pd
    import tabula
    import datetime
    pdfName = pathlib.Path('download').glob('*.pdf')
    print(pdfName)

    gb = ['Go', 'Back']

    dtn = datetime.datetime.now()
    dtn = dtn.strftime('%Y-%m-%d')

    dfs = tabula.read_pdf(f"download\{pdfName}", lattice=True, pages='all')
    for i in range(2):

        dfs[i] = dfs[i].drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2'], axis = 1)
        dfs[i].to_csv(f"timeTable{gb[i]}_{dtn}.csv", index=None)

    # df = tabula.read_pdf("食堂メニュー（6.13-6.17）.pdf", lattice=True, pages='all')
    # for i in range(1):

    #     df[i].to_csv("menu2.csv", index=None)

toCsv()
