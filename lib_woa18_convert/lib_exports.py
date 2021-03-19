from .lib_imports import *

def csv_to_asc_raw_all(config_grid):

    import os
    import numpy as np

    df_dat = get_csv_data(config_grid)

    try:
        curr_dataset = os.path.basename(config_grid['path_csv']).split('.')[0]
        dir_out  = os.path.dirname(config_grid['path_csv']) + '/' + curr_dataset

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
    except ValueError as e:
        print("Error: {}: {}".format(type(e).__name__, e))
        
    return None

def csv_to_asc_depth_all(config_grid):

    import os
    import numpy as np

    df_dat = get_csv_data(config_grid)

    try:
        curr_dataset = os.path.basename(config_grid['path_csv']).split('.')[0]
        dir_out  = os.path.dirname(config_grid['path_csv']) + '/depth_' + curr_dataset

        if not os.path.isdir(dir_out):
            os.makedirs(dir_out)

        bins_lat = np.arange(config_grid['start_lat'],config_grid['end_lat'] + config_grid['cellsize'],config_grid['cellsize'])
        bins_lon = np.arange(config_grid['start_lon'],config_grid['end_lon'] + config_grid['cellsize'],config_grid['cellsize'])
        bins_lat = np.flip(bins_lat, axis=None)

        l_depth_layers = list(df_dat.columns)
        l_depth_layers = l_depth_layers[2:]

        for curr_depth_layer in l_depth_layers:

            path_asc = dir_out + '/depth_' + curr_dataset + '_depth_[' +  curr_depth_layer + '].asc'

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
                        res = df_dat.loc[(df_dat['LAT'] == c_lat) & (df_dat['LON'] == c_lon)]
                        if len(res):
                            r = float(curr_depth_layer)
                        else:
                            r = -9999
                        file_asc.write(str(r) + ' ')
                    file_asc.write('\n')

            print('Depth layer: ' + curr_depth_layer + ', Saved > ' +  path_asc)
            file_asc.close()    
    except ValueError as e:
        print("Error: {}: {}".format(type(e).__name__, e))
        
    return None

def folder_csv_to_asc_raw_all(config_grid):



    return None

def asc_to_asc_minmax_all(config_grid):

    try:
        print('a')
    except ValueError as e:
        print("Error: {}: {}".format(type(e).__name__, e))


    return None
