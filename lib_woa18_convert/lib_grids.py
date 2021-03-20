def make_lat_lon_grids(config_grid):

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