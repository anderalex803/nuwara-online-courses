# import logistic loss function from another script

from 02_log_and_hinge_loss_function import log_loss

# The logistic loss, summed over training examples
def my_loss(w):
    s = 0
    for i in range(0, 569):
        raw_model_output = w@X[i]
        s = s + log_loss(raw_model_output * y[i])
    return s

# Returns the w that makes my_loss(w) smallest
w_fit = minimize(my_loss, X[0]).x
print(w_fit)

# Compare with scikit-learn's LogisticRegression
lr = LogisticRegression(fit_intercept=False, C=1000000).fit(X,y)
print(lr.coef_)
