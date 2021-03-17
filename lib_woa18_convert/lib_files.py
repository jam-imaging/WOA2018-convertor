def get_csv_data(path_csv, config_grid):
    
    import pandas as pd

    sep=","
    comment="#"
    skiprows=1
    df = {}
    
    try:
        df = pd.read_csv(path_csv,sep=sep,skiprows=skiprows,engine='python')
        str_status = 'CSV : Data extracted'
        df = df.rename(columns={"#COMMA SEPARATED LATITUDE": "LAT", " LONGITUDE":"LON"," AND VALUES AT DEPTHS (M):0": "0"}, errors="ignore")
        df = df.fillna(config_grid['nodata_value'])
    except Exception as e:
        str_status = ("Error: {}: {}".format(type(e).__name__, e))

    return(str_status,df)

def to_asc_all_depths(path_csv, config_grid, df_dat):

    import os
    import numpy as np


    try:
        curr_dataset = os.path.basename(path_csv).split('.')[0]
        dir_out  = os.path.dirname(path_csv) + '/' + curr_dataset

        if not os.path.isdir(dir_out):
            os.makedirs(dir_out)

        bins_lat = np.arange(config_grid['start_lat'],config_grid['end_lat'] + config_grid['cellsize'],config_grid['cellsize'])
        bins_lon = np.arange(config_grid['start_lon'],config_grid['end_lon'] + config_grid['cellsize'],config_grid['cellsize'])
        bins_lat = np.flip(bins_lat, axis=None)

        l_depth_layers = list(df_dat.columns)
        l_depth_layers = l_depth_layers[2:]

        for curr_depth_layer in l_depth_layers:

            path_asc = dir_out + '/' + curr_dataset + '_depth_[' +  curr_depth_layer + '].asc'

            ncols     = len(bins_lon)
            nrows     = len(bins_lat)
            xllcorner = min(bins_lon) - (config_grid['cellsize']/2)
            yllcorner = min(bins_lat) - (config_grid['cellsize']/2)

            with open(path_asc,'w') as file_asc:

                file_asc.write('ncols ' +  str(ncols) + '\n')
                file_asc.write('nrows ' +  str(nrows) + '\n')

                file_asc.write('xllcorner '    +  str(xllcorner)                   + '\n')
                file_asc.write('yllcorner '    +  str(yllcorner)                   + '\n')
                file_asc.write('cellsize '     +  str(config_grid['cellsize'])     + '\n')
                file_asc.write('nodata_value ' +  str(config_grid['nodata_value']) + '\n')

                for c_lat in bins_lat:
                    for c_lon in bins_lon:
                        res = df_dat[curr_depth_layer].loc[(df_dat['LAT'] == c_lat) & (df_dat['LON'] == c_lon)]
                        if len(res):
                            r = (res.item())
                            r = round(r,3)
                        else:
                            r = -9999
                        file_asc.write(str(r) + ' ')
                    file_asc.write('\n')

            print('Depth layer: ' + curr_depth_layer + ', Saved > ' +  path_asc)
            file_asc.close()   
        str_status = 'Files written'
    except ValueError as e:
        str_status = ("Error: {}: {}".format(type(e).__name__, e))
        
    return(str_status)