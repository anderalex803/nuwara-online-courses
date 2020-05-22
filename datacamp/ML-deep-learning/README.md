# Key Lessons of course Introduction to Deep Learning in Python

> Good article to understand how backpropagation works, [see here](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/)

* Use of gradient descent to update the weight and minimize the error (`predicted - actual`)
* **Backpropagation** for optimization. The time it takes to go through back prop equals to the time it takes to go through forward prop before (e.g. if we had through 4 iterations of back prop, we must have been through 4 forward prop)

## Steps: Make model, compile, fit, and predict

* Make model, compile, fit: See [03_first_keras_neural_network.py]()
* Predict: See [03_neural_network_predict.py]()
* Types of compiler: `Adam` to optimize the model performance
* Loss functions: `mean_squared_error`, `categorical_crossentropy`
* For `categorical_crossentropy`, add `metric='accuracy` and `softmax` activation in the output layer with 2 nodes

## Neural Network for Classification

See more [04_keras_nn_for_classification.py]

* Uses `softmax` activation in the output layer with 2 nodes (2 because of **binary classification**, e.g. survived or not survived)
* Uses `categorical_crossentropy` compiler (discussed above)

## Model Optimization: the loss function must improve over increasing epochs of training

* Use **stochastic gradient descent** (`sgd`) with different **learning rates**
* The **dying neuron problem** --> ReLu makes some neuron 0, slope also 0, so model can't update. Strategy --> `tanh` and `sigmoid` activation function
* The **vanishing gradient** problem 
