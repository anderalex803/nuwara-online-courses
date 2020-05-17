# Wrapping Up of Part 2 Course: Darwin Evolutionary Theory on Daphne Major Finch Beaks

## EDA of beak depths of Darwin's finches

[Task 1](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/datacamp/statistical-thinking-python/02_05_Task1.py)

For your first foray into the Darwin finch data, you will study how the beak depth (the distance, top to bottom, of a closed beak) of the finch species *Geospiza scandens* has changed over time. The Grants have noticed some changes of beak geometry depending on the types of seeds available on the island, and they also noticed that there was some interbreeding with another major species on Daphne Major, *Geospiza fortis*. These effects can lead to changes in the species over time.

In the next few problems, you will look at the beak depth of *G. scandens* on Daphne Major in 1975 and in 2012. To start with, let's plot all of the beak depth measurements in 1975 and 2012 in a bee swarm plot.

The data are stored in a pandas DataFrame called `df` with columns `'year'` and `'beak_depth'`. The units of beak depth are millimeters (mm)

**Instructions**

* Create the beeswarm plot.
* Label the axes.
* Show the plot.

## ECDFs of beak depths

[Task 2](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/datacamp/statistical-thinking-python/02_05_Task2.py)

While bee swarm plots are useful, we found that ECDFs are often even better when doing EDA. Plot the ECDFs for the 1975 and 2012 beak depth measurements on the same plot.

For your convenience, the beak depths for the respective years has been stored in the NumPy arrays `bd_1975` and `bd_2012`.

**Instructions**

* Compute the ECDF for the 1975 and 2012 data.
* Plot the two ECDFs.
* Set a 2% margin and add axis labels and a legend to the plot.
* Hit 'Submit Answer' to view the plot!

## Parameter estimates of beak depths

[Task 3](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/datacamp/statistical-thinking-python/02_05_Task3.py)

Estimate the difference of the mean beak depth of the G. scandens samples from 1975 and 2012 and report a 95% confidence interval.

Since in this exercise you will use the `draw_bs_reps()` function you wrote in chapter 2, it may be helpful to refer back to it.

**Instructions**

* Compute the difference of the sample means.
* Take 10,000 bootstrap replicates of the mean for the 1975 beak depths using your `draw_bs_reps()` function. Also get 10,000 bootstrap replicates of the mean for the 2012 beak depths.
* Subtract the 1975 replicates from the 2012 replicates to get bootstrap replicates of the difference of means.
* Use the replicates to compute the 95% confidence interval.
* Hit 'Submit Answer' to view the results!

## Hypothesis test: Are beaks deeper in 2012?

[Task 4](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/datacamp/statistical-thinking-python/02_05_Task4.py)

Your plot of the ECDF and determination of the confidence interval make it pretty clear that the beaks of *G. scandens* on Daphne Major have gotten deeper. But is it possible that this effect is just due to random chance? In other words, what is the probability that we would get the observed difference in mean beak depth if the means were the same?

Be careful! The hypothesis we are testing is not that the beak depths come from the same distribution. For that we could use a permutation test. The hypothesis is that the means are equal. To perform this hypothesis test, we need to shift the two data sets so that they have the same mean and then use bootstrap sampling to compute the difference of means.

**Instructions**

* Make a concatenated array of the 1975 and 2012 beak depths and compute and store its mean.
* Shift `bd_1975` and `bd_2012` such that their means are equal to the one you just computed for the combined data set.
* Take 10,000 bootstrap replicates of the mean each for the 1975 and 2012 beak depths.
* Subtract the 1975 replicates from the 2012 replicates to get bootstrap replicates of the difference.
* Compute and print the p-value. The observed difference in means you computed in the last exercise is still in your namespace as `mean_diff`.

## EDA of beak length and depth

[Task 5](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/datacamp/statistical-thinking-python/02_05_Task5.py)

The beak length data are stored as `bl_1975` and `bl_2012`, again with units of millimeters (mm). You still have the beak depth data stored in `bd_1975` and `bd_2012`. Make scatter plots of beak depth (y-axis) versus beak length (x-axis) for the 1975 and 2012 specimens.

