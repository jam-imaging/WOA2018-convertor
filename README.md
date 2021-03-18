# WOA Grid Generator
---
## Summary
- Converting ASCII Grid data to ASCII formats which can used for analysis
- Converting CSV Grid data to ASCII formats which can used for analysis

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
```

