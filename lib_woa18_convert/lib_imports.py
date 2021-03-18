def get_csv_data(config_grid):
    
    import pandas as pd

    sep=","
    comment="#"
    skiprows=1
    df = {}
    
    try:
        df = pd.read_csv(config_grid['path_csv'],sep=sep,skiprows=skiprows,engine='python')
        str_status = 'CSV : Data extracted'
        df = df.rename(columns={"#COMMA SEPARATED LATITUDE": "LAT", " LONGITUDE":"LON"," AND VALUES AT DEPTHS (M):0": "0"}, errors="ignore")
        df = df.fillna(config_grid['nodata_value'])
    except Exception as e:
        str_status = ("Error: {}: {}".format(type(e).__name__, e))

    return(str_status,df)