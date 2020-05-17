# Introduction to Shell

In the directory there are 4 files: `summer.csv`, `spring.csv`, `autumn.csv`, `winter.csv`

## Wildcards (`*`, `[]`, `{}`, `?`)

`cut -d , -f 1 seasonal/s*.csv`

* select the first column with delimiter "," (comma-separated) of all the files spring.csv and summer.csv, files beginning with letter "s" (but not autumn.csv and winter.csv)

<div>
<img src="https://user-images.githubusercontent.com/51282928/82152501-d46cd600-988b-11ea-8a31-ba3884d53957.png" width="700"/>
</div>

## Implementations of pipeline

`cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | head -n 10`

* select the first column from the summer data
* remove the header line containing the word "Tooth"
* select the first 10 lines of actual data.

`cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | sort -r`

* select the first column from the summer data
* remove the header line containing the word "Tooth"
* sort in reverse order

`cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | sort | uniq -c`

* get the second column from seasonal/winter.csv,
* remove the word "Tooth" from the output so that only tooth names are displayed,
* sort the output so that all occurrences of a particular tooth name are adjacent; and
* display each tooth name once along with a count of how often it occurs.

<div>
<img src="https://user-images.githubusercontent.com/51282928/82152536-17c74480-988c-11ea-8c2a-cad98c85ddd5.png" width="500"/>
</div>

`grep "2017-07" seasonal/spring.csv | wc -l`

* search "2017-07" in spring.csv
* count how many "2017-07" in lines (word count)

### Wrapping Up

1. Use wc with appropriate parameters to list the number of lines in all of the seasonal data files. (Use a wildcard for the filenames instead of typing them all in by hand.)

Script: `wc -l seasonal/*.csv`

2. Add another command to the previous one using a pipe to remove the line containing the word "total".

Script: `wc -l seasonal/*.csv | grep -v total`

3. Add two more stages to the pipeline that use sort -n and head -n 1 to find the file containing the fewest lines.

Script: `wc -l seasonal/*.csv | grep -v total | sort -n | head -n 1`
