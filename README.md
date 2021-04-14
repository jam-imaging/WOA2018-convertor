# WOA Grid Generator
---


## Summary

Python library to convert WOA18 environmental data .dat ASCII and .csv CSV files to depth layered .asc files 
which can be imported into MaxentR

Converting CSV Grid data to ASCII formats which can used for analysis
- Convert single CSV file to depth layered raw data ASC files
- Convert multiple CSV files to depth layered ASC files
- Convert single DAT file to depth layered ASC files
- Optional multiprocessing to run parallel computations
- Convert single CSV file to depth layered depth data ASC files
- Convert multiple depth layered depth data ASC files to single depth layered ASC file


### Data Source
World Ocean Atlas 2018 data is available online at the following link
https://www.ncei.noaa.gov/access/world-ocean-atlas-2018/

### Program Usage
```
usage: woa18_csv_to_asc.py [-h] [-r -raw] [-rm -rawm] [-d -depth]
                           [-mm -minmax]

Converts CSV files to ASCII files. Options to convert single file, multiple
files, generate depth files or minmax files

optional arguments:
  -h, --help     show this help message and exit
  -r -raw        extract csv raw data > input: single CSV file, output: single
                 folder with ASC files
  -rm -rawm      extract csv raw data (multiple files) > input: single folder
                 with multiple CSV files, output: multiple folders with ASC
                 files
  -a -rasc       extract asc to raw data > input: WOA15 asc file, output:
                 single folder with ASC files
  -d -depth      extract csv depth data > input: single CSV file, output:
                 single folder with ASC files
  -da -depthasc  extract asc depth data > input: single folder with ASC files,
                 output: single folder with ASC files
  -mm -minmax    extract asc min max data > input: multiple folders with ASC
                 files, output: single folder with ASC files
  -p -pro        enable multiprocessing > input: N number of processes
  -o -out        set output directory > input: output directory name
```

