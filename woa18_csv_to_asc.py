#imports
import pandas as pd
import qgrid
import argparse
import lib_woa18_convert as l_woa
import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
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
            path_csv     = args.i
        else:
            print('No Arguments Provided... using defaults')
            path_csv     = 'E:/Data/GIS/CSV_grids_1_degree/1-Temperature/decav_climate_normal_1981_2010/Monthly/t01_January/other_stats/woa18_decav_t01an01.csv'

        config_grid = {
            'start_lat':-89.5,
            'end_lat':89.5,
            'start_lon':-179.5,
            'end_lon':179.5,
            'nodata_value':-9999,
            'cellsize':1
        }

        str_status,df_dat = l_woa.get_csv_data(path_csv, config_grid)
        print(str_status)
        str_status = l_woa.to_asc_all_depths(path_csv, config_grid, df_dat)
        print(str_status)

        input()
    except ValueError as e:
        print('Error: ' + e)