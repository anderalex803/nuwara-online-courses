# Key Lessons from Supervised Learning in Python course

K-Means Clustering:

* Way to evaluate how many clusters best to cluster the data: cross-tabulation (works for labeled data such as `species` from `iris` data), inertia (inertia and cluster are payoff, determined in the graph as the `elbow`)
* KMeans clustering could be piped in `pipeline` (recall the previous course on [Supervised Learning]()) to parallelize it with **scaling** and **normalizing** data.
* Interesting application of `pipeline`: in clustering which companies have stock moving together (see [01_kmeans_normalize_pipeline.py]())

![image](https://user-images.githubusercontent.com/51282928/82367501-189fd800-9a3e-11ea-9d6d-44bf60635675.png)