**Instructions**

* Make a scatter plot of the 1975 data. Use the `color='blue'` keyword argument. Also use an `alpha=0.5` keyword argument to have transparency in case data points overlap.
* Do the same for the 2012 data, but use the `color='red'` keyword argument.
* Add a legend and label the axes.
* Show your plot.

## Linear regressions

[Task 6]()

Perform a linear regression for both the 1975 and 2012 data. Then, perform pairs bootstrap estimates for the regression parameters. Report 95% confidence intervals on the slope and intercept of the regression line.

You will use the `draw_bs_pairs_linreg()` function you wrote back in chapter 2.

As a reminder, its call signature is `draw_bs_pairs_linreg(x, y, size=1)`, and it returns `bs_slope_reps` and `bs_intercept_reps`. The beak length data are stored as `bl_1975` and `bl_2012`, and the beak depth data is stored in `bd_1975` and `bd_2012`.

**Instructions**

* Compute the slope and intercept for both the 1975 and 2012 data sets.
* Obtain 1000 pairs bootstrap samples for the linear regressions using your * `draw_bs_pairs_linreg()` function.
* Compute 95% confidence intervals for the slopes and the intercepts.

## Displaying the linear regression results

[Task 7]

Now, you will display your linear regression results on the scatter plot, the code for which is already pre-written for you from your previous exercise. To do this, take the first 100 bootstrap samples (stored in `bs_slope_reps_1975`, `bs_intercept_reps_1975`, `bs_slope_reps_2012`, and `bs_intercept_reps_2012`) and plot the lines with `alpha=0.2` and `linewidth=0.5` keyword arguments to `plt.plot()`

**Instructions**

* Generate the x-values for the bootstrap lines using `np.array()`. They should consist of 10 mm and 17 mm.
* Write a `for` loop to plot 100 of the bootstrap lines for the 1975 and 2012 data sets. The lines for the 1975 data set should be `'blue'` and those for the 2012 data set should be `'red'`.
* Hit 'Submit Answer' to view the plot!

## Beak length to depth ratio

[Task 8]()

The linear regressions showed interesting information about the beak geometry. The slope was the same in 1975 and 2012, suggesting that for every millimeter gained in beak length, the birds gained about half a millimeter in depth in both years. However, if we are interested in the shape of the beak, we want to compare the ratio of beak length to beak depth. Let's make that comparison.

Remember, the data are stored in `bd_1975`, `bd_2012`, `bl_1975`, and `bl_2012`.

**Instructions**

* Make arrays of the beak length to depth ratio of each bird for 1975 and for 2012.
* Compute the mean of the length to depth ratio for 1975 and for 2012.
Generate 10,000 bootstrap replicates each for the mean ratio for 1975 and 2012 using your `draw_bs_reps()` function.
* Get a 99% bootstrap confidence interval for the length to depth ratio for 1975 and 2012.
* Print the results.

## EDA of heritability

[Task 9]()

The array `bd_parent_scandens` contains the average beak depth (in mm) of two parents of the species `G. scandens`. The array `bd_offspring_scandens` contains the average beak depth of the offspring of the respective parents. The arrays `bd_parent_fortis` and `bd_offspring_fortis` contain the same information about measurements from *G. fortis* birds.

Make a scatter plot of the average offspring beak depth (y-axis) versus average parental beak depth (x-axis) for both species. Use the `alpha=0.5` keyword argument to help you see overlapping points.

**Instructions**

* Generate scatter plots for both species. Display the data for *G. fortis* in blue and *G. scandens* in red.
* Set the axis labels, make a legend, and show the plot.

## Correlation of offspring and parental data

[Task 10]()

In an effort to quantify the correlation between offspring and parent beak depths, we would like to compute statistics, such as the Pearson correlation coefficient, between parents and offspring. To get confidence intervals on this, we need to do a pairs bootstrap.

