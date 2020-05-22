# Key Lessons of course Model Validation in Python

## Feature importances, probability, and model accuracy

* Parameters of Random Forest: `max_depth`, `random_state`, `n_estimators`
* Feature importances: `.feature_importances_`
* Evaluate the probability of a predicted result: `.predict_proba`
* Evaluate the accuracy: `.score` --> model accuracy, inputs: `X_test` and `y_test`

## Train-test-validation split, accuracy metric

* Split the dataset into `train`, `test`, and `validation`. `test` and `validation` are the **hold-out** sets to assess model performance. Step in sklearn: first split data into `test` and `temp`, then split again `temp` into `train` and `validation`
* Metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE)
* We could measure how one class is better predicted than the other class by comparing its MAE. See also [02_mean_absolute_error_one_class.py]()

In the following, 9% error in prediction for `chocolate` class, and 11% error in prediction for `non-chocolate`. So, `chocolate` class has better prediction.

![image](https://user-images.githubusercontent.com/51282928/82670108-bd046300-9c66-11ea-8da3-b63a14459759.png)

* 3 metrics: 1. Accuracy (`(TN + TP) / total_observation`), 2. Precision (`TP / (TP + FP)`), 3. Recall (`TP / (TP + FN)`); Where `TP` true positive, `TN` true negative, `FP` false positive, and `FN` false negative

See implementation for **confusion matrix** in sklearn [02_confusion_matrix.py] and for **metric score** [02_metric_score.py](), in this case is the **precision** metric. 

![image](https://user-images.githubusercontent.com/51282928/82678600-10c97900-9c74-11ea-9169-e63654072376.png)

```
# Calculate and print the accuracy
accuracy = (491 + 324) / (953)
print("The overall accuracy is {0: 0.2f}".format(accuracy))

# Calculate and print the precision
precision = (491) / (491 + 15)
print("The precision is {0: 0.2f}".format(precision))

# Calculate and print the recall
recall = (491) / (491 + 123)
print("The recall is {0: 0.2f}".format(recall))
```

## Hold-out split is problem when limitted data, Cross Validation is the Solution

* CV score is calculated by splitting the data into 5, 10, etc folds then averaging its scores 
* More reliable 
* **Leave-one-out CV (LOOCV)**, the folds are the number of observations --> validation is every point. `cv=n` where `n` is number of observations

## Randomized Search CV

* See [04_random_search_print_best_model]() to implement how to print the model accuracies for different parameters searched
