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
