"Step 1. Make neural network with 50 nodes on outer layer, 32 nodes on hidden layer, with Sequential model"

# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]

# Set up the model: model
model = Sequential()

# Add the first layer
model.add(Dense(50, activation='relu', input_shape=(n_cols,)))

# Add the second layer
model.add(Dense(32, activation='relu', input_shape=(n_cols,)))

# Add the output layer
model.add(Dense(1, input_shape=(n_cols,)))

"Step 2. Compile the model"

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Verify that model contains information from compiling
print("Loss function: " + model.loss)

"Step 3. Fit the model to the predictor and target data"

# Fit the model
model.fit(predictors, target)
