# Key Points from Course Supervised Learning with Scikit-learn

## Models
1. K-Nearest Neighbor
2. Linear regression
3. Logistic regression

* `01_mnist` practice order: `load_and_view.py` --> `split_and_accuracy.py` --> `overfit_or_underfit.py` 
* correlation matrix: `sns.heatmap(df.corr(), square=True, cmap='RdYlGn')`
* numerical EDA, do these: `df.info()`, summary statistics `df.describe()`, and `df.shape` contains of `(column, row)` columns (features) and rows (data points)
* R squared is a measure of model performance
* Cross-validation
* Lasso regularization: to find which features can be the best predictor --> `02_lasso_regularization.py`
* In lasso and ridge, `alpha` is an important parameter. Incorrect choice will lead to hyperparameter tuning. To see this: `02_ridge_regression_regularization.py`

![image](https://user-images.githubusercontent.com/51282928/82327990-749c3980-9a09-11ea-9eca-e38dbc20fd69.png)

* ROC curve: model's threshold, y-axis is the Recall
* Precision-recall curve: plotting the precision and recall for different thresholds. Precision and recall are defined as:

`Precision = TP / (TP + FP)`<br>
`Recall = TP / (TP + FN)`

![image](https://user-images.githubusercontent.com/51282928/82346306-7b827680-9a20-11ea-9563-7acf4a7293cb.png)

1. If the recall is high, the precision drops
2. In the case when there are no true positives or true negatives, precision is 0/0, which is undefined.
3. When the threshold is very close to 1, precision is also 1, because the classifier is absolutely certain about its predictions.

## Hyperparameter Tuning

* Grid search

![image](https://user-images.githubusercontent.com/51282928/82349487-57289900-9a24-11ea-83ee-e28006557522.png)

* Randomized search

![image](https://user-images.githubusercontent.com/51282928/82350164-314fc400-9a25-11ea-887a-32c841e4bc15.png)

* Hold-out set

(to decide whether Lasso regression, L1 norm, or Ridge regression, L2 is the best to use)

![image](https://user-images.githubusercontent.com/51282928/82352271-f13e1080-9a27-11ea-88db-60fd31d75ac1.png)

(to decide the L1-to-L2 ratio the best to use for Elastic Net regression)

![image](https://user-images.githubusercontent.com/51282928/82353701-fbf9a500-9a29-11ea-9713-062663de9e04.png)
