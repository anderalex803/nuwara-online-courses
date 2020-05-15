# my-online-courses

A repo for my online courses from EdX, Coursera, etc.

## Course Folder

> Note: Some courses use different languages (non-Python). Here are Jupyter notebooks to run various languages in Google Colab.
> * [Octave](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/various-languages-colab/octave_minimal.ipynb) (issue: can't display image `imshow` through `!octave file.m`)
> * [R](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/various-languages-colab/R_notebook.ipynb)
> * [Fortran and C](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/various-languages-colab/Fortran_and_C.ipynb)

|Course|MOOC|Instructor|University|Folder Link|External material|
|:---:|:---:|:---:|:---:|:---:|:---:|
|Computers, Waves, Simulations|Coursera|Prof. Heiner Igel|Ludwig-Maximillians<br> University (LMU), Germany|[Notebooks4Coursera](https://github.com/yohanesnuwara/my-online-courses/tree/master/Notebooks4Coursera)|[seismo-live](http://www.seismo-live.org/)|
|Computer Vision Basics|Coursera|Radhakrishna Dasari|University at Buffalo,<br> The State University of New York|[computer-vision](https://github.com/yohanesnuwara/nuwara-online-courses/tree/master/computer-vision)<br> (Course practices in MATLAB, open in Colab)|
|Simulation and Modeling of Natural Processes|Coursera|Prof. Bastien Chopard|University of Geneva|||
|Statistical Learning|EdX||Stanford University|||
|High Performance Finite-Element Modeling: Part 1|EdX|Prof. Johan Jansson,<br> Prof. Johan Hoffman|KTH, Sweden|[HPFEM_KTH](https://github.com/yohanesnuwara/my-online-courses/tree/master/HPFEM_KTH)|[Solving PDEs in Python - The FEniCS Tutorial Volume I](https://fenicsproject.org/pub/tutorial/html/ftut1.html)|
|Practical Numerical Methods with Python|Open EdX|Prof. Lorena Barba|George Washington University|[numerical-mooc-barba](https://github.com/yohanesnuwara/nuwara-online-courses/tree/master/numerical-mooc-barba)||
|Machine Learning for Physicists|Zoom course|Prof. Florian Marquardt|Friedrich-Alexander University (FAU) Erlangen-Nürnberg, Germany|[Github Repo](github.com/yohanesnuwara/ML_for_physicist)|[Course website](https://pad.gwdg.de/s/HJtiTE__U)
|Introduction to Computational Fluid Dynamics|Udemy|Robert Spall, PhD|Utah State University|[cfd-robertspall](https://github.com/yohanesnuwara/nuwara-online-courses/tree/master/cfd-robertspall)<br> (Course practices in Fortran)||
|High-Performance Computing with Python 3.x|Udemy|Packt Publishing||[hpc-python](https://github.com/yohanesnuwara/nuwara-online-courses/tree/master/hpc-python)||
|Parallel and Concurrent Programming with Python|Udemy|Packt Publishing||[parallel-programming-python](https://github.com/yohanesnuwara/nuwara-online-courses/tree/master/parallel-programming-python)||
|Differential Equations in Action|Udacity|Prof. Jörn Loviscach|Bielefeld University of Applied Sciences|||

## Datacamp courses
> Each course has pdf materials and code scripts

1. [Statistical Thinking in Python](https://github.com/yohanesnuwara/nuwara-online-courses/tree/master/datacamp/statistical-thinking-python) (Dr. Justin Bois, Caltech)
* Part 1 files initialized with `01_01_` for Chapter 1, `01_02_` for Chapter 2, and so on...
* Part 2 files initialized with `02_01_` for Chapter 1, `02_02_` for Chapter 2, and so on...

## Free lecture recordings in YouTube

1. [Continuum Mechanics](https://www.youtube.com/playlist?list=PLq-Gm0yRYwTg9gY-xhVpZ5LoctJVi-m2S) by Prof. Romesh Batra, Virginia Tech Uni
2. [Finite Element Analysis](https://www.youtube.com/watch?v=oNqSzzycRhw) by Prof. Klaus-Jürgen Bathe, MIT
3. [Computational Fluid Dynamics](https://www.youtube.com/playlist?list=PL30F4C5ABCE62CB61) by Prof. Lorena Barba, George Washington Uni
4. [Reservoir Simulation](https://www.youtube.com/channel/UCkCwNnLZnRoaHYFyKTdySDw) by Prof. John T. Foster, UT Austin
5. [Reservoir Geomechanics](https://www.youtube.com/channel/UCFZu4RgaS8pKsfO75979fvg/playlists) by Dr. Nicolas Espinoza, UT Austin

## Free courseware materials

1. [Petroleum Geology](https://ocw.tudelft.nl/courses/petroleum-geology/) by Prof. Stefan Luthi, Delft  
2. [Rock Mechanics](https://ocw.tudelft.nl/courses/principles-of-rock-mechanics/) by Dr. Ruud Weijermars, Delft
3. [Numerical Method](http://folk.ntnu.no/leifh/teaching/tkt4140/._main000.html) by Leif Rune Hellevik, NTNU

## Archived courses in EdX

1. [Fluid Mechanics](https://courses.edx.org/courses/course-v1:EPFLx+MF201x+1T2018/course/) (Lectures in French: Mécanique des Fluides), Ecole Polytechnique Fédérale de Lausanne

## Materials, Notebooks, Github for Scientific Computation and PDEs

1. Hans Petter Langtangen [Github](https://github.com/hplgit/prog4comp/tree/master/src/py/) linked to his [book](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/books/Langtangen%20-%20Programming%20for%20Computations%20with%20Python.pdf) "Programming for Computation with Python" (+ ODE/PDE)
2. Hans Petter Langtangen [Github](https://github.com/hplgit/scipro-primer) linked to his [book](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/books/Langtangen_APrimerOnScientificProgramming_Python.pdf) "A Primer on Scientific Programming with Python" (+ ODE/PDE)
3. jrjohansson [Github](https://github.com/jrjohansson/scientific-python-lectures) linked to his [PDF materials](https://github.com/yohanesnuwara/nuwara-online-courses/blob/master/books/Scientific-Computing-with-Python.pdf) "Scientific Computing with Python"
4. juanklopper [Github](https://github.com/juanklopper/Differential-Equations)

## FEniCS working in my GWDG Jupyter

**Temporary installation:**
```
TEMP=~/.user-temp conda install -c conda-forge fenics
TEMP=~/.user-temp conda install -c conda-forge mshr=2018 
```
Note: mshr is not available in the newest fenics

**Installation in a new environment:**
```
. /opt/conda/etc/profile.d/conda.sh
conda create -y --prefix ./FENIX
conda activate ./FENIX
conda install -c conda-forge fenics
python3 -m ipykernel install --user --name FENIX --display-name "FENIX"
```
Note: no success, error code in notebook:
```
Could not find DOLFIN pkg-config file. Please make sure appropriate paths are set.
```
