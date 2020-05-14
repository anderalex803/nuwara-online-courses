# Section 2

## Derivation of FD

* Central FD second-order (accurate): we get the exact solution for problem <img src="https://render.githubusercontent.com/render/math?math=f(x) = x^2">, we get solution <img src="https://render.githubusercontent.com/render/math?math=f'(0)=0">, using <img src="https://render.githubusercontent.com/render/math?math=\Delta x=1">.

However,
* Forward FD first-order: for the same problem <img src="https://render.githubusercontent.com/render/math?math=f(x) = x^2">, we get not accurate solution, <img src="https://render.githubusercontent.com/render/math?math=f'(0)=1">, using <img src="https://render.githubusercontent.com/render/math?math=\Delta x=1">. Using <img src="https://render.githubusercontent.com/render/math?math=\Delta x=1/2">, the solution <img src="https://render.githubusercontent.com/render/math?math=f'(0)=1/2">. Then using <img src="https://render.githubusercontent.com/render/math?math=\Delta x=1/4">, the solution <img src="https://render.githubusercontent.com/render/math?math=f'(0)=1/4">

Therefore, 
* In the forward FD first-order scheme, if we cut the mesh by half, <img src="https://render.githubusercontent.com/render/math?math=\Delta x_2=1/2 \Delta x_1">, the error also cut by half <img src="https://render.githubusercontent.com/render/math?math=O(1)_2=1/2 O(1)_1">.
* For central FD second-order scheme, if we cut the mesh by half, <img src="https://render.githubusercontent.com/render/math?math=\Delta x_2=1/2 \Delta x_1">, the error also cut by one-four <img src="https://render.githubusercontent.com/render/math?math=O(2)_2=1/4 O(2)_1">.

So, central FD second-order is better than forward FD first-order.

**Is higher order always good?** NO, it will be problematic for the **boundary condition**. So, central second-order is enough (and always better than first-order). 

## Basic Iterative Solvers

The SOR (Succesive-over-relaxation) technique:

<img src="https://render.githubusercontent.com/render/math?math=0 &lt \Omega &lt 2">

* <img src="https://render.githubusercontent.com/render/math?math=\Omega &gt 2">: solution blows up
* <img src="https://render.githubusercontent.com/render/math?math=\Omega = 1">: solution equals to Gauss-Seidel
* <img src="https://render.githubusercontent.com/render/math?math=\Omega &lt 1">: solution under-relaxed
* <img src="https://render.githubusercontent.com/render/math?math=\Omega &gt 1">: solution over-relaxed
