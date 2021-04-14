from .lib_grids import *


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


def get_asc_data(config_grid):

    import pandas as pd
    import numpy as np

    df = {}
    config_grid = make_dat_lat_lon_grids(config_grid)
    
    try:

        path_dat = config_grid['path_dat']

        df['LAT'] = []
        df['LON'] = []

        for c_lat in config_grid['bins_lat']:
            for c_lon in config_grid['bins_lon']:
                df['LAT'].append(c_lat)
                c_lon = c_lon + 180.0
                if c_lon > 179.5:
                    c_lon = c_lon-360.0
                df['LON'].append(c_lon)
                
        all_data = []

        with open(path_dat,'r') as file_dat:
            lines_all = file_dat.readlines()
            for line_curr in lines_all:
                #line_curr = line_curr.strip()
                line_curr = line_curr.split('\n')[0]
                d = [line_curr[i:i+8] for i in range(0, len(line_curr), 8)]
                all_data.extend(d)  

        size_layer = len(df['LAT'])
        curr_depth_layer = -1
        size_c = size_layer

        for c_data in all_data:
            if size_c >= size_layer:
                size_c = 0
                curr_depth_layer = curr_depth_layer + 1
                df[str(curr_depth_layer)] = []
            
            df[str(curr_depth_layer)].append(float(c_data))

            size_c = size_c + 1

        df_dat = pd.DataFrame.from_dict(df)
        df_dat = df_dat.replace(-99.9999,-9999.0)
        df_dat = df_dat.replace('-99.9999',-9999.0)

    except Exception as e:
        print("Error: {}: {}".format(type(e).__name__, e))

    return(df_dat)
