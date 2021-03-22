def get_csv_data(config_grid):
    
    import pandas as pd

    sep=","
    comment="#"
    skiprows=1
    df = {}
    
    try:
        path_csv = config_grid['path_csv']
        df = pd.read_csv(path_csv,sep=sep,skiprows=skiprows,engine='python')
        print('CSV : Data extracted')
        df = df.rename(columns={"#COMMA SEPARATED LATITUDE": "LAT", " LONGITUDE":"LON"," AND VALUES AT DEPTHS (M):0": "0"}, errors="ignore")
        df = df.fillna(config_grid['nodata_value'])
    except Exception as e:
        print("Error: {}: {}".format(type(e).__name__, e))

    return(df)

def get_list_of_csv(dir_csv):

    import os

    l_path_csv = os.listdir(dir_csv)
    l_path_csv = [s for s in l_path_csv if '.csv' in s]
    print('Found ' + str(len(l_path_csv)) + ' files')

    l_fullpath = []
    for c_path_csv in l_path_csv:
        l_fullpath.append(dir_csv + '/' + c_path_csv)
    return l_fullpath

def get_dir_list(dir_name, dir_list):

    import os
    list_names = os.listdir(dir_name) 
    list_names = [ s for s in list_names if '.DS' not in s]

    for curr_name in list_names:
        path_full = dir_name + '/' + curr_name
        if os.path.isdir(path_full):
            dir_list = get_dir_list(path_full + '/', dir_list)
        else:
            dir_list.append(path_full)
    return dir_list
