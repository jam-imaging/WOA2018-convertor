from .lib_imports import *
from .lib_grids import *
import numpy as np    
import os


def write_asc_header(path_asc, config_grid):
    with open(path_asc,'w') as file_asc:
        file_asc.write('ncols '        +  str(config_grid['ncols'])        + '\n')
        file_asc.write('nrows '        +  str(config_grid['nrows'])        + '\n')
        file_asc.write('xllcorner '    +  str(config_grid['xllcorner'])    + '\n')
        file_asc.write('yllcorner '    +  str(config_grid['yllcorner'])    + '\n')
        file_asc.write('cellsize '     +  str(config_grid['cellsize'])     + '\n')
        file_asc.write('nodata_value ' +  str(config_grid['nodata_value']) + '\n')
    return None

def csv_to_asc_raw_all(config_grid):

    try:
        df_dat       = get_csv_data(config_grid)
        curr_dataset = os.path.basename(config_grid['path_csv']).split('.')[0]
        dir_out      = config_grid['dir_out'] + '/' + curr_dataset

        if not os.path.isdir(dir_out):
            os.makedirs(dir_out)

        config_grid = make_asc_lat_lon_grids(config_grid)

        l_depth_layers = list(df_dat.columns)
        l_depth_layers = l_depth_layers[2:]

        for curr_depth_layer in l_depth_layers:

            path_asc = dir_out + '/' + curr_dataset + '_depth_[' +  curr_depth_layer + '].asc'
            write_asc_header(path_asc, config_grid)

            with open(path_asc,'a+') as file_asc:
                for c_lat in config_grid['bins_lat']:
                    for c_lon in config_grid['bins_lon']:
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


def asc_to_asc_raw_all(config_grid):

    try:

        df_dat       = get_asc_data(config_grid)
        curr_dataset = os.path.basename(config_grid['path_dat']).split('.')[0]
        dir_out      = config_grid['dir_out'] + '/' + curr_dataset

        if not os.path.isdir(dir_out):
            os.makedirs(dir_out)

        config_grid = make_asc_lat_lon_grids(config_grid)
    
        l_depth_layers = list(df_dat.columns)
        l_depth_layers = l_depth_layers[2:]

        for curr_depth_layer in l_depth_layers:

            path_asc = dir_out + '/' + curr_dataset + '_depth_[' +  curr_depth_layer + '].asc'
            write_asc_header(path_asc, config_grid)

            with open(path_asc,'a+') as file_asc:
                for c_lat in config_grid['bins_lat']:
                    for c_lon in config_grid['bins_lon']:
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


def asc_to_asc_depth_all(config_grid):

    import pandas as pd
    import os

    try:
        
        dir_asc      = config_grid['dir_asc']
        dir_out      = config_grid['dir_out'] + '/depth'

        if not os.path.isdir(dir_out):
            os.makedirs(dir_out)

        config_grid = make_asc_lat_lon_grids(config_grid)
        l_path_asc  = get_dir_list(dir_asc,[])
        l_depth_layers = get_depth_layers(os.path.dirname(l_path_asc[0]))

        for curr_depth_layer in l_depth_layers:

            c = [s for s in l_path_asc if '[' + curr_depth_layer + ']' in s]
            print('Number of files found: ' + str(len(c)))
            df = pd.DataFrame()

            all_data = []
            with open(c[0],'r') as file_dat:
                lines_all = file_dat.readlines()
                lines_all = lines_all[6:]
                for line_curr in lines_all:
                    all_data  = all_data + (line_curr.split())
            df['data'] = all_data
            df = df.astype(float)
            df[df !=-9999.0] = int(curr_depth_layer)

            path_asc = dir_out + '/depth_' + '_depth_[' +  curr_depth_layer + '].asc'
            write_asc_header(path_asc, config_grid)

            with open(path_asc,'a+') as file_asc:
                c_i = 0
                for c_lat in config_grid['bins_lat']:
                    for c_lon in config_grid['bins_lon']:
                        file_asc.write(str(df['data'].iloc[c_i]) + ' ')
                        c_i = c_i + 1
                    file_asc.write('\n')

            print('Depth layer: ' + curr_depth_layer + ', Saved > ' +  path_asc)
            file_asc.close()  

    except ValueError as e:
        print("Error: {}: {}".format(type(e).__name__, e))
        
    return None