You have already written a function to do pairs bootstrap to get estimates for parameters derived from linear regression. Your task in this exercise is to make a new function with call signature `draw_bs_pairs(x, y, func, size=1)` that performs pairs bootstrap and computes a single statistic on pairs samples defined. The statistic of interest is computed by calling `func(bs_x, bs_y)`. In the next exercise, you will use `pearson_r` for `func`.

**Instructions**

* Set up an array of indices to sample from. (Remember, when doing pairs bootstrap, we randomly choose indices and use those to get the pairs.)
* Initialize the array of bootstrap replicates. This should be a one-dimensional array of length `size`.
* Write a `for` loop to draw the samples.
* Randomly choose indices from the array of indices you previously set up.
* Extract `x` values and `y` values from the input array using the indices you just chose to generate a bootstrap sample.
* Use `func` to compute the statistic of interest from the bootstrap samples of `x` and `y` and store it in your array of bootstrap replicates.
* Return the array of bootstrap replicates.

## Pearson correlation of offspring and parental data

[Task 11]()

The Pearson correlation coefficient seems like a useful measure of how strongly the beak depth of parents are inherited by their offspring. Compute the Pearson correlation coefficient between parental and offspring beak depths for *G. scandens*. Do the same for *G. fortis*. Then, use the function you wrote in the last exercise to compute a 95% confidence interval using pairs bootstrap.

Remember, the data are stored in `bd_parent_scandens`, `bd_offspring_scandens`, `bd_parent_fortis`, and `bd_offspring_fortis`.

**Instructions**

* Use the `pearson_r()` function you wrote in the prequel to this course to compute the Pearson correlation coefficient for G. scandens and G. fortis.
* Acquire 1000 pairs bootstrap replicates of the Pearson correlation coefficient using the `draw_bs_pairs()` function you wrote in the previous exercise for *G. scandens* and *G. fortis*.
* Compute the 95% confidence interval for both using your bootstrap replicates.

## Measuring heritability

[Task 12]()

Remember that the Pearson correlation coefficient is the ratio of the covariance to the geometric mean of the variances of the two data sets. This is a measure of the correlation between parents and offspring, but might not be the best estimate of heritability. If we stop and think, it makes more sense to define heritability as the ratio of the covariance between parent and offspring to the variance of the parents alone. In this exercise, you will estimate the heritability and perform a pairs bootstrap calculation to get the 95% confidence interval.

This exercise highlights a very important point. Statistical inference (and data analysis in general) is not a plug-n-chug enterprise. You need to think carefully about the questions you are seeking to answer with your data and analyze them appropriately. If you are interested in how heritable traits are, the quantity we defined as the heritability is more apt than the off-the-shelf statistic, the Pearson correlation coefficient.

Remember, the data are stored in `bd_parent_scandens`, `bd_offspring_scandens`, `bd_parent_fortis`, and `bd_offspring_fortis`.

**Instructions**

* Write a function `heritability(parents, offspring)` that computes heritability defined as the ratio of the covariance of the trait in parents and offspring divided by the variance of the trait in the parents. Hint: Remind yourself of the `np.cov()` function we covered in the prequel to this course.
* Use this function to compute the heritability for *G. scandens* and *G. fortis*.
* Acquire 1000 bootstrap replicates of the heritability using pairs bootstrap for *G. scandens* and *G. fortis*.
* Compute the 95% confidence interval for both using your bootstrap replicates.
Print the results.

## Is beak depth heritable at all in G. scandens?

[Task 13]()

The heritability of beak depth in *G. scandens* seems low. It could be that this observed heritability was just achieved by chance and beak depth is actually not really heritable in the species. You will test that hypothesis here. To do this, you will do a pairs permutation test.

**Instructions**

* Initialize your array of replicates of heritability. We will take 10,000 pairs permutation replicates.
- Write a `for` loop to generate your replicates.
- Permute the bd_parent_scandens array using `np.random.permutation()`.
* Compute the heritability between the permuted array and the `bd_offspring_scandens` array using the `heritability()` function you wrote in the last exercise. Store the result in the replicates array.
Compute the p-value as the number of replicates that are greater than the observed `heritability_scandens` you computed in the last exercise.
