# Create function
function what_day_is_it {

  # Parse the results of date
  date=$(date | cut -d " " -f1)

  # Echo the result
  echo $date
}

# Call the function
what_day_is_it
