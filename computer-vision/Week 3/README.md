# Week 3: Low, Mid, and High Level Vision

## Low-level vision:
* Identifying motion of object (optical flow)
![image](https://user-images.githubusercontent.com/51282928/81851025-0972e300-9583-11ea-8c65-dee15987ca48.png)

* Filters and convolutions to identify a pattern/texture (repetitive pattern)
![image](https://user-images.githubusercontent.com/51282928/81850793-abde9680-9582-11ea-9aaf-d0666297569c.png)

* Seeking pattern (salient featuring) to match different images from different viewpoints and using SSD (sum of squared difference) & NCC (Normalized Cross Correlation)
![image](https://user-images.githubusercontent.com/51282928/81850270-f4498480-9581-11ea-9878-e8d30df127aa.png)
![image](https://user-images.githubusercontent.com/51282928/81850419-22c75f80-9582-11ea-8dbf-6094a2267ced.png)
![image](https://user-images.githubusercontent.com/51282928/81850502-425e8800-9582-11ea-8415-12557bfec75b.png)

## Mid-level vision: 
* Segmentation: Separating image and background by separating based on its HSV, RGB spectrum
* Detection of motion of moving object (tracking)
* K-means clustering to separate images

K (K-means coeff.)=7
![image](https://user-images.githubusercontent.com/51282928/81849810-450cad80-9581-11ea-88d4-e78c17f97101.png)
![image](https://user-images.githubusercontent.com/51282928/81849926-76857900-9581-11ea-994c-6244972b2966.png)

* K-means clustering to identify where in the picture multiple objects lie in the same planes

Increasing K will increase detection of how many similar planes (Left K=3, right K=7)

![image](https://user-images.githubusercontent.com/51282928/81851533-d1b86b00-9583-11ea-95ac-352634150468.png)

## High-level vision:
* Visual recognition: identifying objects in a still or moving image, including geometric attributes
* Action recognition: a pattern that is unique to a repetitive motion (waving hand, nodding head, etc)

![image](https://user-images.githubusercontent.com/51282928/81852042-9a968980-9584-11ea-9526-2d25d6759a9c.png)

> **Challenges to high-level vision**:
> 1. Illumination (different angle of lighting) 
> 2. Scale (changing small-large size of an object)
> 3. Deformable objects
> 4. Occlusion
> 5. Cluttered background (background that is having the same color/appearance with the interest object)

Example of problem with visual recognition (inaccurate recognition):
![image](https://user-images.githubusercontent.com/51282928/81852726-aafb3400-9585-11ea-8f8f-4201c89fd5c9.png)
