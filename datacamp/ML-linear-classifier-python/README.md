# Key Lessons from couse Linear Classifiers in Python

## Comparison: Logistic Regression vs SVM
* Logistic regression works by minimizing loss function (using **logistic loss function**)
* SVM works mainly by maximizing margin. Its loss function using **hinge loss function**

![image](https://user-images.githubusercontent.com/51282928/82482414-089cfc80-9b01-11ea-93e2-17a48bce80c7.png)

* The theory behind the **decision boundary** of linear classifiers (logistic regression and SVC): `raw model output = coefficient * X_test + intercept`. If the result is negative, it predicts the data into one class (`0`), if positive it predicts to another class `1`. This `0` and `1` class are associated with the `y_test`
* **Least square loss function is least favorable** ([02_minimizing_loss_function_squared.py]()). So, we could use **logistic loss function** for **logistic regression**, and **hinge loss function** for SVM (more on this: [02_log_and_hinge_loss_function.py]()). From this function, `log_loss` is used for a logistic regression from scratch, and compare it to `scikit learn LogistisRegression` (more on this: [02_logistic_regression.py]()). Both results are the same!
* The use of function `predict_proba` to measure the probabilities of each predicted result

## Logistic Regression

> **Important: Logistic regression hyperparameter is `C` (inverse of regularization)** 

* Hyperparameter `C` is inverse of regularization strength (to combat overfitting): larger `C`, smaller regularization, vice versa
* Increase regularization causes training accuracy to decrease, however test accuracy increases. See [03_logistic_regression_regularization_accuracy.py]()

![image](https://user-images.githubusercontent.com/51282928/82472941-10ee3b00-9af3-11ea-82f1-532cd0962fc9.png)

* Regularization decreases probabilities

* Using Grid Search Cross-Validation (recall course **Supervised Learning**) for Feature selection (leaving only the selected features). See [03_logistic_regression_gridsearch_feature_selection]()

## Multi-class Classification

* Is classification and prediction for multi-class data type

Multi class Logistic regression:

![image](https://user-images.githubusercontent.com/51282928/82478933-dc32b180-9afb-11ea-8c92-d516499ec1bd.png)

Multi class SVM:

![image](https://user-images.githubusercontent.com/51282928/82478870-bdccb600-9afb-11ea-90a3-c87cb667ce23.png)

* 2 algorithms: **one-vs-rest** (OVR) and **softmax** (or **multinomial**). Multinomial is a standard in neural network. OVR done by classifying one cluster vs the rest clusters, one-by-one. `lr.fit(x, y==1)`, `lr.fit(x, y==2)`, and so on

Comparison:

* OVR performs in logistic regression not as well as in SVM.

Logistic Regression:

![image](https://user-images.githubusercontent.com/51282928/82478627-63335a00-9afb-11ea-9b70-06ef52bbb1fc.png)

SVM:

![image](https://user-images.githubusercontent.com/51282928/82478300-ef914d00-9afa-11ea-98a6-7a84d3415066.png)

## Support Vector Machine

> **Important: Logistic regression hyperparameter is `C` and `gamma`** 

* Support vectors are incorrectly classified points (points located in the wrong clusters)

![image](https://user-images.githubusercontent.com/51282928/82481001-d8ecf500-9afe-11ea-8f01-5190ed9b83c0.png)

* As `gamma` decreases (to 0.01 etc), the decision boundary becomes linear. As `gamma` increases (above 1), the decision boundary becomes more comples. But, higher `gamma` can cause **overfitting**
* To search the best `gamma`, like in logistic regression, we use **Grid Search CV**. See [04_SVM_gridsearch.py]()
* Jointly grid search to tune `C` and `gamma` hyperparameters. See [04_SVM_joint_gridsearch.py]()

```
Best CV params {'C': 10, 'gamma': 0.0001}
Best CV accuracy 0.9988864142538976
Test accuracy of best grid search hypers: 0.9988876529477196
```

## Stochastic Gradient Classifier 

* Both logistic regression and SVM loss function can be accessed in SGD Classifier

```
from sklearn.linear_model import SGDClassifier
logreg = SGDClassifier(loss='log')
linsvm = SGDClassifier(loss='hinge')
```

* Grid search CV hyperparameter tuning to determine which `loss` and `penalty` are best used. See more [04_SGDClassifier_gridsearch.py]()

![image](https://user-images.githubusercontent.com/51282928/82483474-a80ebf00-9b02-11ea-9f54-2357bbb150e8.png)
