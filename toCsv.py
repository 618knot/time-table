def toCsv():
    import glob
    import pathlib as Path
    import tabula

    remove("csv/*")

    file = glob.glob("download/*")
    gb = ['goC', 'backS']
    dfs = tabula.read_pdf(f"{file[0]}", lattice=True, pages='all')
    
    for i in range(2):
        dfs[i] = dfs[i].dropna(axis = 1)
        dfs[i].to_csv(f"csv/{gb[i]}.csv", index=None)

def remove(pathname, recursive = True):
    import glob
    import os
    for i in glob.glob(pathname, recursive=recursive):
        if os.path.isfile(i):
            os.remove(i)
