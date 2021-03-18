SET PATH_SCRIPT=python.exe woa18_convert.py

start "" cmd /k %PATH_SCRIPT% -r E:/Data/GIS/CSV_grids_1_degree/6-Apparent_Oxygen_Utilization/all_available_years/Annual/Mean/woa18_all_A00mn01.csv
start "" cmd /k %PATH_SCRIPT% -rm E:/Data/GIS/CSV_grids_1_degree/6-Apparent_Oxygen_Utilization/all_available_years/Annual/SD/

start "" cmd /k %PATH_SCRIPT% -d E:/Data/GIS/CSV_grids_1_degree/7-Percent_Oxygen_Saturation/all_available_years/Annual/Mean/woa18_all_O00mn01.csv
start "" cmd /k %PATH_SCRIPT% -mm E:/Data/GIS/CSV_grids_1_degree/7-Percent_Oxygen_Saturation/all_available_years/Annual/SD/