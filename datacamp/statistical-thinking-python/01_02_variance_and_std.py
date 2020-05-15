" Compute variance step-by-step and using build-in function np.var"

# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = differences**2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results
print(variance_explicit, variance_np)

"Compute standard deviation using square root of variance and using np.std"

# Print the square root of the variance = std
print(np.sqrt(variance_explicit))

# Print the standard deviation
print(np.std(versicolor_petal_length))
