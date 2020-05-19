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

* ROC curve: model's threshold
