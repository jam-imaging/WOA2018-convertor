def make_lat_lon_grids(config_grid):

    import numpy as np

    bins_lat = np.arange(config_grid['start_lat'],config_grid['end_lat'] + config_grid['cellsize'],config_grid['cellsize'])
    bins_lon = np.arange(config_grid['start_lon'],config_grid['end_lon'] + config_grid['cellsize'],config_grid['cellsize'])
    bins_lat = np.flip(bins_lat, axis=None)

    config_grid['ncols']     = len(bins_lon)
    config_grid['nrows']     = len(bins_lat)
    config_grid['xllcorner'] = min(bins_lon) - (config_grid['cellsize']/2)
    config_grid['yllcorner'] = min(bins_lat) - (config_grid['cellsize']/2)
    config_grid['bins_lat'] = bins_lat
    config_grid['bins_lon'] = bins_lon

    return config_grid

def get_depth_layers(dir_csv):

    import re
    import os

    l_path_csv = os.listdir(dir_csv)

    l_path_csv = [s for s in l_path_csv if '.asc' in s]
    print('Found ' + str(len(l_path_csv)) + ' files')

    l_layers = []
    for c_path_csv in l_path_csv:
        #k = re.findall(r'[[][0-9]+[]]',c_path_csv)
        #i = re.findall('[0-9]+',k[0])
        #l_layers.append(str(i[0]))

        i = c_path_csv[c_path_csv.find('depth_[')+7:c_path_csv.find(']')]
        l_layers.append(str(i))

    print('Found: ' + str(len(l_layers)) + 'layers')

    return l_layers