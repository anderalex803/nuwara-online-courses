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

## t-SNE Clustering

![image](https://user-images.githubusercontent.com/51282928/82416030-9b0eb300-9aa3-11ea-81dc-c5c297515db1.png)

## Intrinsic dimension

Knowing the intrinsic dimension helps us to reduce the dimension e.g. from 5 or more features into lesser features. Important for unsupervised learning. See [03_PCA_evaluate_intrinsic_dimension.py]()

![image](https://user-images.githubusercontent.com/51282928/82426702-62c2a100-9ab2-11ea-94f3-4b918ed101aa.png)

## Tf-idf Vectorizer and Truncated SVD

Applied to compute frequency of certain words in multiple documents

![image](https://user-images.githubusercontent.com/51282928/82429486-2f821100-9ab6-11ea-8473-60f31f4833bf.png)

Application to a Wikipedia dataset. See [03_wikipedia_truncatedSVD.py](). Make a pipeline that contains Truncated SVD algorithm to reduce dimension as the first step, then chain to K-Means clustering, to sort the frequency of certain words/terms. 

![image](https://user-images.githubusercontent.com/51282928/82430639-cf8c6a00-9ab7-11ea-9c07-c37726068748.png)

## Non-Negative Matrix Factorization (NMF)

Applied to compute frequency of certain words in multiple documents, image encoding, audio spectrographs, etc.

### Application to a Wikipedia dataset. 

* Result below represents the `NMF = 3` result for both actors `Anne Hathaway` and `Denzel Washington`, pointing out to the topics associated these names, which are `acting`. See [04_wikipedia_NMF.py]()

![image](https://user-images.githubusercontent.com/51282928/82432829-ca7cea00-9aba-11ea-8f64-6b34edff3ed8.png)

Also NMF can recognize the topics which belongs to certain words, e.g. the same `Anne Hathaway` and `Denzel Washington`. NMF for the topic `film` is 0.6, meaning that the words belong to topic `film`. See [04_wikipedia_NMF_learn_topics.py]()

![image](https://user-images.githubusercontent.com/51282928/82435215-2ac15b00-9abe-11ea-8d4a-f0e8cf63228c.png)

### Application to LED digit encoding (PCA can't perform well)

![image](https://user-images.githubusercontent.com/51282928/82435703-e4b8c700-9abe-11ea-8df8-9c148d34d678.png)

![image](https://user-images.githubusercontent.com/51282928/82436788-95739600-9ac0-11ea-973a-31ba958003ac.png)

Each of these features represent the intensity of each bars:

![image](https://user-images.githubusercontent.com/51282928/82436545-3150d200-9ac0-11ea-8281-a0fa8a1872c7.png)

## Cosine Similarity: Build a Recommender System using NMF. See [04_NMF_music_recommender_system]()

* Create pipeline to first scale the data, then NMF, then normalize.

![image](https://user-images.githubusercontent.com/51282928/82438267-f4d2a580-9ac2-11ea-9c5e-7d7ae80f3c4a.png)

* Suppose you like `Bruce Springsteen`, this recommender system will recommend you **what other musicians might you like?** using **NMF** to cluster the similar topics between the musicians, then do **cosine similarity**

![image](https://user-images.githubusercontent.com/51282928/82439004-213af180-9ac4-11ea-9f34-564ab7a1d4c4.png)

Output:

![image](https://user-images.githubusercontent.com/51282928/82438716-b4275c00-9ac3-11ea-9915-892484fe3f98.png)
