# Key Lessons from Course Tree-Models (CART) in Python

## Decision Tree

* Terms in decision tree: feature `f`, split point `sp`. Its anatomy is defined by root, node, and leaf.
* The aim of decision tree is to maximize the Information Gain `IG`
* The hyperparameter is the `minimum samples per leaf` and the `maximum depth` (like in hierarchial clustering)
* Two kinds of criterion: `gini` and `entropy`. Both produce same accuracy, but `gini` is faster.
* Decision tree is used for both **classification** (as a classifier) and **regression** (as regressor)

![image](https://user-images.githubusercontent.com/51282928/82547179-7f7ad980-9b83-11ea-8550-317a5c440ecd.png)

## Bias-Variance Tradeoff

As complexity increases (`higher maximum depth` and `min samples per leaf`), bias decreases while variance increases. 

![image](https://user-images.githubusercontent.com/51282928/82549073-8f47ed00-9b86-11ea-85de-91a53e1609eb.png)

* To diagnose bias and variance, do **Cross Validation** (CV)
* Types of CV: **K-Fold** and **Hold-out**. K-fold will split the data randomly into trains and tests, `X` times (e.g. 5 times for 5-fold, 10 times for 10-fold, etc)

#### [02_cross_validation_diagnose_bias_variance.py]() is a good practice to decide if our selected parameters for a model resulting high variance / high bias

Steps:
* Step 1. Instantiate an ML model: DecisionTree
* Step 2. Compute Root Mean Squared error mean from CV
* Step 3. Compute RMSE of the train set
* Step 4. Decide if it has high variance or high bias

![image](https://user-images.githubusercontent.com/51282928/82550824-56f5de00-9b89-11ea-8b22-c05723a6ebce.png)

![image](https://user-images.githubusercontent.com/51282928/82550900-73921600-9b89-11ea-85bd-4910f0b57f87.png)

## Ensemble Learning 

* Combine multiple models to a meta-model, purpose --> increasing accuracy
* 3 techniques: Voting Classifier, Bagging, Random Forest

### Voting Classifier

**See: [02_ensemble_knn+logistic+decisiontree.py]()**

### Bagging (Bootstrap Aggregation),

* For classfication and regression
* Increase accuracy
* Averagely 63% of data are bootstrap sampled, while the 37% aren't sampled --> Out-of Bag (OOB)

### Random Forest

* We can evaluate which features are important to fit and predict the data.
* See more: [03_random_forest_regressor.py]()

### Adaboost (Adaptive Boosting)

See more: [04_adaboost_roc_auc_scoring.py](). This time the `metric` to evaluate is not `accuracy`, but `ROC AUC score` (see previous course Supervised Learning with scikit-learn)

### Gradient Boosting

See more: [04_gradient_boosting.py](). The `metric` to evaluate is Root Mean Squared Error (RMSE)

### Stochastic Gradient Boosting

SGBT uses the same `GradientBoostingRegressor` function, but now added with more parameters such as `max_features` and `subsample` (how many percent data will be sampled)

See more: [04_stochastic_gradient_boosting.py](). The `metric` to evaluate is Root Mean Squared Error (RMSE)