def csv_to_asc_depth_all(config_grid):

    try:
        df_dat       = get_csv_data(config_grid)
        curr_dataset = os.path.basename(config_grid['path_csv']).split('.')[0]
        dir_out      = config_grid['dir_out'] + '/depth_' + curr_dataset

        if not os.path.isdir(dir_out):
            os.makedirs(dir_out)

        config_grid = make_asc_lat_lon_grids(config_grid)

        l_depth_layers = list(df_dat.columns)
        l_depth_layers = l_depth_layers[2:]

        for curr_depth_layer in l_depth_layers:

            path_asc = dir_out + '/depth_' + curr_dataset + '_depth_[' +  curr_depth_layer + '].asc'
            write_asc_header(path_asc, config_grid)

            with open(path_asc,'a+') as file_asc:
                for c_lat in config_grid['bins_lat']:
                    for c_lon in config_grid['bins_lon']:
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

def asc_to_asc_minmax_all(config_grid):

    import pandas as pd
    import os

    try:
        
        dir_asc      = config_grid['dir_asc']
        dir_out      = config_grid['dir_out']
        dir_out_min  = dir_out + '/min'
        dir_out_max  = dir_out + '/max'

        if not os.path.isdir(dir_out):
            os.makedirs(dir_out)
        if not os.path.isdir(dir_out_min):
            os.makedirs(dir_out_min)
        if not os.path.isdir(dir_out_max):
            os.makedirs(dir_out_max)

        config_grid = make_asc_lat_lon_grids(config_grid)
        l_path_asc  = get_dir_list(dir_asc,[])
        l_depth_layers = get_depth_layers(os.path.dirname(l_path_asc[0]))

        for curr_depth_layer in l_depth_layers:

            c = [s for s in l_path_asc if '[' + curr_depth_layer + ']' in s]
            print('Number of files found: ' + str(len(c)))
            df = pd.DataFrame()

            for i in range(len(c)):
                all_data = []
                with open(c[i],'r') as file_dat:
                    lines_all = file_dat.readlines()
                    lines_all = lines_all[6:]
                    for line_curr in lines_all:
                        all_data  = all_data + (line_curr.split())
                    df[str(i)] = all_data

            df = df.astype(float)
            df = df.replace(-9999.0,np.nan)

            l_min = df.min(axis=1)
            l_max = df.max(axis=1)
            df['min'] = l_min
            df['max'] = l_max
            df = df.replace(np.nan,-9999)

            path_asc = dir_out_min + '/min_' + '_depth_[' +  curr_depth_layer + '].asc'

            write_asc_header(path_asc, config_grid)

            with open(path_asc,'a+') as file_asc:
                c_i = 0
                for c_lat in config_grid['bins_lat']:
                    for c_lon in config_grid['bins_lon']:
                        file_asc.write(str(df['min'].iloc[c_i]) + ' ')
                        c_i = c_i + 1
                    file_asc.write('\n')

            print('Depth layer: ' + curr_depth_layer + ', Saved > ' +  path_asc)
            file_asc.close()   

            path_asc = dir_out_max + '/max_' + '_depth_[' +  curr_depth_layer + '].asc'

            write_asc_header(path_asc, config_grid)

            with open(path_asc,'a+') as file_asc:
                c_i = 0
                for c_lat in config_grid['bins_lat']:
                    for c_lon in config_grid['bins_lon']:
                        file_asc.write(str(df['max'].iloc[c_i]) + ' ')
                        c_i = c_i + 1
                    file_asc.write('\n')

            print('Depth layer: ' + curr_depth_layer + ', Saved > ' +  path_asc)
            file_asc.close()   
        
    except ValueError as e:
        print("Error: {}: {}".format(type(e).__name__, e))


    return None
