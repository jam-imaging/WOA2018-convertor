# WOA Grid Generator
---
## Summary
Converting CSV Grid data to ASCII formats which can used for analysis
- Convert single CSV file to depth layered raw data ASC files
- Convert multiple CSV files to depth layered ASC files
- Optional multiprocessing to run parallel computations
- Convert single CSV file to depth layered depth data ASC files
- Conver multiple depth layered depth data ASC files to single depth layered ASC file


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
  -h, --help   show this help message and exit
  -r -raw      convert single CSV file to depth layered set of raw data ASC
               files
  -rm -rawm    convert multiple CSV files to depth layered sets of raw data
               ASC files
  -d -depth    convert single CSV file to depth layered set of depth data ASC
               files
  -mm -minmax  convert multiple depth layered sets of ASC files to single
               depth layered set of min and max ASC files
  -p -pro      enable option for using multiprocessing with N number of
               processes
```

