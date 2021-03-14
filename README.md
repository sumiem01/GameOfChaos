Game of chaos 

The idea of game is that you have 3 points in a plane (not laying on one line).
Starting point:  
Choose randomly one point inside this triangle.
Iterative point: 
Randomly choose one of the vertex of the triangle and add a point in the half of the way to this point. This is your next starting point.
Repeat.

Intuitively when we distribute something randomly inside a shape we should expect just random set of points inside. But adding condition about half of distance between vertices of a triangle we got this beautiful shape called Sierpinski's triangle.

This is how it suppose to look. Blue dots are vertices, Orange dot is starting point, Green ones are next steps of iteration.
![image](https://user-images.githubusercontent.com/26064347/111077460-294f9c00-84f1-11eb-8ae1-b83d878b00a6.png)


I will try to simulate different objects. Maybe in a square or octagon there will be similar fractals. Let's see.

Square game of chaos with standard configuration is just a mess distributed inside this square randomly.  
But we can add another condition e.g. in next iteration we cannot choose the same vertex and we will receive a fractal shape.

Expectations:  
![image](https://user-images.githubusercontent.com/26064347/111076695-a842d580-84ed-11eb-8003-767889932aa4.png)

Reality:  
![image](https://user-images.githubusercontent.com/26064347/111076702-ad078980-84ed-11eb-8b58-e467cc1da545.png)


But after some adjustment (100 000 points, and arguments size = 0.2, alpha = 0.1 in plt.scatter()) reality seems more bearable:  
![image](https://user-images.githubusercontent.com/26064347/111077214-ff49aa00-84ef-11eb-8f04-d6e52df4b8af.png)


