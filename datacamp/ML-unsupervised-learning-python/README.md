# Key Lessons from Supervised Learning in Python course

## K-Means Clustering

* Way to evaluate how many clusters best to cluster the data: cross-tabulation (works for labeled data such as `species` from `iris` data), inertia (inertia and cluster are payoff, determined in the graph as the `elbow`)
* KMeans clustering could be piped in `pipeline` (recall the previous course on [Supervised Learning]()) to parallelize it with **scaling** and **normalizing** data.
* Interesting application of `pipeline`: in clustering which companies have stock moving together (see [01_kmeans_normalize_pipeline.py]())

![image](https://user-images.githubusercontent.com/51282928/82367501-189fd800-9a3e-11ea-9d6d-44bf60635675.png)

## Hierarchial Clustering

* Complete vs Single: Single sorts the hierarchy from the largest distance to the smallest distance, unlike Complete. The following is Single hierarchial type. 

In scipy: Complete --> `linkage(..., method='complete')`, Single --> `linkage(..., method='single')`

![image](https://user-images.githubusercontent.com/51282928/82413824-3ef65f80-9aa0-11ea-89c0-56ae50bc8e0b.png)

* The y-axis in the hierarchial cluster diagram is the **clustering height**. Clustering height is the **distance of each datapoint to the centroid** If we pick for instance maximum height = 16, it will sort how many cluster there are below that height, see [02_hierarchial_extract_label+crosstab.py]()
