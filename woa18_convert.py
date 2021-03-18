#imports
import argparse
import lib_woa18_convert as l_woa
import sys
import os

dict_help = {
    'r':'convert single CSV file to depth layered set of raw data ASC files',
    'rm':'convert multiple CSV files to depth layered sets of raw data ASC files',
    'd':'convert single CSV file to depth layered set of depth data ASC files',
    'mm':'convert multiple depth layered sets of ASC files to single depth layered set of min and max ASC files'
}

config_grid = {
    'start_lat':-89.5,
    'end_lat':89.5,
    'start_lon':-179.5,
    'end_lon':179.5,
    'nodata_value':-9999,
    'cellsize':1
}

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:



            my_parser = argparse.ArgumentParser(description='Converts CSV files to ASCII files. Options to convert single file, multiple files, generate depth files or minmax files')

            my_parser.add_argument('-r',
                                metavar='-raw',
                                type=str,
                                help=dict_help['r']
                                )
            my_parser.add_argument('-rm',
                                metavar='-rawm',
                                type=str,
                                help=dict_help['rm']
                                )
            my_parser.add_argument('-d',
                                metavar='-depth',
                                type=str,
                                help=dict_help['d']
                                )

            my_parser.add_argument('-mm',
                                metavar='-minmax',
                                type=str,
                                help=dict_help['mm']
                                )

            args = my_parser.parse_args()

            if args.r:
                print(dict_help['r'])
                config_grid['path_csv'] = args.r
                str_status,df_dat = l_woa.get_csv_data(config_grid)
                print(str_status)
                str_status = l_woa.csv_to_asc_raw_all(config_grid, df_dat)
                print(str_status)

            if args.d:
                print(dict_help['d'])
                config_grid['path_csv'] = args.d
                str_status,df_dat = l_woa.get_csv_data(config_grid)
                print(str_status)
                str_status,df_dat = l_woa.csv_to_asc_depth_all(config_grid, df_dat)
                print(str_status)

            if args.rm:
                print(dict_help['rm'])
                dir_csv    = args.rm
                l_path_csv = os.listdir(dir_csv)
                l_path_csv = [s for s in l_path_csv if '.csv' in s]
                print('Found ' + str(len(l_path_csv)) + ' files')
                for c_path_csv in l_path_csv:
                    print('Processing ' + c_path_csv)
                    config_grid['path_csv'] = dir_csv + '/' + c_path_csv
                    str_status,df_dat = l_woa.get_csv_data(config_grid)
                    print(str_status)
                    str_status = l_woa.csv_to_asc_raw_all(config_grid, df_dat)
                    print(str_status)

            if args.mm:
                dir_asc    = args.mm
        else:
            print('No Arguments Provided.... Please enter correct arguments and try again or see -h for help')

    except ValueError as e:
        print('Error: ' + e)