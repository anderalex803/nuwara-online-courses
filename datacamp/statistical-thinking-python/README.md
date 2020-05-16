# Key insights from Statistical Thinking In Python course

1. Graphical Exploratory Data Analysis (EDA) vs Quantitative EDA
2. In graphical EDA, the CDF (cumulative distribution function) plot is more robust than histogram and bee-swarm plot. Box-whisker plot is also another robust representation to identify the data outliers. 
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
