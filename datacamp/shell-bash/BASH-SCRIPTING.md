# Problem Statements to each of the codes in course Introduction to Bash Scripting

> Note:
> * Do `which bash` in your shell terminal to find out in which bash directory you're in now. Then input it as the she-bang `#!/...` at the very first of Bash script  
> * Using the she-bang `#!/...` or not in a bash script is OPTIONAL
> * If using she-bang `#!/...`, use `./script.sh` to run the bash script you created `script.sh`
> * If NOT using she-bang, use `bash script.sh` to run the bash script you created `script.sh`

1. Searching a book with shell

There is a copy of Charles Dickens's infamous 'Tale of Two Cities' in your home directory called two_cities.txt.

Use command line arguments such as cat, grep and wc with the right flag to count the number of lines in the book that contain either the character 'Sydney Carton' or 'Charles Darnay'. Use exactly these spellings and capitalizations.

`cat two_cities.txt | egrep 'Sydney Carton|Charles Darnay' | wc -l`

2. Shell: `echo "right now it is date"`. Output: right now it is December 25 2020<br>
double tick --> shell in a shell, backtick --> date<br>
alternative: right now it is $(date)

`dog_name='Messi'` (not a double tick)
`dog_age=6`
`echo "My dog's name is $dog_name and he is $dog_age years old"` 

## Cronjobs

```
# Create a schedule for 30 minutes past 2am every day
30 2 * * * bash script1.sh

# Create a schedule for every 15, 30 and 45 minutes past the hour
15,30,45 * * * * bash script2.sh

# Create a schedule for 11.30pm on Sunday evening, every week
30 23 * * 7 bash script3.sh
```

## Tough Practices

### [01_soccer_find_winner.sh]()

On the terminal, run: `./script.sh`

![image](https://user-images.githubusercontent.com/51282928/82155925-6384e880-98a2-11ea-8854-2b08663f332d.png)

### [01_soccer_replace_text.sh]()

On the terminal, run: `./script.sh`

![image](https://user-images.githubusercontent.com/51282928/82156098-60d6c300-98a3-11ea-9d80-d8d752d4c6cf.png)

### [01_HR_filter_cityname.sh]()

On the terminal, run: `bash script.sh Seoul`, then `bash script.sh Tallinn`

![image](https://user-images.githubusercontent.com/51282928/82156739-3850c800-98a7-11ea-855b-d39787ca931a.png)

### [02_fahrenheit_to_celsius.sh]()

Convert Fahrenheit to celsius: `C = (F - 32) x (5/9)`

Structure of computation (`STDIN`, `STDOUT`, and `ARGV`)

![image](https://user-images.githubusercontent.com/51282928/82185751-ec883800-9913-11ea-8d3e-a6a15fa44f8c.png)

### [03_good_or_bad_model.sh]()

![image](https://user-images.githubusercontent.com/51282928/82236886-fedb9380-995e-11ea-9afd-dedf35367f37.png)

### [03_check_if_text_is_inside_file]()

![image](https://user-images.githubusercontent.com/51282928/82237623-27b05880-9960-11ea-9d24-3e174a56b16f.png)

### [03_glob_file.sh]()

![image](https://user-images.githubusercontent.com/51282928/82238915-3435b080-9962-11ea-820d-4b2a7c6265eb.png)

### [03_sorting_file_forloop.sh]()

![image](https://user-images.githubusercontent.com/51282928/82239891-b2df1d80-9963-11ea-9fa7-b7b745ce717b.png)

### [03_case_weekday_or_weekend.sh]()

![image](https://user-images.githubusercontent.com/51282928/82241511-7cef6880-9966-11ea-83a9-6114afa2a65c.png)

### [03_case_sorting_file.sh]()

![image](https://user-images.githubusercontent.com/51282928/82242255-bffe0b80-9967-11ea-89b0-377d2d71afde.png)

### [04_function_what_day_is_today.sh]()

![image](https://user-images.githubusercontent.com/51282928/82243720-46b3e800-996a-11ea-8067-dec9fb257d6d.png)

### [04_function_percentage_calculator.sh]()

![image](https://user-images.githubusercontent.com/51282928/82244838-0fded180-996c-11ea-9639-60dbb26cf762.png)

### [04_function_sport_analytics.sh]()

![image](https://user-images.githubusercontent.com/51282928/82246011-2a19af00-996e-11ea-8465-83ee0e1318cd.png)

### [04_function_summing_array.sh]()

![image](https://user-images.githubusercontent.com/51282928/82247153-1d965600-9970-11ea-9cd5-c9f9d219b31f.png)
