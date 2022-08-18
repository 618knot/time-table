def toJSON(csv_name):
    import pandas as pd

    df = pd.read_csv("csv/" + csv_name, header=0)

    key_list = ["bus stations"]
    contents_list = [list(df.columns)]

    for i in range(len(df)):
        key_list.append(f"bus{i}")
        contents_list.append(df.iloc[i].tolist())

    return dict(zip(key_list, contents_list))