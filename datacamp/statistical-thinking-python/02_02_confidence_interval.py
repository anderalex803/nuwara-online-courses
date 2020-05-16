# confidence interval e.g. 95% confidence is percentile at 2.5th and 97.5th of data

lower_interval_limit = np.percentile(data, 2.5)
upper_interval_limit = np.percentile(data, 97.5)
