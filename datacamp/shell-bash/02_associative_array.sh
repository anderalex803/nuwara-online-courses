declare -A model_metrics=([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)

# Print out the entire array
echo ${model_metrics[@]}

# Print out just the keys
echo ${!model_metrics[@]}
