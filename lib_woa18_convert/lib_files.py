def get_csv_data(path_csv):
    
    import pandas as pd

    sep=","
    comment="#"
    skiprows=1
    df = {}
    
    try:
        df = pd.read_csv(path_csv,sep=sep,skiprows=skiprows,engine='python')
        str_status = 'CSV : Data extracted'
    except Exception as e:
        str_status = ("Error: {}: {}".format(type(e).__name__, e))

    return(str_status,df)