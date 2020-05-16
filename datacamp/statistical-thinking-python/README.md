# Key insights from Statistical Thinking In Python course

## Part 1

1. Graphical Exploratory Data Analysis (EDA) vs Quantitative EDA
2. In graphical EDA, the **CDF** (cumulative distribution function) plot is more robust than **histogram** and **bee-swarm** plot. Box-whisker plot is also another robust representation to identify the data outliers. Histogram suffers from **binning bias** (its disadvantage). In the histogram below, lesser bin tends to appear like majority votes for McCain (skewed to the right), however in real fact (with more bins) appears majority votes for Obama (skewed to the left). 

![image](https://user-images.githubusercontent.com/51282928/82116439-13b7fb80-9794-11ea-8f6c-b8cd74676e88.png)

3. Covariance is a measure of distance of a data point in `x` to mean of `x`, compared to distance of a data point in `y` to mean of `y`

![image](https://user-images.githubusercontent.com/51282928/82116358-6fce5000-9793-11ea-99b4-a4329424dd30.png)

4. Simulate your data with "hacker statistics": generate random numbers with normal distribution (`np.random.normal`), Poisson distribution (`np.random.poisson`), and exponential distribution (`np.random.exponential`)
5. Binomial distribution becomes **Poisson distribution** in the case of rare events (e.g. the *no-hitter* in baseball game), having **low p, high n**
6. The time interval between the Poisson-distributed rare *no-hitter* events has **exponential distribution** type.
7. Data distribution can be displayed as PMF (probability mass function) or PDF (probability density function). PMF is a discrete function, only at certain occurences (e.g. 0, 1, 2, 3, ...) vs. PDF is a continuous function. 

![image](https://user-images.githubusercontent.com/51282928/82116283-d868fd00-9792-11ea-9bd2-75f9889edbf0.png)

8. Probability in PDF is expressed as the area under the curve. The area always sums to unity (1). E.g. below, 97% probability of light speed below 300,000 km/s and 3% above 300,000 km/s

![image](https://user-images.githubusercontent.com/51282928/82116266-bcfdf200-9792-11ea-8a64-cb441d2436f3.png)

9. How to translate to CDF? At 300,000 km/s light speed measurement, the CDF is 0.75. It means, the probability below 300,000 km/s is 75%, therefore the probability above 300,000 km/s is (100%-75%=25%)

![image](https://user-images.githubusercontent.com/51282928/82116172-e5d1b780-9791-11ea-9ced-8acba9a16510.png)

10. In normal distribution, the peak of PDF is the **mean** of data. The **std** is half of the width of PDF

## Part 2

1. Anscombe quartet: multiple data could have the same summary statistics and have the same linear regression line. E.g. all of the following data have exactly the same regression line, the same mean, the same variance, and the same sum sq. residual. 

![image](https://user-images.githubusercontent.com/51282928/82118506-14578e80-97a2-11ea-9e2f-5e34fe6d0b20.png)

2. Bootstrapping: to replicate a data based on its summary statistics (e.g. mean and variance). Purpose: if we have only 20 data, and predict what the data would be like in the next 1000 data recorded. 
3. Pair bootstrapping: to know how the regression line will vary (confidence interval)

![image](https://user-images.githubusercontent.com/51282928/82118438-af9c3400-97a1-11ea-876c-aa2df6fdcfe0.png)

4. Hypothesis test, p-value<br>
* Permutation hypothesis test: compare a dataset with a dataset 
* Bootstrap hypothesis test: compare a dataset with a value (e.g. comparing dataset of Michelson speed of light experiment with the mean value obtained by Newcomb)

5. Hypothesis testing pipeling:
* Clearly state the null hypothesis
* Define your test statistic
* Generate many sets of simulated data assuming the null hypothesis is true
* Compute the test statistic for each simulated data set
* The p-value is the fraction of your simulated data sets for which the test statistic is at least as extreme as for the real data

> Note: need some time to digest the bootstrap hypothesis testing and p-value concept. Look for the two problems with two scripts here:
> <div>
<img src="https://user-images.githubusercontent.com/51282928/82122083-9e602100-97bb-11ea-9d1b-d8624402e773.png" width="300"/>
</div>
