# Assignment 6

## Included Files:

* **gradient.py**: A python script analyzing different methods of differentiation in Python as well as methods of plotting gradients
* **t_plate.py**: A 2D contour plot of the heated plate temperature distribution
* **dtdx.png**: A comparative plot of 3 different differentiation methods: Analytically, Central Differencing, and numpy.gradient
* **heat_flow.png**: An vector field displaying the direction of heat flow on top of the contour plot

## Responses

### Question D-i:
At the interior points, the maximum absolute difference is 0, telling us that the numpy.gradient uses the Central Differencing method.

### Question D-ii: 
On the edges, numpy.gradient uses one-sided differencing (forward or backwards). On the interior points, its uses a second order Central Differencing method, leading to much lower error than the edges, where it only uses a single order one-sided differencing method. This makes the edge error a whole order less accurate than the interior points. The step size of dx also significantly affects this. Halving the step size decreases the edge error by a factor of 2, but decreases the interior error by a factor of 4.

### Question E: 
The direction of the arrows (heat flow) are all perpendicular to the contour lines. They all point directly outwards from the hot center.
