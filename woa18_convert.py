#imports
import argparse
import lib_woa18_convert as l_woa
import sys
import os
from multiprocessing import Pool

dict_help = {
    'r':'extract csv raw data > input: single CSV file, output: single folder with ASC files',
    'rm':'extract csv raw data (multiple files) > input: single folder with multiple CSV files, output: multiple folders with ASC files',
    'a': 'extract asc to raw data > input: WOA15 asc file, output: single folder with ASC files',
    'd':'extract csv depth data > input: single CSV file, output: single folder with ASC files',
    'da':'extract asc depth data > input: single folder with ASC files, output: single folder with ASC files',
    'mm':'extract asc min max data > input: multiple folders with ASC files, output: single folder with ASC files',
    'p':'enable multiprocessing > input: N number of processes',
    'o':'set output directory >  input: output directory name'
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
            my_parser.add_argument('-a',
                                metavar='-rasc',
                                type=str,
                                help=dict_help['a']
                                )                                
            my_parser.add_argument('-d',
                                metavar='-depth',
                                type=str,
                                help=dict_help['d']
                                )
            my_parser.add_argument('-da',
                                metavar='-depthasc',
                                type=str,
                                help=dict_help['da']
                                )
            my_parser.add_argument('-mm',
                                metavar='-minmax',
                                type=str,
                                help=dict_help['mm']
                                )
            my_parser.add_argument('-p',
                                metavar='-pro',
                                type=str,
                                help=dict_help['p']
                                )
            my_parser.add_argument('-o',
                                metavar='-out',
                                type=str,
                                help=dict_help['o']
                                )

            args = my_parser.parse_args()

            if args.o:
                print(dict_help['o'])
                config_grid['dir_out'] = args.o

            if args.r:
                print(dict_help['r'])
                config_grid['path_csv'] = args.r
                l_woa.csv_to_asc_raw_all(config_grid)

            if args.a:
                print(dict_help['a'])
                config_grid['path_dat'] = args.a
                config_grid['depth_layers'] = ['0']
                l_woa.asc_to_asc_raw_all(config_grid)

            if args.d:
                print(dict_help['d'])
                config_grid['path_csv'] = args.d
                l_woa.csv_to_asc_depth_all(config_grid)

            if args.da:
                print(dict_help['da'])
                config_grid['dir_asc'] = args.da
                l_woa.asc_to_asc_depth_all(config_grid)

            if args.rm:
                print(dict_help['rm'])
                l_path_csv = l_woa.get_list_of_csv(args.rm)

                if args.p:
                    print(dict_help['p'])
                    rm_pool = Pool(int(args.p))

                    l_process = []
                    for c_path_csv in l_path_csv:
                        c_config_grid = dict(config_grid)
                        c_config_grid['path_csv'] = c_path_csv
                        l_process.append(c_config_grid)
                    rm_pool.map(l_woa.csv_to_asc_raw_all,l_process,chunksize=1)

                else:
                    for c_path_csv in l_path_csv:
                        config_grid['path_csv'] = c_path_csv
                        l_woa.csv_to_asc_raw_all(config_grid)

            if args.mm:
                config_grid['dir_asc'] = args.mm
                str_status = l_woa.asc_to_asc_minmax_all(config_grid)


        else:
            print('No Arguments Provided.... Please enter correct arguments and try again or see -h for help')

    except ValueError as e:
        print('Error: ' + e)