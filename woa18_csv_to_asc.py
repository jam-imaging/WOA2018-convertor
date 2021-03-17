#imports
import pandas as pd
import qgrid
import numpy as np
import os
import argparse
import lib_woa18_convert as l_woa

my_parser = argparse.ArgumentParser(description='Converts CSV files to ASCII files')
my_parser.add_argument('--i',
                       metavar='i',
                       type=str,
                       help='the path to list')
my_parser.add_argument('--o',
                       metavar='o',
                       type=str,
                       help='the path to list')

args = my_parser.parse_args()


#user_paths
#path_csv     = 'E:/Data/GIS/CSV_grids_1_degree/Temperature/decav_climate_normal_1981_2010/Annual_t00/standard_deviation_sd/woa18_decav_t00sd01.csv'
#dir_out_base = 'E:/Data/GIS/CSV_grids_1_degree/Temperature/decav_climate_normal_1981_2010/Annual_t00/standard_deviation_sd'
flag_validate = False

path_csv     = args.i

config_grid = {
    'start_lat':-89.5,
    'end_lat':89.5,
    'start_lon':-179.5,
    'end_lon':179.5,
    'nodata_value':-9999,
    'cellsize':1
}

curr_filename = os.path.basename(path_csv).split('.')[0]
dir_out_base  = os.path.dirname(path_csv)
print(dir_out_base)
dir_out  = dir_out_base + '/' + curr_filename

print('Input > ' + path_csv)
print('Output > ' + dir_out)


if not os.path.isdir(dir_out):
    os.makedirs(dir_out)

str_status,df_dat = l_woa.get_csv_data(path_csv)
df_dat = df_dat.rename(columns={"#COMMA SEPARATED LATITUDE": "LAT", " LONGITUDE":"LON"," AND VALUES AT DEPTHS (M):0": "0"}, errors="ignore")
df_dat = df_dat.fillna(config_grid['nodata_value'])

bins_lat = np.arange(config_grid['start_lat'],config_grid['end_lat'] + config_grid['cellsize'],config_grid['cellsize'])
bins_lon = np.arange(config_grid['start_lon'],config_grid['end_lon'] + config_grid['cellsize'],config_grid['cellsize'])
bins_lat = np.flip(bins_lat, axis=None)

l_depth_layers = list(df_dat.columns)
l_depth_layers = l_depth_layers[2:]

for curr_depth_layer in l_depth_layers:
#curr_depth_layer = '0'

    if flag_validate is True:
        l_woa.plot_layer_by_number(df_dat,curr_depth_layer)

    path_asc = dir_out + '/' + curr_filename + '_depth_[' +  curr_depth_layer + '].asc'

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